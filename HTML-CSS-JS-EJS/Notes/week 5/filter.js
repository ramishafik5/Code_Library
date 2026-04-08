function isOdd(num) {
  return num % 2 === 1;
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// with named function
const oddNumbers = nums.filter(isOdd);

console.log(oddNumbers);

// with anonymous fat-arrow function
const evenNumbers = nums.filter((num) => num % 2 === 0);

console.log(evenNumbers);

// Note that nums is unchanged by the filter() calls
console.log(nums);