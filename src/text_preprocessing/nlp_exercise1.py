import re
from pathlib import Path

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


def excercise1():
    # Define the project root directory
    project_root = Path(__file__).resolve().parents[2]
    # Define candidate paths to the CSV file
    candidate_paths = [
        Path("tripadvisor_hotel_reviews.csv"),
        project_root / "tripadvisor_hotel_reviews.csv",
        project_root / "data" / "raw" / "tripadvisor_hotel_reviews.csv",
        project_root / "data" / "processed" / "tripadvisor_hotel_reviews.csv",
    ]

    # Search for the CSV file in the candidate paths
    csv_path = next((p for p in candidate_paths if p.exists()), None)
    # If the CSV file is not found, print an error message and exit
    if csv_path is None:
        print("ERROR: Could not locate 'tripadvisor_hotel_reviews.csv'.")
        print("Searched in:")
        for p in candidate_paths:
            print("  -", p)
        print("Place the file in the project root or data/raw/ and try again.")
        return

    print(f"Loading data from: {csv_path}")
    # load data
    data = pd.read_csv(csv_path)
    # print summary of data
    print(data.info())
    
    # convert review to lowercase
    data['review_lowercase']= data['Review'].str.lower()
    # print first 5 rows of data to check the new column
    print(data.head())
    
    # en_stopwords is a list of English stop words from the NLTK library. 
    # Stop words are common words that are often removed from text data during 
    # preprocessing because they do not carry significant meaning and can be considered noise in natural language processing tasks. Examples of stop words include "the", "is", "in", "and", etc. By removing stop words, we can focus on the more meaningful words in the text, which can improve the performance of various NLP models and analyses.
    en_stopwords = stopwords.words('english')
    # remove "not" from stop words list as it is important for sentiment analysis
    en_stopwords.remove("not")
    # remove stop words from review column and create new column review_no_stopwords
    # lambda function is used to apply the stop word removal to each review in the review_lowercase column. The lambda function takes a review (x), 
    # splits it into individual words, and then joins back only those words that are not in the en_stopwords list. 
    # The resulting cleaned reviews are stored in a new column called review_no_stopwords.
    data['review_no_stopwords']= data['review_lowercase'].apply(lambda x: ' '.join([word for word in x.split() if word not in (en_stopwords) ]))
    # this will print the first review with stop words removed, allowing us to see the effect of the stop word removal process on the text data.
    print(data['review_no_stopwords'][0])
    
    # remove punctuation from review_no_stopwords column and create new column review_no_stopwords_no_punct
    # The lambda function uses the re.sub() method to replace any character that is not a word character (alphanumeric or underscore) or whitespace with an empty string. 
    # This effectively removes all punctuation from the reviews. The cleaned reviews are stored in a new column called review_no_stopwords_no_punct.
    # row by row, the lambda function takes each review from the review_no_stopwords column, applies the regex substitution to remove punctuation,
    # and saves the cleaned review in the new column review_no_stopwords_no_punct.
    data['review_no_stopwords_no_punct'] = data.apply(lambda x: re.sub(r"[*]", "star", x['review_no_stopwords']), axis=1)
    print(data.head())