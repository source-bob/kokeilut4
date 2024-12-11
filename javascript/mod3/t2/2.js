const ul = document.querySelector('#target');

let elements = ['First elem', 'Second elem', 'Third elem'];

for (let i = 0; i < 3; i++) {
    const li = document.createElement('li');
    li.textContent = elements[i];
    
    ul.appendChild(li);
};

const second = document.getElementsByTagName('li')[1];
second.className = 'my-item';