document.addEventListener("DOMContentLoaded", function () { //makes sure page is loaded


    let searchBox = document.getElementById("searchInput");
    let autocompleteBox = document.getElementById("autocompleteList");
    let fieldSelect = document.getElementById("filterField");
    let clearBtn = document.getElementById("clearSearch");
    let resetBtn = document.getElementById("resetView");
    let advToggleBtn = document.getElementById("toggleAdvanced");
    let advPanel = document.getElementById("advancedPanel");
    let cardArea = document.getElementById("cardGrid");
    let allCards = Array.from(document.querySelectorAll(".card"));

    let sortSelect = document.getElementById("sortSelect");
    let sortDirBtn = document.getElementById("sortDirectionBtn");

    let Timer = null;
    let TIME = 300;
    let sortDescending = false; 



    if (advToggleBtn) { //advanced featuress 
        advToggleBtn.addEventListener("click", function () {
            // toggle "show" class
            advPanel.classList.toggle("show");
            advToggleBtn.classList.toggle("active");
        });
    }


    function updateSortArrow() {
        if (sortDescending) {
            sortDirBtn.textContent = "Down"; 
            sortDirBtn.classList.add("desc");
        } else {
            sortDirBtn.textContent = "Up";
            sortDirBtn.classList.remove("desc");
        }
    }


    function makeSortValue() {
        let chosen = sortSelect.value;
        if (!chosen) return "";

        let parts = chosen.split("_"); // e.g "name_asc"
        let field = parts[0];

        if (sortDescending) {
            return field + "_desc";
        } else {
            return field + "_asc";
        }
    }


    function showEveryCard() {
        allCards.forEach(function (card) {
            card.style.display = "";
        });
    }



    async function filterCards(searchText, fieldName) { //filtering
        try {
            let unit = document.getElementById("unit")?.value || ""; // ?.value only gets if its not defined, || "" makes it empty string if undefined
            let rarity = document.getElementById("raritySelect")?.value || "";
            let arena = document.getElementById("arenaSelect")?.value || "";
            let elixMin = document.getElementById("elixirMin")?.value || "";
            let elixMax = document.getElementById("elixirMax")?.value || "";
            let evo = document.getElementById("filterEvo")?.checked ? "1" : "";
            let splash = document.getElementById("filterSplash")?.checked ? "1" : "";
            let spawn = document.getElementById("filterSpawn")?.checked ? "1" : "";
            let sortVal = makeSortValue();

            // Build parameters
            let params = new URLSearchParams();
            params.set("q", searchText); // // same in search.py, search query
            params.set("field", fieldName); // e.g name, description
            params.set("limit", "125"); // max cards to show

            if (unit) params.set("unit", unit); // advanced filters
            if (rarity) params.set("rarity", rarity);
            if (arena) params.set("arena", arena);
            if (elixMin) params.set("elixir_min", elixMin);
            if (elixMax) params.set("elixir_max", elixMax);
            if (evo) params.set("evo", evo);
            if (splash) params.set("splash", splash);
            if (spawn) params.set("spawn", spawn);
            if (sortVal) params.set("sort", sortVal);

            // Ask server for results
            let res = await fetch("/api/search?" + params.toString());
            let data = await res.json();

            if (data.error) {
                console.error("Server error:", data.error);
                showEveryCard();
                return;
            }

            let idSet = new Set(data.map(x => x.id)); // set of IDs in results

            let cardMap = new Map();
            allCards.forEach(function (card) {
                let id = parseInt(card.dataset.cardId);
                cardMap.set(id, card);
            });

            data.forEach(function (item) {
                let card = cardMap.get(item.id);
                if (card) {
                    cardArea.appendChild(card);
                    card.style.display = "";
                }
            });


            allCards.forEach(function (card) {
                let id = parseInt(card.dataset.cardId);
                if (!idSet.has(id)) {
                    card.style.display = "none";
                }
            });

        } catch (err) {
            console.error("Fetch failed:", err);
            showEveryCard();
        }
    }



    searchBox.addEventListener("input", function () { // autocomplete
        let text = searchBox.value.trim();
        let field = fieldSelect.value;

        clearTimeout(Timer);

        if (text === "") {
            autocompleteBox.innerHTML = "";
            showEveryCard();
            return;
        }


        Timer = setTimeout(async function () {
            try {
                let adv = new URLSearchParams();
                adv.set("q", text);
                adv.set("field", field);
                adv.set("limit", "8");

                // advanced filter
                let unit = document.getElementById("unitselect")?.value || "";
                let rarity = document.getElementById("raritySelect")?.value || "";
                let arena = document.getElementById("arenaSelect")?.value || "";
                let elixMin = document.getElementById("elixirMin")?.value || "";
                let elixMax = document.getElementById("elixirMax")?.value || "";
                let evo = document.getElementById("filterEvo")?.checked ? "1" : "";
                let splash = document.getElementById("filterSplash")?.checked ? "1" : "";
                let spawn = document.getElementById("filterSpawn")?.checked ? "1" : "";

                if (unit) adv.set("unit", unit);
                if (rarity) adv.set("rarity", rarity);
                if (arena) adv.set("arena", arena);
                if (elixMin) adv.set("elixir_min", elixMin);
                if (elixMax) adv.set("elixir_max", elixMax);
                if (evo) adv.set("evo", evo);
                if (splash) adv.set("splash", splash);
                if (spawn) adv.set("spawn", spawn);

                let r = await fetch("/api/search?" + adv.toString());
                let suggestions = await r.json();

                if (!Array.isArray(suggestions)) {
                    autocompleteBox.innerHTML = "";
                    return;
                }

               
                if (suggestions.length > 0) {
                    autocompleteBox.innerHTML = suggestions.map(function (item) {
                        let extra = item[field] ? `<small>${item[field]}</small>` : "";
                        return `
                            <div class="autocomplete-item" data-value="${item.name}">
                                <span>${item.name}</span>
                                ${extra}
                            </div>
                        `;
                    }).join("");


                    let items = document.querySelectorAll(".autocomplete-item");
                    items.forEach(function (box) {
                        box.addEventListener("click", function () {
                            searchBox.value = box.dataset.value;
                            autocompleteBox.innerHTML = "";
                            filterCards(box.dataset.value, field);
                        });
                    });

                } else {
                    autocompleteBox.innerHTML = `
                        <div class="autocomplete-no-results">No results found</div>
                    `;
                }

                filterCards(text, field);

            } catch (error) {
                console.error("Autocomplete failed:", error);
                autocompleteBox.innerHTML = "";
            }
        }, TIME);
    });


    fieldSelect.addEventListener("change", function () {
        filterCards(searchBox.value.trim(), fieldSelect.value);
    });


    let advancedIds = [
        "unitselect", "raritySelect", "arenaSelect",
        "elixirMin", "elixirMax",
        "filterEvo", "filterSplash", "filterSpawn",
        "sortSelect"
    ];

    advancedIds.forEach(function (id) {
        let el = document.getElementById(id);
        if (!el) return;

        el.addEventListener("change", function () {
            filterCards(searchBox.value.trim(), fieldSelect.value);
        });
    });


    sortDirBtn.addEventListener("click", function () {
        sortDescending = !sortDescending;
        updateSortArrow();
        filterCards(searchBox.value.trim(), fieldSelect.value);
    });

    updateSortArrow();


    
    clearBtn.addEventListener("click", function () { // clear search
        searchBox.value = "";
        autocompleteBox.innerHTML = "";
        showEveryCard();
        searchBox.focus();
    });



    resetBtn.addEventListener("click", function () {
        searchBox.value = "";
        autocompleteBox.innerHTML = "";
        showEveryCard();
        fieldSelect.value = "name"; 
        searchBox.focus();
    });


    document.addEventListener("click", function (event) { // hidew if you clcik off 
        if (event.target !== searchBox && !event.target.closest(".autocomplete-item")) {
            autocompleteBox.innerHTML = "";
        }
    });
});
