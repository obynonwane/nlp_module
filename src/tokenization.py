import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# download punkt tokenizer models if not already downloaded
# used for sentence tokenization and word tokenization
# for sentence boundary detection and word boundary detection
# hence detecting where sentences and words start and end and splitting them accordingly
nltk.download("punkt_tab")


def sentence_tokenisation(sentence):
    return sent_tokenize(sentence)


def word_tokenisation(word):
    return word_tokenize(word)
