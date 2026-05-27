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
    # print first 5 rows of data
    print(data.head())
   