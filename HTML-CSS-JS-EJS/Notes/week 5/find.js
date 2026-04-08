function isAdult(person) {
  return person.age >= 18;
}

const people = [
  {name: 'Cindy', age: 6},
  {name: 'Bobby', age: 7},
  {name: 'Jan', age: 10},
  {name: 'Peter', age: 10},
  {name: 'Marsha', age: 12},
  {name: 'Greg', age: 13},
  {name: 'Alice', age: 44}
]

const firstAdult = people.find(isAdult);

console.log(firstAdult);