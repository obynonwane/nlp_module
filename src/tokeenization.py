import nltk

nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize, word_tokenize


def sentence_tokenisation(sentence):
    return sent_tokenize(sentence)


def word_tokenisation(word):
    return word_tokenize(word)
