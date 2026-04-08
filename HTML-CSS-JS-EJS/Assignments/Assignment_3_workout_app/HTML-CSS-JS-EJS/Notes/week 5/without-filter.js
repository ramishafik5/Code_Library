function isOdd(num) {
  return num % 2 === 1;
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const oddNumbers = [];
for (let num of nums) {
  if (isOdd(num)) {
    oddNumbers.push(num);
  }
}

console.log(oddNumbers);