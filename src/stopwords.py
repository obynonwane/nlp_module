# stopwords.py
import nltk

# download stopwords if not already downloaded
nltk.download("stopwords")

# import stopwords from nltk corpus
from nltk.corpus import stopwords


def get_stopwords(language="english"):
    # return a setof stop words for a given language
    return stopwords.words(language)


def remove_stopwords(sentence, language="english"):
    # 1.  get stop word
    en_stopword = get_stopwords(language)

    # 2.  split sentence into individual words
    split_sentence = sentence.split()

    # 3. keep only words that are not in stopword list
    clean_word_list = []
    for word in split_sentence:
        if word not in en_stopword:
            clean_word_list.append(word)

    # 4. join the filtered words back
    join_word = " ".join(clean_word_list)

    # return the cleaned word
    return join_word
