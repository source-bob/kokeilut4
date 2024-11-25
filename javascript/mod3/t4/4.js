'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const select = document.querySelector('#target');

for (let i = 0; i < students.length; i++) {
  const option = document.createElement('option');
  const text = document.createTextNode(students[i].name);

  option.appendChild(text);
  option.value = students[i].id;
  select.appendChild(option);
};