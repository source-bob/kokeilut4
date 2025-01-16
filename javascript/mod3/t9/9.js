let answer;

const button = document.querySelector('#start');


let operation = function(evt) {
    
    let lause = document.querySelector('#calculation').value;
    let marks = ['+', '-', '*', '/'];

    for (let i = 0; i < marks.length; i++) {
        
        check = lause.includes(marks[i]);
        console.log(check);
        
        if (check) {
            
            lause = lause.split(marks[i]);
            let num1 = parseInt(lause[0]);
            let num2 = parseInt(lause[1]);

            if (i === 0) {
                answer = num1 + num2;
            }
            else if (i === 1) {
                answer = num1 - num2;
            }
            else if (i === 2) {
                answer = num1 * num2;
            }
            else if (i === 3) {
                answer = num1 / num2;
            };
            break;
        };
    };
    
    const res = document.querySelector('#result');
    res.innerHTML = answer;
};

button.addEventListener('click', operation);