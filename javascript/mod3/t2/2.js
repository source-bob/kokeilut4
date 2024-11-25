const ul = document.querySelector('#target');

let elements = ['First elem', 'Second elem', 'Third elem'];

for (let i = 0; i < 3; i++) {
    const li = document.createElement('li');
    const text = document.createTextNode(elements[i]);
    
    li.appendChild(text);
    ul.appendChild(li);
};

const second = document.getElementsByTagName('li')[1];
second.classList.toggle('my-item');