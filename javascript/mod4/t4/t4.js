const style = document.createElement('style');
style.textContent = `
    body {
        font-family: Arial, sans-serif;
    }
    #results {
        display: block;
        width: 100%;
        margin: 0 auto;
    }
    article {
        display: flex;
        flex-direction: column;
        border: 1px solid #ccc;
        width: 90%;
        border-radius: 8px;
        padding: 2%;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        margin: 3%;
    }
    img {
        max-width: 40%;
        border-radius: 5px;
        float: left;
        margin-right: 3%;
        margin-bottom: 1.5%;
    }

    .summary {
        clear: both;
    }

    a {
        display: block;
        margin: 5px 0;
        color: blue;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
`;

document.head.appendChild(style);


const resultsContainer = document.createElement('div');
resultsContainer.id = 'results';
document.body.appendChild(resultsContainer);

document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const query = document.getElementById('query').value;
    
    
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const jsonData = await response.json();
        resultsContainer.innerHTML = '';

        console.log(jsonData);

        jsonData.forEach(result => {
            const show = result.show;

            const article = document.createElement('article');

            const title = document.createElement('h2');
            title.textContent = show.name;

            const link = document.createElement('a');
            link.href = show.url;
            link.textContent = 'Details';
            link.target = '_blank';

            const image = document.createElement('img');
            if (show.image?.medium) {
                image.src = show.image.medium;
                image.alt = show.name;
            }

            const summary = document.createElement('div');
            summary.innerHTML = show.summary || 'No summary available';
            const mainCont = document.createElement('div');

            article.appendChild(title);
            article.appendChild(link);

            image.src = show.image?.medium || 'https://via.placeholder.com/210x295?text=Not%20Found';
            
            mainCont.appendChild(image);
            mainCont.appendChild(summary);
            
            article.appendChild(mainCont);

            resultsContainer.appendChild(article);
        });

    } catch (error) {
        resultsContainer.textContent = `Error: ${error.message}`;
    }
});