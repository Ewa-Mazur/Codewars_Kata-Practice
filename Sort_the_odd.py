# TASK DESCRIPTION
# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order
# while leaving the even numbers at their original positions.

#EXAMPLE: [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]

def sort_array(source_array):
    support_arrey = []

    for i in source_array:
        if i % 2 != 0:
            support_arrey.append(i)

    support_arrey.sort()

    j = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = support_arrey[j]
            j += 1

    return source_array