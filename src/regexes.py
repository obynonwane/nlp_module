import re


# This function takes a regex pattern and a string,
# and returns the first match of the pattern in the string,
# or None if no match is found.
def regex_search(pattern, string):
    result = re.search(pattern, string)
    return result


# This function takes a regex pattern, a replacement string, and an input string,
# and returns a new string where all occurrences of the pattern
# in the input string are replaced with the replacement string.
def regex_sub_string(pattern, repl, string):
    result = re.sub(pattern, repl, string)
    return result


# This function takes an array of strings and applies the regex substitution
# to each string in the array, returning a new array with the modified strings.
def regex_search_string_array(pattern, string_array):
    new_string_array = []

    for string in string_array:
        new_string = re.search(pattern, string)
        if new_string:
            new_string_array.append(string)

    return new_string_array
