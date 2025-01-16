


let answer;
const button = document.querySelector('#start');



let moves = function(evt) {
    const operation = document.getElementById('operation').value;
    const num1 = parseInt(document.getElementById('num1').value);
    const num2 = parseInt(document.getElementById('num2').value);

    if (operation === 'add') {
        answer = num1 + num2;
    }
    else if (operation === 'sub') {
        answer = num1 - num2;
    }
    else if (operation === 'multi') {
        answer = num1 * num2;
    }
    else if (operation === 'div') {
        answer = num1 / num2;
    };
    const res = document.querySelector('#result');
    res.innerHTML = answer;
};

button.addEventListener('click', moves);