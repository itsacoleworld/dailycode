# Daily Code 2
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i .
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

# variables
items = [1, 2, 3, 4, 5]

def multiply_list(list):

    total = 1
    for item in list:
        total = total * item
    return total

def get_multiplied_array(list):

    total = multiply_list(list)
    new_array = []

    for item in list:
        multiplied_value = int(total / item)
        new_array.append(multiplied_value)
    return new_array

new_array = get_multiplied_array(items)
print(new_array)
