// ===============================
// Elements
// ===============================

const menuBtn = document.getElementById("menuBtn");
const closeBtn = document.getElementById("closeBtn");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");
const welcome = document.querySelector(".welcome");

// ===============================
// Language Translation
// ===============================

async function changeLanguage(lang) {
    try {
        const response = await fetch(`/translations/${lang}`);
        const t = await response.json();

        document.title = t.app_title;

        document.getElementById("pageTitle").innerText = t.app_title;
        document.getElementById("logoText").innerText = t.app_title;

        document.getElementById("welcomeTitle").innerText =
            t.welcome_title;

        document.getElementById("welcomeText").innerText =
            t.welcomeText;

        document.getElementById("quickServicesTitle").innerText =
            t.quick_services;

        // Sidebar

        const home = document.getElementById("navHome");
        if (home) home.innerText = t.home;

        const birth = document.getElementById("navBirth");
        if (birth) birth.innerText = t.birth;

        const income = document.getElementById("navIncome");
        if (income) income.innerText = t.income;

        const caste = document.getElementById("navCaste");
        if (caste) caste.innerText = t.caste;

        const residence = document.getElementById("navResidence");
        if (residence) residence.innerText = t.residence;

        const marriage = document.getElementById("navMarriage");
        if (marriage) marriage.innerText = t.marriage;

        const driving = document.getElementById("navDriving");
        if (driving) driving.innerText = t.driving;

        const aadhaar = document.getElementById("navAadhaar");
        if (aadhaar) aadhaar.innerText = t.aadhaar;

        const digi = document.getElementById("navDigiLocker");
        if (digi) digi.innerText = t.digilocker;

        const esewa = document.getElementById("navESewa");
        if (esewa) esewa.innerText = t.esewa;

        const seva = document.getElementById("navSevaKendra");
        if (seva) seva.innerText = t.sevakendra;

        const scholarship = document.getElementById("navScholarship");
        if (scholarship) scholarship.innerText = t.scholarship;

        userInput.placeholder = t.placeholder;
    } catch (err) {
        console.log("Translation Error:", err);
    }
}

// ===============================
// Sidebar
// ===============================

function openSidebar() {
    sidebar.classList.add("active");
    overlay.classList.add("active");
}

function closeSidebar() {
    sidebar.classList.remove("active");
    overlay.classList.remove("active");
}

menuBtn.addEventListener("click", openSidebar);

closeBtn.addEventListener("click", closeSidebar);

overlay.addEventListener("click", closeSidebar);

document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
        closeSidebar();
    }
});

// ===============================
// Enter to Send
// ===============================

userInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();

        sendMessage();
    }
});

// ===============================
// Chat
// ===============================

async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) return;

    const language = document.getElementById("language").value;

    if (welcome) {
        welcome.style.display = "none";
    }

    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    userInput.value = "";

    scrollBottom();

    // Typing Indicator

    const typing = document.createElement("div");

    typing.className = "bot-message";
    typing.id = "typing";

    typing.innerHTML = `
        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    chatBox.appendChild(typing);

    scrollBottom();

    try {
        const response = await fetch("/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message,
                language: language
            })
        });

        const data = await response.json();

        const typingBox = document.getElementById("typing");

        if (typingBox) {
            typingBox.remove();
        }

        let html = `
            <div class="bot-message">
                ${data.reply}
        `;

        if (data.links && data.links.length > 0) {
            html += `
                <div class="sources">
                    <h3>🌐 Official Sources</h3>
            `;

            data.links.forEach(link => {
                html += `
                    <a
                        class="source-card"
                        href="${link.url}"
                        target="_blank">

                        <span>🔗</span>

                        <span>${link.title}</span>

                    </a>
                `;
            });

            html += `</div>`;
        }

        html += `</div>`;

        chatBox.innerHTML += html;

        scrollBottom();
    } catch (err) {
        console.error(err);

        const typingBox = document.getElementById("typing");

        if (typingBox) {
            typingBox.remove();
        }

        chatBox.innerHTML += `
            <div class="bot-message">

                ❌ Unable to connect.

                Please try again.

            </div>
        `;

        scrollBottom();
    }
}
function scrollBottom() {
    chatBox.scrollTo({
        top: chatBox.scrollHeight,
        behavior: "smooth"
    });
}

// ===============================
// Sidebar Service Information
// ===============================

document.querySelectorAll(".service-link").forEach(link => {
    link.addEventListener("click", async function (e) {
        e.preventDefault();

        const service = this.dataset.service;

        closeSidebar();

        // Home button
        if (service === "Home") {
            location.reload();
            return;
        }

        if (welcome) {
            welcome.style.display = "none";
        }

        chatBox.innerHTML = `
            <div class="bot-message">
                Loading ${service}...
            </div>
        `;

        scrollBottom();

        try {
            const language =
                document.getElementById("language").value;

            const responseLang = await fetch(`/translations/${language}`);
            const t = await responseLang.json();

            const response = await fetch("/service-info", {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    service: service,
                    language: language
                })
            });

            const data = await response.json();

            // Scholarship page
            if (data.type === "scholarships") {
                let html = `
                    <div class="bot-message">
                        <h1>${data.title}</h1>
                        <p>${data.description}</p>
                `;

                data.items.forEach(item => {
                    html += `
                        <hr>

                        <h2>${item.name}</h2>

                        <p><strong>Eligibility:</strong> ${item.eligibility}</p>

                        <p><strong>Benefits:</strong> ${item.benefits}</p>

                        <p><strong>How to Apply:</strong> ${item.how_to_apply}</p>

                        <a
                            class="source-card"
                            href="${item.official_link}"
                            target="_blank">

                            🔗 Official Website

                        </a>
                    `;
                });

                html += `
                    </div>
                `;

                chatBox.innerHTML = html;

                scrollBottom();

                return;
            }

            // New database response
            if (data.success) {
                let docs = "";

                data.documents.forEach(doc => {
                    docs += `<li>${doc}</li>`;
                });

                let links = "";

                data.links.forEach(link => {
                    links += `
                        <a
                            class="source-card"
                            href="${link.url}"
                            target="_blank">

                            🔗 ${link.title}

                        </a>
                    `;
                });

                chatBox.innerHTML = `
                    <div class="bot-message">

                        <h1>${data.service}</h1>

                        <h2>${t.purpose}</h2>
                        <p>${data.purpose}</p>

                        <h2>${t.documents}</h2>

                        <ul>
                            ${docs}
                        </ul>

                        <h2>${t.fee}</h2>
                        <p>${data.fee}</p>

                        <h2>${t.processing}</h2>
                        <p>${data.processing_time}</p>

                        <h2>${t.offline}</h2>
                        <p>${data.apply_offline}</p>

                        <div class="sources">
                            <h3>${t.sources}</h3>

                            ${links}
                        </div>

                    </div>
                `;
            } else {
                chatBox.innerHTML = `
                    <div class="bot-message">
                        ${data.reply}
                    </div>
                `;
            }

            scrollBottom();
        } catch (err) {
            console.log(err);

            chatBox.innerHTML = `
                <div class="bot-message">
                    Unable to load service information.
                </div>
            `;
        }
    });
});
// ===============================
// Language Selector
// ===============================

document.getElementById("language").addEventListener("change", function () {
    changeLanguage(this.value);
});

// Default Language

changeLanguage("en");

// ======================================
// Voice Recognition
// ======================================

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

if (SpeechRecognition) {
    const recognition = new SpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.lang = "en-IN";

    const micBtn = document.getElementById("micBtn");

    micBtn.addEventListener("click", () => {
        recognition.start();
    });

    recognition.onstart = () => {
        micBtn.classList.add("listening");
    };

    recognition.onend = () => {
        micBtn.classList.remove("listening");
    };

    recognition.onresult = (event) => {
        const speech = event.results[0][0].transcript;

        document.getElementById("userInput").value = speech;

        document.getElementById("userInput").focus();
    };

    recognition.onerror = (event) => {
        console.log(event.error);

        micBtn.classList.remove("listening");
    };
} else {
    alert("Your browser does not support Voice Recognition.");
}