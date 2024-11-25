let joke = async function(evt) {
    evt.preventDefault();
    
    const query = document.getElementById('query').value;
    
    try {
        const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${query}`);
        const jsonData = await response.json();

        if (jsonData.total === 0) {
            console.log('No jokes found for this query.');
        } else {
            jsonData.result.forEach(joke => {
                console.log(joke.value);
            });
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

const but = document.querySelector('form');
but.addEventListener('submit', joke);