from stopwords import get_stopwords, remove_stopwords


def main():
    # Execute stop words
    print(get_stopwords("english"))
    sentence = "it was too far to go to the shop and he did not want her to walk"
    print(remove_stopwords(sentence))
    #============================================================================
    


if __name__ == "__main__":
    main()
