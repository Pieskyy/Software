document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const autocompleteList = document.getElementById("autocompleteList");
    const filterField = document.getElementById("filterField");
    const clearSearchBtn = document.getElementById("clearSearch");
    const resetViewBtn = document.getElementById("resetView");
    const cardGrid = document.getElementById("cardGrid");
    const allCards = Array.from(document.querySelectorAll(".card"));
    
    // Debounce timer for autocomplete
    let debounceTimer;
    const DEBOUNCE_DELAY = 300;
    
    // Show all cards
    function showAllCards() {
        allCards.forEach(card => card.style.display = "");
    }
    
    // Filter cards based on search and field
    async function filterCards(searchTerm, field) {
        if (!searchTerm.trim()) {
            showAllCards();
            autocompleteList.innerHTML = "";
            return;
        }
        
        // Fetch matching cards from API
        try {
            const response = await fetch(
                `/api/search?q=${encodeURIComponent(searchTerm)}&field=${field}&limit=500`
            );
            const results = await response.json();
            
            if (results.error) {
                console.error("Search error:", results.error);
                showAllCards();
                return;
            }
            
            // Get matching card IDs
            const matchingIds = new Set(results.map(r => r.id));
            
            // Show/hide cards
            allCards.forEach(card => {
                const cardId = parseInt(card.dataset.cardId);
                card.style.display = matchingIds.has(cardId) ? "" : "none";
            });
        } catch (error) {
            console.error("Fetch error:", error);
            showAllCards();
        }
    }
    
    // Handle autocomplete suggestions
    searchInput.addEventListener("input", (e) => {
        const query = e.target.value.trim();
        const field = filterField.value;
        
        clearTimeout(debounceTimer);
        
        if (!query) {
            autocompleteList.innerHTML = "";
            showAllCards();
            return;
        }
        
        // Fetch suggestions
        debounceTimer = setTimeout(async () => {
            try {
                const response = await fetch(
                    `/api/search?q=${encodeURIComponent(query)}&field=${field}&limit=8`
                );
                const suggestions = await response.json();
                
                if (suggestions.error) {
                    autocompleteList.innerHTML = "";
                    return;
                }
                
                // Render autocomplete list
                if (suggestions.length > 0) {
                    autocompleteList.innerHTML = suggestions
                        .map(item => {
                            const displayField = item[field] || item.name;
                            return `
                                <div class="autocomplete-item" data-value="${item.name}">
                                    <span>${item.name}</span>
                                    ${item[field] ? `<small>${displayField}</small>` : ""}
                                </div>
                            `;
                        })
                        .join("");
                    
                    // Add click handlers to suggestions
                    document.querySelectorAll(".autocomplete-item").forEach(item => {
                        item.addEventListener("click", () => {
                            searchInput.value = item.dataset.value;
                            autocompleteList.innerHTML = "";
                            filterCards(item.dataset.value, field);
                        });
                    });
                } else {
                    autocompleteList.innerHTML = '<div class="autocomplete-no-results">No results found</div>';
                }
                
                // Filter cards in real-time
                filterCards(query, field);
            } catch (error) {
                console.error("Autocomplete fetch error:", error);
                autocompleteList.innerHTML = "";
            }
        }, DEBOUNCE_DELAY);
    });
    
    // Change search field
    filterField.addEventListener("change", () => {
        const query = searchInput.value.trim();
        if (query) {
            filterCards(query, filterField.value);
        }
    });
    
    // Clear search
    clearSearchBtn.addEventListener("click", () => {
        searchInput.value = "";
        autocompleteList.innerHTML = "";
        showAllCards();
        searchInput.focus();
    });
    
    // Reset view (same as clear)
    resetViewBtn.addEventListener("click", () => {
        searchInput.value = "";
        autocompleteList.innerHTML = "";
        showAllCards();
        filterField.value = "name";
        searchInput.focus();
    });
    
    // Hide autocomplete when clicking outside
    document.addEventListener("click", (e) => {
        if (e.target !== searchInput && !e.target.closest(".autocomplete-item")) {
            autocompleteList.innerHTML = "";
        }
    });
});
