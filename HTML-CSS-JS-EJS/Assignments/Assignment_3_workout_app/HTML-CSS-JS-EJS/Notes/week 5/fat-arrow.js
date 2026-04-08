// Standard function
function square(x) {
  return x * x;
}

let result = square(2);
console.log(result);

// fat-arrow function
const square2 = (x) => {
  return x * x;
};

result = square2(3);
console.log(result);

// briefer fat-arrow function
// when curly braces aren't included, the expression
// to the right of the fat arrow is evaluated and returned.
const square3 = (x) => x * x;

result = square3(4);
console.log(result);

// briefest fat-arrow function
// when only one parameter is passed, parenthese
// are not required.
const square4 = x => x * x;

result = square4(5);
console.log(result);