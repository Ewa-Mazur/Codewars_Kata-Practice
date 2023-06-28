"""
TASK:
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
EXAMPLE:
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    result = []
    counter = 0

    for number in lst:
        if number == 0:
            counter += 1
        else:
            result.append(number)

    for i in range(counter):
        result.append(0)

    return result
