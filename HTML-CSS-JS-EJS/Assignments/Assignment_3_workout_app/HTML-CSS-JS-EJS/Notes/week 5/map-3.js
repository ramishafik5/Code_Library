function createSelect(values) {
  let select = '<select>\n';
  const options = values.map((value) => 
    `<option value='${value}'>${value}</option>`
  );
  for (option of options) {
    select += '\t' + option + '\n';
  }
  select += '</select>';
  return select;
}

const fruits = ['banana', 'apple', 'peach', 'cherry'];
let select = createSelect(fruits);
console.log(select);