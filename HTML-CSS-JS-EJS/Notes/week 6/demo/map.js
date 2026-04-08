// map method
// callback method --> function passed to another function

// Standard method
// Write a function in JS in which user 
// input number and get the sube of it as output

// input --> 2, 3 or 4
// output --> 8, 27 or 64
function cube(num)
{
    return num*num*num;
}
// list of number
const nums = [1,2,3,4,5,6,7,8,9]
/*const cubes = []
for(let num of nums)
{
    cubes.push(cube(num))
}
console.log(cubes);*/
// alternate from above
const cubes = nums.map(cube)
console.log(cubes);
// map loops through your original array and call the method for each
// value in the array. It collects the results of your function to 
// create new array with the result

/*<select>
    <option value="Apple">Apple</option>
    <option value="Banana">Banana</option>
    <option value="Cherry">Cherry</option>
</select>*/

createOption = (value) =>
{
    return `<option value="${value}">${value}</option>`
}

createSelect = value => {
    let select = `<select>\n`
    let options = value.map(createOption)
    for(option of options)
    {
        select += '\t' + option + '\n'
    }
    select += `</select>\n`
    return select
}
const fruits = ['Apple','Banana','Cherry']
let select = createSelect(fruits)
console.log(select)















