from text_preprocessing.lemmatization import lemmatize_word
from text_preprocessing.ngrams import (
    bigram_impl,
    ngram_impl,
    trigram_impl,
    unigram_impl,
)
from text_preprocessing.nlp_exercise1 import excercise1
from text_preprocessing.regexes import (
    regex_search,
    regex_search_string_array,
    regex_sub_string,
    remove_punctuation,
    remove_punctuation_in_reviews,
)
from text_preprocessing.stemming import stem_word
from text_preprocessing.stopwords import get_stopwords, remove_stopwords
from text_preprocessing.tagging_speech import test_spacy
from text_preprocessing.tokenization import sentence_tokenisation, word_tokenisation


def main():
    # Execute stop words
    print("====================Executing Stop words=================================")
    execute_stopword()
    print("=====================Executing Regex Manipulation========================")
    execute_regex_manipulation()
    print("=====================Executing Tokenization========================")
    execute_tokenize()

    print("=====================Executing Stemming========================")
    execute_stem()

    print("=====================Executing Lemmatizer========================")
    execute_lemmatize()
    print("=====================Executing Ngrams============================")
    execute_ngram()
    print("=====================Executing Unigrams============================")
    unigram_impl()
    print("=====================Executing Bigrams============================")
    bigram_impl()
    print("=====================Executing Trigrams============================")
    trigram_impl()
    print("=====================Executing Execercise one============================")
    exercise_one_impl()
    print("=====================Executing Text Tagging============================")
    execute_text_tagging()


def execute_stopword():
    print(get_stopwords("english"))
    sentence = "it was too far to go to the shop and he did not want her to walk"
    print(remove_stopwords(sentence))


def execute_regex_manipulation():
    # ====================================================================================
    # initilise search string with item that will be found
    searchable_string_exist = r"string containing the pattern"

    # initilise search string with item that will not be found
    searchable_string_not_exist = r"the phrase to find isn't in this string"

    # initilise variable with item i want to find in above string
    search_pattern1 = "pattern"

    print("Result Exist", regex_search(search_pattern1, searchable_string_exist))
    print(
        "Result do not exist",
        regex_search(search_pattern1, searchable_string_not_exist),
    )

    # ====================================================================================
    # pattern, repl, string
    # Search pattern and replace a string with replace_with_string
    search_pattern2 = r"sara"
    replace_with_string = r"sarah"
    string_pattern = r"sara was able to help me find the items i needed quickly"
    regex_sub_string(search_pattern2, replace_with_string, string_pattern)

    # ====================================================================================
    # Search pattern ending with sarah or sara using ?
    # Pull out reviews that mention sara or sarah using ? regex pattern
    customer_reviews = [
        "sam was a great help to me in the store",
        "the cashier was very rude to me, I think her name was eleanor",
        "amazing work from sadeen!",
        "sarah was able to help me find the items i needed quickly",
        "lucy is such a great addition to the team",
        "great service from sara she found me what i wanted",
    ]

    search_pattern3 = r"sarah?"
    print(
        "Get result with sarah or sara",
        regex_search_string_array(search_pattern3, customer_reviews),
    )

    # ====================================================================================
    # search for pattern that start with letter a
    search_pattern4 = r"^a"
    print(
        "Get result for pattern staring with later a",
        regex_search_string_array(search_pattern4, customer_reviews),
    )

    # ====================================================================================
    # search for pattern that end with letter y
    search_pattern5 = r"y$"
    print(
        "Get result for pattern staring with later y",
        regex_search_string_array(search_pattern5, customer_reviews),
    )

    # ====================================================================================
    # search for pattern with pipe | that acts like an or
    search_pattern6 = r"(need|want)ed"
    print(
        "Get result for pipe symbol",
        regex_search_string_array(search_pattern6, customer_reviews),
    )

    # ====================================================================================
    # removing punctuation from string using regex pattern [^\w\s]
    # examples of punctuation include !, ., ,, ?, etc.
    string_with_punctuation = r"this is a string with punctuation! it has commas, full stops. and exclamation marks!"
    print(
        "Removing punctuation from string:", remove_punctuation(string_with_punctuation)
    )

    # ====================================================================================
    # removing punctuation from reviews
    print(
        "Removing punctuation from reviews",
        remove_punctuation_in_reviews(customer_reviews),
    )


def execute_tokenize():
    sentences = "Her cat's name is Luna. Her dog's name is max"
    sentence_2 = "Her cat's name is Luna and her dog's name is max"
    print("Result of Word Tokenisation:", sentence_tokenisation(sentences))
    print("Result of Sentence Tokenisation", word_tokenisation(sentences))
    print("Result of Second Word Tokenisation", word_tokenisation(sentence_2))


def execute_stem():
    connect_tokens = ["connecting", "connected", "connectivity", "connect", "connects"]
    stem_word(connect_tokens)

    learn_tokens = ["learned", "learning", "learn", "learns", "learner", "learners"]
    stem_word(learn_tokens)

    likes_tokens = ["likes", "better", "worse"]
    stem_word(likes_tokens)


def execute_lemmatize():
    connect_tokens = ["connecting", "connected", "connectivity", "connect", "connects"]
    lemmatize_word(connect_tokens)

    learn_tokens = ["learned", "learning", "learn", "learns", "learner", "learners"]
    lemmatize_word(learn_tokens)

    likes_tokens = ["likes", "better", "worse"]
    lemmatize_word(likes_tokens)


def exercise_one_impl():
    excercise1()


def execute_ngram():
    ngram_impl()


def execute_text_tagging():
    test_spacy()
    
if __name__ == "__main__":
    main()
