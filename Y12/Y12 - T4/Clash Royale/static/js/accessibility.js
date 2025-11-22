let accessibilityEnabled = localStorage.getItem("accessibilityMode") === "true";
if (accessibilityEnabled) {
    document.body.classList.add("accessibility-mode");
}

function speak(text) {
    if (!accessibilityEnabled || !text) return;
    const msg = new SpeechSynthesisUtterance(text);
    msg.rate = 0.95;
    msg.pitch = 0.95;
    speechSynthesis.cancel();
    speechSynthesis.speak(msg);
}

document.addEventListener("DOMContentLoaded", () => {

    const speakableSelector = "button, a, input, textarea, select, [role='button'], [tabindex='0'], h1, h2, h3, h4, h5, h6, label";

    document.querySelectorAll(speakableSelector).forEach(el => {
        el.addEventListener("mouseenter", () => {
            if (!accessibilityEnabled) return;
            let text = el.textContent.trim() || el.value || el.getAttribute("aria-label") || el.title;
            if (!text) {
                const img = el.querySelector("img");
                text = img?.alt || "link";
            }
            speak(text);
        });
        el.addEventListener("click", () => {
            if (!accessibilityEnabled) return;
            let text = el.textContent.trim() || el.value || el.getAttribute("aria-label") || el.title;
            if (!text) {
                const img = el.querySelector("img");
                text = img?.alt || "link";
            }
            speak(text + " selected");
        });
    });

    document.querySelectorAll("img").forEach(img => {
        img.addEventListener("mouseenter", () => {
            if (!accessibilityEnabled) return;
            speak(img.alt || "image");
        });
    });

    const settingsBtn = document.getElementById("settingsButton");
    const settingsDropdown = document.getElementById("settingsDropdown");
    if (settingsBtn) {
        settingsBtn.addEventListener("mouseenter", () => {
            if (!accessibilityEnabled) return;
            const img = settingsBtn.querySelector("img");
            speak(img?.alt || "Settings");
        });
        settingsBtn.addEventListener("click", () => {
            if (!accessibilityEnabled) return;
            const img = settingsBtn.querySelector("img");
            speak((img?.alt || "Settings") + " selected");
        });
    }

    if (settingsBtn && settingsDropdown) {
        settingsBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            settingsDropdown.classList.toggle("open");
        });
        document.addEventListener("click", () => {
            settingsDropdown.classList.remove("open");
        });
    }

    const accBtn = document.getElementById("accessibilityBtn");
    if (accBtn) {
        accBtn.addEventListener("click", () => {
            accessibilityEnabled = !accessibilityEnabled;
            if (accessibilityEnabled) document.body.classList.add("accessibility-mode");
            else document.body.classList.remove("accessibility-mode");
            localStorage.setItem("accessibilityMode", accessibilityEnabled);
            speak("Accessibility mode " + (accessibilityEnabled ? "enabled" : "disabled"));
        });
    }

    document.querySelectorAll(".card").forEach(card => {
        card.addEventListener("mouseenter", () => {
            if (!accessibilityEnabled) return;
            const cardName = card.getAttribute("data-card-name") || card.querySelector("img")?.alt;
            if (cardName) speak(cardName);
        });
        card.addEventListener("focus", () => {
            if (!accessibilityEnabled) return;
            const cardName = card.getAttribute("data-card-name") || card.querySelector("img")?.alt;
            if (cardName) speak(cardName);
        });
    });


    const battleBtn = document.getElementById('battle-btn');
    const battleAudio = document.getElementById('battle-audio');
    const volumeSlider = document.getElementById("musicVolume");


    let musicPlaying = localStorage.getItem("musicPlaying") === "true";
    let musicVolume = parseFloat(localStorage.getItem("musicVolume")) || 0.5;

    if (battleAudio) {
        battleAudio.volume = musicVolume;
        battleAudio.loop = true;
        if (musicPlaying) battleAudio.play().catch(e => console.log("Audio failed:", e));
    }

    if (volumeSlider) volumeSlider.value = musicVolume;


    if (battleBtn && battleAudio) {
        battleBtn.addEventListener('click', () => {
            musicPlaying = !musicPlaying;
            if (musicPlaying) battleAudio.play().catch(e => console.log("Audio failed:", e));
            else battleAudio.pause();
            localStorage.setItem("musicPlaying", musicPlaying);
        });
    }

    if (volumeSlider && battleAudio) {
        volumeSlider.addEventListener('input', () => {
            battleAudio.volume = volumeSlider.value;
            localStorage.setItem("musicVolume", battleAudio.volume);
        });
    }
});
