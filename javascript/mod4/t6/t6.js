document.getElementById('jokeForm').addEventListener('submit', async function(evt) {
    evt.preventDefault();

    const query = document.getElementById('query').value;

    try {
        const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${query}`);
        const jsonData = await response.json();

        const jokesContainer = document.getElementById('jokes-container');
        jokesContainer.innerHTML = '';

        if (jsonData.result.length === 0) {
            jokesContainer.innerHTML = '<p>No jokes found for this query.</p>';
        } else {
            jsonData.result.forEach(joke => {
                const article = document.createElement('article');
                const p = document.createElement('p');
                p.textContent = joke.value;
                article.appendChild(p);
                jokesContainer.appendChild(article);
            });
        }
    } catch (error) {
        console.error('Error fetching jokes:', error);
    }
});
