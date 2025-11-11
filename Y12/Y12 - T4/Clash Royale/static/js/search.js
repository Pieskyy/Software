document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const autocompleteList = document.getElementById("autocompleteList");
    const filterField = document.getElementById("filterField");
    const clearSearchBtn = document.getElementById("clearSearch");
    const resetViewBtn = document.getElementById("resetView");
    const toggleAdvancedBtn = document.getElementById("toggleAdvanced");
    const advancedPanel = document.getElementById("advancedPanel");
    const cardGrid = document.getElementById("cardGrid");
    const allCards = Array.from(document.querySelectorAll(".card"));
    const sortSelect = document.getElementById("sortSelect");
    const sortDirectionBtn = document.getElementById("sortDirectionBtn");
    
    let debounceTimer;
    const DEBOUNCE_DELAY = 300;
    let isSortDescending = false;  // Track sort direction
    
    // Toggle advanced panel visibility
    if (toggleAdvancedBtn) {
        toggleAdvancedBtn.addEventListener("click", () => {
            advancedPanel.classList.toggle("show");
            toggleAdvancedBtn.classList.toggle("active");
        });
    }

    function updateSortButton() {
        if (isSortDescending) {
            sortDirectionBtn.textContent = "↑";
            sortDirectionBtn.classList.add("desc");
        } else {
            sortDirectionBtn.textContent = "↓";
            sortDirectionBtn.classList.remove("desc");
        }
    }

    function getSortValue() {
        const baseSort = sortSelect.value;
        if (!baseSort) return '';
        const [field, _] = baseSort.split('_');
        return isSortDescending ? `${field}_desc` : `${field}_asc`;
    }

    function showAllCards() {
        allCards.forEach(card => card.style.display = "");
    }
    
    async function filterCards(searchTerm, field) {
        // If searchTerm is empty, still call the API to return
        // items that match the selected field (e.g. all cards with evo=true)
        
        try {
            // Gather advanced filters
            const rarity = document.getElementById('raritySelect')?.value || '';
            const arenaVal = document.getElementById('arenaSelect')?.value || '';
            const elixirMin = document.getElementById('elixirMin')?.value || '';
            const elixirMax = document.getElementById('elixirMax')?.value || '';
            const evo = document.getElementById('filterEvo')?.checked ? '1' : '';
            const splash = document.getElementById('filterSplash')?.checked ? '1' : '';
            const spawn = document.getElementById('filterSpawn')?.checked ? '1' : '';
            const sort = getSortValue();

            const params = new URLSearchParams({
                q: searchTerm,
                field: field,
                limit: '500'
            });
            if (rarity) params.set('rarity', rarity);
            if (arenaVal) params.set('arena', arenaVal);
            if (elixirMin) params.set('elixir_min', elixirMin);
            if (elixirMax) params.set('elixir_max', elixirMax);
            if (evo) params.set('evo', evo);
            if (splash) params.set('splash', splash);
            if (spawn) params.set('spawn', spawn);
            if (sort) params.set('sort', sort);

            const response = await fetch(`/api/search?${params.toString()}`);
            const results = await response.json();
            
            if (results.error) {
                console.error("Search error:", results.error);
                showAllCards();
                return;
            }

            const matchingIds = new Set(results.map(r => r.id));
            
            // Create a map of id -> card element for reordering
            const cardMap = new Map();
            allCards.forEach(card => {
                cardMap.set(parseInt(card.dataset.cardId), card);
            });
            
            // Reorder cards in the DOM based on API response order
            const container = cardGrid;
            results.forEach(result => {
                const card = cardMap.get(result.id);
                if (card) {
                    container.appendChild(card);  // Move card to the end (preserves API order)
                    card.style.display = "";     // Show it
                }
            });
            
            // Hide any cards not in results
            allCards.forEach(card => {
                const cardId = parseInt(card.dataset.cardId);
                if (!matchingIds.has(cardId)) {
                    card.style.display = "none";
                }
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
                // include advanced filter params in autocomplete requests
                const advParams = new URLSearchParams({
                    q: query,
                    field: field,
                    limit: '8'
                });
                const rare = document.getElementById('raritySelect')?.value || '';
                const arenaVal = document.getElementById('arenaSelect')?.value || '';
                const elixirMin = document.getElementById('elixirMin')?.value || '';
                const elixirMax = document.getElementById('elixirMax')?.value || '';
                const evo = document.getElementById('filterEvo')?.checked ? '1' : '';
                const splash = document.getElementById('filterSplash')?.checked ? '1' : '';
                const spawn = document.getElementById('filterSpawn')?.checked ? '1' : '';
                if (rare) advParams.set('rarity', rare);
                if (arenaVal) advParams.set('arena', arenaVal);
                if (elixirMin) advParams.set('elixir_min', elixirMin);
                if (elixirMax) advParams.set('elixir_max', elixirMax);
                if (evo) advParams.set('evo', evo);
                if (splash) advParams.set('splash', splash);
                if (spawn) advParams.set('spawn', spawn);

                const response = await fetch(`/api/search?${advParams.toString()}`);
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
    
    // Change search field: always trigger a filter action so selecting a field
    // with an empty query (e.g. 'evo') returns matching cards immediately.
    filterField.addEventListener("change", () => {
        const query = searchInput.value.trim();
        filterCards(query, filterField.value);
    });

    // Advanced filters -> trigger filter on change
    ['raritySelect','arenaSelect','elixirMin','elixirMax','filterEvo','filterSplash','filterSpawn','sortSelect'].forEach(id => {
        const el = document.getElementById(id);
        if (!el) {
            console.warn(`Element with id "${id}" not found`);
            return;
        }
        el.addEventListener('change', () => {
            console.log(`Filter changed: ${id}`);
            filterCards(searchInput.value.trim(), filterField.value);
        });
    });
    
    // Sort direction button
    sortDirectionBtn.addEventListener('click', () => {
        isSortDescending = !isSortDescending;
        updateSortButton();
        filterCards(searchInput.value.trim(), filterField.value);
    });
    
    // Initialize sort button display
    updateSortButton();
    
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
