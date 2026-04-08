function createOption(value) {
  return `<option value='${value}'>${value}</option>`;
}

function createSelect(values) {
  let select = '<select>\n';
  let options = values.map(createOption);
  for (option of options) {
    select += '\t' + option + '\n';
  }
  select += '</select>';
  return select;
}

const fruits = ['banana', 'apple', 'peach', 'cherry'];
let select = createSelect(fruits);
console.log(select);