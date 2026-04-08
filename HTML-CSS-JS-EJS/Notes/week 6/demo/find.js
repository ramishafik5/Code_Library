// find the data of adults from the students database
const students = [
    {name:'Alex', age:7},
    {name:'Bob', age:10},
    {name:'Peter', age:12},
    {name:'Justin', age:16},
    {name:'Cindy', age:20}
]
function isAdult(students)
{
    return students.age >= 18;
}
const firstAdult = students.find(isAdult)
console.log(firstAdult)
/*let firstAdult;
for(let person of students)
{
    if(isAdult(person))
    {
        firstAdult = person;
        break;
    }
}
console.log(firstAdult)*/