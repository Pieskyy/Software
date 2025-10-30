document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector(".dropbtn");
    const content = document.querySelector(".dropdown-content");

    btn.addEventListener("click", () => {
        if(content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
});
<<<<<<< HEAD
=======
 function filterCards() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {
                const name = card.dataset.name;
                card.style.display = name.includes(query) ? '' : 'none';
            });
        }

        function sortCards() {
            const sortValue = document.getElementById('sortSelect').value;
            const grid = document.getElementById('cardGrid');
            const cards = Array.from(grid.children);

            cards.sort((a, b) => {
                if (sortValue === 'name') {
                    return a.dataset.name.localeCompare(b.dataset.name);
                } else if (sortValue === 'health') {
                    return parseFloat(b.dataset.health) - parseFloat(a.dataset.health);
                } else if (sortValue === 'damage') {
                    return parseFloat(b.dataset.damage) - parseFloat(a.dataset.damage);
                } else if (sortValue === 'elixir') {
                    return parseFloat(a.dataset.elixir) - parseFloat(b.dataset.elixir);
                }
            });
            cards.forEach(card => grid.appendChild(card));
        }
>>>>>>> parent of b469196 (ZX)
