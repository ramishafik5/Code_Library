// a function within a function

// Write a program in which make the square of input number and 
// then add 2 in the square.

function add(num)
{
    r = square(num)
    function square(num)
    {
        res = num*num
        return res
    }
    value = r + 2
    return value
}
let output = add(3)
console.log(output)