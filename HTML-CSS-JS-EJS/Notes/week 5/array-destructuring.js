// Return a random integer
function randInt(low, high) {
  var rndDec = Math.random();
  var rndInt = Math.floor(rndDec * (high - low + 1) + low);
  return rndInt;
}

// Return a random president as an array: [firstName, lastName]
function randPresident() {
  presidents = [
    'George Washington',
    'Thomas Jefferson',
    'Abraham Lincoln',
    'Teddy Roosevelt',
    'Richard Nixon',
    'Ronald Reagan',
    'Barack Obama'
  ];

  const i = randInt(0, presidents.length-1);
  return presidents[i].split(' ');
}

const [firstName, lastName] = randPresident();
console.log('First name:', firstName);
console.log('Last name:', lastName);