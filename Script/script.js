const lastMod = document.lastModified;
const year = new Date().getFullYear();

document.getElementById("date").textContent = lastMod;
document.getElementById("currentYear").textContent = year;