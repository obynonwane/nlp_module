import matplotlib

matplotlib.use("Agg")
import os

import matplotlib.pyplot as plt
import nltk
import pandas as pd

tokens = [
    "the",
    "rise",
    "of",
    "artificial",
    "intelligence",
    "has",
    "led",
    "to",
    "significant",
    "advancements",
    "in",
    "natural",
    "language",
    "processing",
    "computer",
    "vision",
    "and",
    "other",
    "fields",
    "machine",
    "learning",
    "algorithms",
    "are",
    "becoming",
    "more",
    "sophisticated",
    "enabling",
    "computers",
    "to",
    "perform",
    "complex",
    "tasks",
    "that",
    "were",
    "once",
    "thought",
    "to",
    "be",
    "the",
    "exclusive",
    "domain",
    "of",
    "humans",
    "with",
    "the",
    "advent",
    "of",
    "deep",
    "learning",
    "neural",
    "networks",
    "have",
    "become",
    "even",
    "more",
    "powerful",
    "capable",
    "of",
    "processing",
    "vast",
    "amounts",
    "of",
    "data",
    "and",
    "learning",
    "from",
    "it",
    "in",
    "ways",
    "that",
    "were",
    "not",
    "possible",
    "before",
    "as",
    "a",
    "result",
    "ai",
    "is",
    "increasingly",
    "being",
    "used",
    "in",
    "a",
    "wide",
    "range",
    "of",
    "industries",
    "from",
    "healthcare",
    "to",
    "finance",
    "to",
    "transportation",
    "and",
    "its",
    "impact",
    "is",
    "only",
    "set",
    "to",
    "grow",
    "in",
    "the",
    "years",
    "to",
    "come",
]


# panda is for data manipulation and analysis,
# it provides data structures and functions to work with structured data,
# such as tables and time series. It is commonly used for data cleaning,
# transformation, and analysis tasks in various fields,
# including machine learning and natural language processing.


# matplotlib is a plotting library for the Python programming language
# and its numerical mathematics extension NumPy.


def unigram_impl():
    unigrams = (pd.Series(nltk.ngrams(tokens, 1))).value_counts()
    print(unigrams)
    unigrams[0:10].sort_values().plot.barh(
        color="lightsalmon", width=0.9, figsize=(12, 8)
    )
    plt.title("10 Most Frequently Occuring Unigrams")
    os.makedirs("outputs/figures", exist_ok=True)
    out_path = "outputs/figures/unigrams.png"
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()
    print(f"Saved plot to {out_path}")


def bigram_impl():
    bigrams = (pd.Series(nltk.ngrams(tokens, 2))).value_counts()
    print(bigrams)
    bigrams[0:10].sort_values().plot.barh(
        color="lightsalmon", width=0.9, figsize=(12, 8)
    )
    plt.title("10 Most Frequently Occuring bigrams")
    os.makedirs("outputs/figures", exist_ok=True)
    out_path = "outputs/figures/bigrams.png"
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()
    print(f"Saved plot to {out_path}")


def trigram_impl():
    trigrams = (pd.Series(nltk.ngrams(tokens, 3))).value_counts()
    print(trigrams)
    trigrams[0:10].sort_values().plot.barh(
        color="lightsalmon", width=0.9, figsize=(12, 8)
    )
    plt.title("10 Most Frequently Occuring trigrams")
    os.makedirs("outputs/figures", exist_ok=True)
    out_path = "outputs/figures/trigrams.png"
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()
    print(f"Saved plot to {out_path}")


def ngram_impl():
    print(tokens)
