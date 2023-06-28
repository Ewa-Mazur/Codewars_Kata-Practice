#TASK: Complete the solution so that the function will break up camel casing, using a space between words.
# "camelCasing"  =>  "camel Casing"

input = 'camelCasing'
new_word = ''

for letter in input:
    if letter.isupper():
        new_word += " "
    new_word = new_word + letter


print(new_word)


def solution(input):
    new_word = ''

    for letter in input:
        if letter.isupper():
            new_word += " "
        new_word = new_word + letter

    return new_word