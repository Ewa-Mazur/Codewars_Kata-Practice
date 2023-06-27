"""
TASK: Find the missing letter
Write a method that takes an array of consecutive (increasing) letters
as input and that returns the missing letter in the array.

You will always get a valid array. And it will be always exactly one letter be missing.
The length of the array will always be at least 2.
The array will always contain letters in only one case.
EXAMPLES:
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""
import string


def find_missing_letter(chars):
    alphabet = list(string.ascii_lowercase)
    starting_letter = chars[0].lower()
    alphabet_starting_point = alphabet.index(starting_letter)

    j = 0
    for i in range(alphabet_starting_point, len(alphabet)):
        if alphabet[i] != chars[j].lower():
            result = alphabet[i]
            break
        j += 1

    if chars[0].isupper():
        result = result.upper()

    return result
