const blogsContainer = document.getElementById('blogs-container');
let cachedBlogs = localStorage.getItem('cachedBlogs');
const batchSize = 2;
let renderedCount = 0;


const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
        if(entry.isIntersecting) {
            const blogEl = entry.target;
            blogEl.classList.add('visible');
            const img = blogEl.querySelector('img[data-src]');
            if(img) {
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
            }
            obs.unobserve(blogEl);
        }
    });
}, { rootMargin: '200px' });


function renderBatch(blogs) {
    const nextBatch = blogs.slice(renderedCount, renderedCount + batchSize);
    nextBatch.forEach(blog => {
        const div = document.createElement('div');
        div.className = 'blog ' + (blog.type === 'featured' ? 'featured' : '');
        div.innerHTML = `
            <a href="${blog.url}" target="_blank" class="blog-link">
                ${blog.cover_image ? `<img data-src="${blog.cover_image}" alt="cover">` : ''}
                <div class="title">${blog.title}</div>
                <div class="date">${blog.date}</div>
                ${blog.description ? `<div class="desc">${blog.description}</div>` : ''}
            </a>
        `;
        blogsContainer.appendChild(div);
        observer.observe(div);
    });
    renderedCount += batchSize;
}


window.addEventListener('scroll', () => {
    if(window.innerHeight + window.scrollY >= document.body.offsetHeight - 300) {
        if(renderedCount < blogs.length) renderBatch(blogs);
    }
});


let blogs = [];
if(cachedBlogs) {
    blogs = JSON.parse(cachedBlogs);
    renderBatch(blogs);
} else {
    blogs = blogsData;
    localStorage.setItem('cachedBlogs', JSON.stringify(blogs));
    renderBatch(blogs);
}
