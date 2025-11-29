const container = document.getElementById("blogs-container");
const blogs = window.blogsData || [];

if (blogs.length === 0) {
    container.innerHTML = "<p>No blogs found.</p>";
}

blogs.forEach(blog => {
    const div = document.createElement("div");
    div.className = "blog-card";

    div.innerHTML = `
        <a href="${blog.url}" target="_blank">
            <img src="${blog.cover_image || ''}" alt="Blog Image">
            <h3>${blog.title || 'No title'}</h3>
            <p>${blog.date || ''}</p>
        </a>
    `;
    container.appendChild(div);
});