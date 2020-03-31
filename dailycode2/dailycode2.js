/* Daily Code 2
*
* This problem was asked by Uber.
*
* Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
* For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
* Follow-up: what if you can't use division?
*/

// variables
let items = [1,2,3,4,5]

function multiply_list(arr) {
  total = 1
  for (i=0; i < arr.length; i++) {
    total = total * arr[i]
  }
  return total
}

function get_multiplied_array(arr) {
  total = multiply_list(arr)
  new_array = []

  for (i=0; i < arr.length; i++) {
    multiplied_value = total / arr[i]
    new_array.push(multiplied_value)
  }
  return new_array
}

new_array = get_multiplied_array(items)
console.log(new_array)
