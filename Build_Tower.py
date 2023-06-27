"""
TASK: Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
    [
        "  *  ",
        " *** ",
        "*****"
    ]
"""
def tower_builder(n_floors):
    num_of_stars = []
    result = []

    for i in range(1, 2*n_floors):
        if i%2 != 0:
            num_of_stars.append(i)

    floor_total_width = num_of_stars[-1]

    for i in range(n_floors):
        number_of_white_spaces = int((floor_total_width - num_of_stars[i])/2)
        result.append(((" ") * number_of_white_spaces + ("*" * num_of_stars[i]) + (" ") * number_of_white_spaces))

    return result