if (true) {
  let aLet = 'aLet'; // block scoped
  var aVar = 'aVar'; // global
  const A_CONST = 'A_CONST'; // block scoped
  console.log('Found ' + aLet + ' in block.');
  console.log('Found ' + aVar + ' in block.');
  console.log('Found ' + A_CONST + ' in block.');
}
console.log('---------');

try {
  console.log('Found ' + aLet + ' in global scope.');
} catch(e) {
  console.log('Did not find aLet in global scope.');
}

try {
  console.log('Found ' + aVar + ' in global scope.');
} catch(e) {
  console.log('Did not find aVar in global scope.');
}

try {
  console.log('Found ' + A_CONST + ' in global scope.');
} catch(e) {
  console.log('Did not find A_CONST in global scope.');
}
console.log('---------');

function outputLet() {
  try {
    console.log('Found ' + aLet + ' in function.');
  } catch(e) {
    console.log('Did not find aLet in function.');
  }
}

function outputVar() {
  try {
    console.log('Found ' + aVar + ' in function.');
  } catch(e) {
    console.log('Did not find aVar in function.');
  }
}

function outputConst() {
  try {
    console.log('Found ' + A_CONST + ' in function.');
  } catch(e) {
    console.log('Did not find A_CONST in function.');
  }
}

outputLet();
outputVar();
outputConst();