# Text Preprocessing Overview

This document summarizes the text preprocessing implemented in this project, especially the NLTK-based steps.

## NLTK Text Processing Used

### 1. Tokenization

File: `src/text_preprocessing/tokenization.py`

- `nltk.download("punkt")`
  - Downloads the NLTK Punkt tokenizer models.
  - Required for sentence boundary detection in `sent_tokenize()`.

- `sentence_tokenisation(sentence)`
  - Uses `nltk.tokenize.sent_tokenize()`.
  - Splits a text string into a list of sentences.
  - Example: `"Hello world. This is text."` -> `['Hello world.', 'This is text.']`

- `word_tokenisation(word)`
  - Uses `nltk.tokenize.word_tokenize()`.
  - Splits a text string into word tokens and punctuation tokens.
  - Example: `"Hello, world!"` -> `['Hello', ',', 'world', '!']`

### 2. Stopword Handling

File: `src/text_preprocessing/stopwords.py`

- `nltk.download("stopwords", quiet=True)`
  - Downloads the NLTK stopwords list.

- `get_stopwords(language="english")`
  - Returns the NLTK stopword list for the chosen language.
  - Example: `['i', 'me', 'my', ...]`

- `remove_stopwords(sentence, language="english")`
  - Splits a sentence on whitespace.
  - Removes words found in the stopword list.
  - Rejoins the remaining words into a cleaned string.
  - Example: `"it was too far"` -> `"too far"`

## Other Text Processing in the Project

### Regex-based text manipulation

File: `src/text_preprocessing/regexes.py`

This code is not NLTK-specific, but it is also part of text preprocessing:

- `regex_search(pattern, text)`
  - Searches for a regex pattern inside a string.

- `regex_search_string_array(pattern, string_array)`
  - Applies a regex search over a list of strings.

- `regex_sub_string(pattern, replacement, text)`
  - Replaces regex matches in a string.

- `remove_punctuation(text)`
  - Removes punctuation from a single string.

- `remove_punctuation_in_reviews(reviews)`
  - Removes punctuation from each string in a list.

## Usage Example

In `src/main.py`, the following functions are demonstrated:

- `execute_stopword()`
  - Prints English stopwords and a version of a sentence with stopwords removed.

- `execute_tokenize()`
  - Prints sentence tokenization and word tokenization results.

## Notes

- `punkt` is a tokenizer model bundle used by NLTK for sentence and word tokenization.
- `stopwords` is a built-in NLTK corpus that contains common stopwords for many languages.
- If you add more preprocessing steps, add them here and include the relevant file references.
