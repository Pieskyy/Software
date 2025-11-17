document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector(".dropbtn");
    const content = document.querySelector(".dropdown-content");

    if (btn && content) {
        btn.addEventListener("click", () => {
            if(content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    }
});
