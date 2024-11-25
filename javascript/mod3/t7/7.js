const item = document.querySelector('#trigger');
img = document.querySelector('#target');

let over = function(evt) {
    img.src = 'img/picB.jpg';
};

let out = function(evt) {
    img.src = 'img/picA.jpg';
};

item.addEventListener('mouseover', over);
item.addEventListener('mouseout', out);
