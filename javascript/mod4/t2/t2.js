document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const query = document.getElementById('query').value;
    const resultsContainer = document.querySelector('body');

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const jsonData = await response.json();

        console.log(jsonData);

        resultsContainer.textContent = JSON.stringify(jsonData, null, 2);
    } catch (error) {
        resultsContainer.textContent = `Error: ${error.message}`;
    }
});