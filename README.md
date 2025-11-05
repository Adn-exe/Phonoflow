# NameFlow-Bigram  
*A Smooth Character-Level Fantasy Name Generator*

NameFlow-Bigram is a lightweight name generation model that learns how characters follow each other in real names.  
It uses **bigram probabilities** (`P(next character | current character)`) extracted from your dataset and enhances them with:

- **Vowel Balancing** (keeps names smooth and pronounceable)
- **Consonant-Cluster Control** (prevents harsh / unreadable letter runs)
- **Temperature-Based Sampling** (controls creativity vs realism)

This results in names that feel **natural, melodic, and fantasy-inspired** — without using neural networks or heavy models.

---

## ✨ Example Outputs

Kalira Sorian
Serina Aviel
Avelia Miren
Jonel Ariva
Melion Sareen
Talion Verana
Elira Solen

yaml
Copy code

Names are generated from **letter flow**, influenced by your dataset — meaning different training data → different naming style.

---

## 📁 Project Structure

NameFlow-Bigram/
│
├── names.txt # Training dataset (list of input names)
├── nameflow_bigram.ipynb # Main Colab notebook (model + generation)
└── README.md # Project description (this file)

yaml
Copy code

---

## 🚀 How It Works

1. Read all names from the dataset.
2. Create a **character vocabulary**.
3. Count how often each character follows another (bigram matrix).
4. Apply **Laplace smoothing** to avoid zero probabilities.
5. Convert counts into conditional probabilities.
6. Generate names by sampling one character at a time:
   - Apply **temperature** to adjust randomness.
   - **Boost vowels** for smoother rhythm.
   - **Prevent 3 consonants in a row** to maintain readability.
   - Stop when end token is reached.

No neural networks, no transformers — **just statistics + smart sampling**.

---

## 🧠 Why It Sounds Good  
Typical bigram models can sound choppy:
kagt, llay, zrmol...

yaml
Copy code

This model adds:
- **phonetic shaping**
- **natural flow constraints**

So names sound like actual **spoken language patterns**, not random noise.

---

## 💻 Usage

Open the notebook in **Google Colab**:

```bash
File → Upload to Google Colab
Or run locally with Jupyter Notebook.

Make sure your dataset (names.txt) is in the same directory.

📝 Customizing Style
Parameter	Controls	Effect
temperature	randomness	Higher → creative / Lower → realistic
vowel boost (* 1.15)	melody softness	Higher → more lyrical names
consonant cluster guard	pronounceability	Prevents harsh sequences

Tuning these gives Elven, Human, Dark, or Mythic name aesthetics.

📜 License
Free to use, modify, and learn from.
Credit appreciated but not required.

🌟 Author
Built by Adnan ✨
Exploring how small models + human-inspired rules can create expressive language.

yaml
Copy code

---

If you'd like, I can also:

✅ Create a **project banner** (ASCII or logo style)  
✅ Write a **README demo GIF**  
✅ Add **example output section with different styles** (Elven / Dark / Human)  

Just say:  
**"Make it aesthetic"**






