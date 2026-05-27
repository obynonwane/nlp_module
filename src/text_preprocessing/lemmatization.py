import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")


lemmatizer = WordNetLemmatizer()


def lemmatize_word(strings):
    for word in strings:
        print(word, ": ", lemmatizer.lemmatize(word))
