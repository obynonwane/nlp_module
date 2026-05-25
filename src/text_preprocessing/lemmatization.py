import nltk
nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()



def lemmatize_word(strings):
    for word in strings:
        print(word, ": ", lemmatizer.lemmatize(word))

