console.log(1);

document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const resultsContainer = document.getElementById('results');

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const query = document.getElementById('query').value;

        fetch('/api/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query }),
        })
        .then(response => response.json())
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
            resultsContainer.innerHTML = '<p>Erro ao buscar os dados. Por favor, tente novamente mais tarde.</p>';
        });
    });

    function displayResults(data) {
        resultsContainer.innerHTML = ''; // Limpar resultados anteriores
        
        if (data.items.length === 0) {
            resultsContainer.innerHTML = '<p>Nenhum resultado encontrado para esta busca.</p>';
            return;
        }

        const itemList = document.createElement('ul');

        data.items.forEach(item => {
            const listItem = document.createElement('li');
            const itemLink = document.createElement('a');
            itemLink.href = item.link;
            itemLink.textContent = `${item.title} - Preço: ${item.price}`;
            listItem.appendChild(itemLink);
            itemList.appendChild(listItem);
        });

        resultsContainer.appendChild(itemList);
    }
});