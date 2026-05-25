from nltk.stem import PorterStemmer

ps = PorterStemmer()


def stem_word(strings):
    for word in strings:
        print(word, ": ", ps.stem(word))
