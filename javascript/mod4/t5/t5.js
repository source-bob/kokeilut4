

let joke = async function(evt) {
    
    try {
        const response = await fetch('https://api.chucknorris.io/jokes/random');
        const jsonData = await response.json();

        console.log(jsonData.value);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

const but = document.querySelector('button');
but.addEventListener('click', joke);