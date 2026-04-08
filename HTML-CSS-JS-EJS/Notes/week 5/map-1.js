function cube(num) {
  return num * num * num;
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// with named function
const cubes = nums.map(cube);

console.log(cubes);

// with anonymous fat-arrow function
const squares = nums.map((num) => num * num );

console.log(squares);

// Note that nums is unchanged by the map() calls
console.log(nums); // unchanged