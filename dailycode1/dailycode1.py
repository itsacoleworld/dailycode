# Daily Code 1
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# variables
items = [10, 15, 3, 7]
k = 17

# sort items descending
items.sort(reverse=True)

# check if any two numbers in list add to k
def check_match(arr, check):
    for item in arr:
        candidate = check - item
        if candidate in arr:
            response = f"True ({item} + {candidate} = {check})"
            break
        else:
            response = "No match"
    return response

test = check_match(items, k)
print(test)
