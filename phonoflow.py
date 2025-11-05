with open('names.txt', 'r') as f:
    words = f.read().strip().split()

import torch

# Build Vocabulary.

chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}

# Build Count Matrix N

N = torch.zeros((len(stoi), len(stoi)), dtype=torch.int32)

for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1, ix2] += 1

# Visualize The 'N' Matrix

import matplotlib.pyplot as plt
# %matplotlib inline

plt.figure(figsize=(16,16))
plt.imshow(N, cmap = 'Blues')
for i in range(27):
  for j in range(27):
    chstr = itos[i] + itos[j]
    plt.text(j, i, chstr, ha = 'center', va = 'bottom', color = 'gray')
    plt.text(j, i, N[i,j].item(), ha = 'center', va = 'top', color = 'gray')
plt.axis('off')

# Laplace smoothing (+1 prevents zero probabilities)

P = (N + 1).float()
P /= P.sum(1, keepdim=True)

# g = torch.Generator().manual_seed(2147483647) For Reproducing Samples.

for _ in range(10):
    out = []
    ix = 0
    while True:
        p = P[ix].clone()

        # Vowels
        for v in "aeiou":
            p[stoi[v]] *= 1.15
        p /= p.sum()

        temperature = 0.9
        logp = torch.log(p + 1e-9)
        p = torch.softmax(logp / temperature, dim=0)

        # Prevent Consonant Clusters
        if len(out) >= 2 and out[-1] not in "aeiou" and out[-2] not in "aeiou":
            mask = torch.zeros_like(p)
            for v in "aeiou":
                mask[stoi[v]] = 1
            p = p * mask + 1e-8
            p /= p.sum()

        ix = torch.multinomial(p, num_samples=1).item()

        # Prevent too-short names
        if ix == 0 and len(out) < 4:
            continue

        # Prevent too-long names
        if len(out) > 12:
            break

        if ix == 0:
            break

        out.append(itos[ix])

    print(''.join(out).capitalize())

def gen_word(start_ix=0):
    out = []
    ix = start_ix
    while True:
        p = P[ix].clone()

        # temperature + vowel bias
        p = torch.softmax(torch.log(p + 1e-9) / 0.8, dim=0)
        for v in "aeiou": p[stoi[v]] *= 1.15
        p /= p.sum()

        # consonant cluster guard
        if len(out) >= 2 and out[-1] not in "aeiou" and out[-2] not in "aeiou":
            mask = torch.zeros_like(p)
            for v in "aeiou": mask[stoi[v]] = 1
            p = (p * mask) + 1e-8
            p /= p.sum()

        ix = torch.multinomial(p, 1).item()

        if ix == 0 and len(out) < 3: continue
        if len(out) > 12 and ix != 0: break
        if ix == 0: break

        out.append(itos[ix])
    return "".join(out).capitalize()

for _ in range(20):
    w1 = gen_word()


    vowels = [c for c in w1.lower() if c in "aeiou"]
    if vowels:
        start = stoi[vowels[-1]]
    else:
        start = 0

    w2 = gen_word(start_ix=start)

    print(w1, w2)

# Evaluate Model Likelihood

log_likelihood = 0.0

for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        prob = P[ix1, ix2]
        log_likelihood += torch.log(prob)
        #print(f"{ch1}{ch2} : {prob:.4f} ")

nll = -log_likelihood
print("Negative Log Likelihood:", nll.item())
total_transitions = sum(len(w)+1 for w in words)
print("Average NLL per transition:", (nll/total_transitions).item())
