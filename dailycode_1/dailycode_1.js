/* Daily Code 1
*
* This problem was recently asked by Google.
* Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
* For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
* Bonus: Can you do this in one pass?
*/

// variables
let items = [10, 15, 3, 7]
let k = 17

// sort items
items.sort((a,b) => b - a);

//
function check_match(arr, check){
  let response = ''
  for (i=0; i < arr.length; i++) {
    let candidate = check - arr[i]
    let included = arr.includes(candidate)
    if (included) {
      response = `Yes; (${candidate} + ${arr[i]} = ${check})`
      break;
    }
    else {
      response = "No match"
    }
  }
  return response;
}

let result = check_match(items, k)
console.log(result);
