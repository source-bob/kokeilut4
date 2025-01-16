'use strict';
const names = ['John', 'Paul', 'Jones'];

const ul = document.querySelector('#target');
let html = ``;

for (let i = 0; i < 3; i++) {
    html += `<li>${names[i]}</li>`;
    
};

ul.innerHTML = html;