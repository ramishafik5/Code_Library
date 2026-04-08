function cube(num) {
  return num * num * num;
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const cubes = [];
for (let num of nums) {
  cubes.push(cube(num));
}

console.log(cubes);