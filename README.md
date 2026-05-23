# NLP Project

## What this project does
A Natural Language Processing project using Python tools including NLTK, spaCy, TextBlob, and Transformers for text analysis tasks such as stopword removal, sentiment analysis, and text classification.

---

## Project Structure

```
my-project/
│
├── data/
│   ├── raw/              # original data, never touch
│   └── processed/        # cleaned/transformed data
│
├── notebooks/
│   └── exploration.ipynb # jupyter notebooks for experimenting
│
├── src/
│   └── main.py           # your actual python scripts
│
├── outputs/
│   ├── models/           # saved models
│   └── figures/          # charts, plots
│
├── tests/
│   └── test_main.py      # tests
│
├── .gitignore            # files git should ignore
├── environment.yml       # conda full environment
├── requirements.txt      # pip packages only
└── README.md             # this file
```

---

## Setup & Installation

### Option 1 — Using Conda (Recommended)
Recreates the full environment including Python version:

```bash
conda env create -f environment.yml
conda activate my-env
```

### Option 2 — Using pip only
If you are not using Conda:

```bash
pip install -r requirements.txt
```

---

## Generating environment.yml and requirements.txt

These files are **not written manually** — they are generated from your terminal by scanning your active environment.

### Generate `environment.yml` (Conda)
Captures everything: Python version, conda packages, pip packages, and environment name.

```bash
conda activate your-env
conda env export > environment.yml
```

### Generate `requirements.txt` (pip)
Captures only pip-installed packages as a flat list.

```bash
conda activate your-env
pip freeze > requirements.txt
```

### When to regenerate them

| When | Action |
|---|---|
| Setting up project first time | Run both commands |
| Before pushing to GitHub | Run both to capture latest |
| After installing a new package | Run again to update |
| Before sharing with a teammate | Run to make sure it's current |

### What is the difference?

| File | Managed by | Captures |
|---|---|---|
| `environment.yml` | Conda | Python version + conda + pip packages — full blueprint |
| `requirements.txt` | Pip | Pip packages only — ingredients list |

Keep both because:
- Teammates using **Conda** will use `environment.yml`
- Teammates using **plain Python/venv** will use `requirements.txt`
- **Servers and Docker** deployments use `requirements.txt`

---

## Daily Workflow

```bash
# Start working
conda activate your-env

# After installing a new package
pip install somepackage
pip freeze > requirements.txt
conda env export > environment.yml

# Push changes to GitHub
git add .
git commit -m "added somepackage"
git push
```

---

## What is committed to GitHub

| File/Folder | Push to GitHub? |
|---|---|
| `src/` code | Yes |
| `notebooks/` | Yes |
| `README.md` | Yes |
| `environment.yml` | Yes |
| `requirements.txt` | Yes |
| `.gitignore` | Yes |
| `data/raw/` | No — usually too large |
| `outputs/models/` | No — too large |
| `__pycache__/` | No — auto-generated |
| `.env` secrets | Never |

---

## Key Packages

| Package | Purpose |
|---|---|
| `nltk` | Tokenization, stopwords, text processing |
| `spacy` | Advanced NLP pipeline |
| `textblob` | Simple sentiment analysis |
| `vaderSentiment` | Social media sentiment analysis |
| `transformers` | Hugging Face models (BERT, GPT etc.) |
| `scikit-learn` | Machine learning |
| `gensim` | Topic modeling, word embeddings |
| `torch` | Deep learning (PyTorch) |
| `pandas` | Data manipulation |
| `matplotlib` / `seaborn` | Visualizations |
