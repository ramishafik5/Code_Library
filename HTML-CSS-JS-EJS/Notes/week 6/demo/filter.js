// Task --> Find the odd number from given array
// input --> 1,2,3,4,5,6,7,8,9
// output --> 1,3,5,7,9

// Standard method

function isOdd(num)
{
    return num%2==1;
}
const nums = [1,2,3,4,5,6,7,8,9]
/*const OddNum = []
for (let num of nums)
{
    if(isOdd(num))
        OddNum.push(num)
}*/
const OddNum = nums.filter(isOdd)
console.log(OddNum)