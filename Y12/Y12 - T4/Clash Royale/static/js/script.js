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

    const battleBtn = document.getElementById('battle-btn');
    const battleAudio = document.getElementById('battle-audio');

    if(battleBtn && battleAudio) {
        battleBtn.addEventListener('click', () => {
            battleAudio.play().catch(e => console.log("Audio failed to play:", e));
        });
    }
});