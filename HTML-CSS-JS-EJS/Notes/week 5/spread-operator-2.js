const fruits = ['banana', 'apple', 'peach', 'cherry'];
const veggies = ['squash', 'spinach', 'asparagus', 'peas'];

const foods = [];

// Attempt 1
foods.push(fruits);
foods.push(veggies);

console.log('ATTEMPT 1:');
console.log(foods); // foods will contain an array of arrays

// Clear foods
foods.length = 0;

// Attempt 2
foods.push(...fruits);
foods.push(...veggies);

console.log('---------');
console.log('ATTEMPT 2:');
console.log(foods); // foods will now contain an array of strings