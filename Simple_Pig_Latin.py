"""
TASK:
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.
EXAMPLES:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    new_text = ''
    words_arr = text.split()

    for word in words_arr:
        if word.isalnum():
            new_text = new_text + word[1:] + word[0] + 'ay '
        else:
            new_text = new_text + word

    if new_text[-1] == " ":
        new_text = new_text[:-1]

    return new_text
