const blogsContainer = document.getElementById("blogs-container");
let saved = localStorage.getItem("cachedBlogs");
let blogsList = [];
let index = 0;
let amount = 2;

// load images when seen
let observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
        if (entry.isIntersecting) {
            let box = entry.target;
            box.classList.add("visible");

            let img = box.querySelector("img[data-src]");
            if (img) {
                img.src = img.getAttribute("data-src");
                img.removeAttribute("data-src");
            }

            observer.unobserve(box);
        }
    });
}, {
    rootMargin: "200px"
});


// draw some blogs each time
function showMoreBlogs(list) {
    let part = list.slice(index, index + amount);

    part.forEach(function (b) {
        let div = document.createElement("div");
        div.className = "blog";

        if (b.type === "featured") {
            div.className += " featured";
        }

        let imgHtml = "";
        if (b.cover_image) {
            imgHtml = `<img data-src="${b.cover_image}" alt="">`;
        }

        div.innerHTML = `
            <a href="${b.url}" target="_blank" class="blog-link">
                ${imgHtml}
                <div class="title">${b.title}</div>
                <div class="date">${b.date}</div>
                ${b.description ? `<div class="desc">${b.description}</div>` : ""}
            </a>
        `;

        blogsContainer.appendChild(div);
        observer.observe(div);
    });

    index += amount;
}


// load cached or fresh data
if (saved) {
    blogsList = JSON.parse(saved);
    showMoreBlogs(blogsList);
} else {
    blogsList = blogsData;
    localStorage.setItem("cachedBlogs", JSON.stringify(blogsList));
    showMoreBlogs(blogsList);
}


// check scroll for more blogs
window.addEventListener("scroll", function () {
    let bottom = window.innerHeight + window.scrollY;
    let pageHeight = document.body.offsetHeight;

    if (bottom >= pageHeight - 300) {
        if (index < blogsList.length) {
            showMoreBlogs(blogsList);
        }
    }
});
