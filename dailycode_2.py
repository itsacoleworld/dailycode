#This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

input_array = [1, 2, 3, 4, 5]

# set start of multiplication function to 1 so that index 0 multiplies by 1.
product = 1

def product_of_array(input_array, product):

    for i in reversed(input_array):
        input_array.pop(i)
        print (input_array)

product_of_array(input_array, product)






"""
#solution one

# multiply each item of array by product of previous items
def multiply_array(input_array, product):
    for i in input_array:
        product *= i
    return product

# Divide product of array by each index and append quotient to new array
def new_array(input_array_product, input_array):

    new_product_array = []

    for i in input_array:
        a = input_array_product / i
        new_product_array.append(a)
    return new_product_array


# set variable equal to product of original array
input_array_product = multiply_array(input_array, product)
print (input_array_product)

# set variable equal to new array containing quotients
new_product_array = new_array(input_array_product, input_array)
print (new_product_array)
"""
