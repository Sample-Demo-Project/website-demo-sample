const container = document.getElementById("sample-list");

for (let i = 216; i <= 228; i++) {
    const section = document.createElement("section");
    section.className = "card";

    section.innerHTML = `
        <h2>Sample ${i}</h2>
        <a href="samples/sample-${i}/index.html">View Sample</a>
    `;

    container.appendChild(section);
}
