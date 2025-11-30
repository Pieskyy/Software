document.addEventListener('DOMContentLoaded', function() {
    const blogs = document.querySelectorAll('.blog');
    blogs.forEach((blog, index) => {
        setTimeout(() => {
            blog.classList.add('visible');
        }, index * 10);
    });
});