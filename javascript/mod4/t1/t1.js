document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const query = document.getElementById('query').value;
    console.log('Searching for:', query);

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const jsonData = await response.json();
        
        console.log(jsonData);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});