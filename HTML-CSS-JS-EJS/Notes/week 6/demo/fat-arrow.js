// Standard method --> without using ES2015

// Write a function in JS in which user 
// input number and get the square of it as output

// input --> 3, 4 or 5
// output --> 9, 16 or 25
function square(x)
{
    return x * x;
}
console.log(square(3))
// fat-arrow
const square2 = (x) => {
    return x * x
}
console.log(square2(4))

const square3 = x => x * x; // Vue.js
console.log(square3(5))