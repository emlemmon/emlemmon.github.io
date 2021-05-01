const lastMod = document.lastModified;
const year = new Date().getFullYear();

document.querySelector("#date").textContent = lastMod;
document.querySelector("#currentYear").textContent = year;