const currentDate = new Date();
const year = new Date().getFullYear();

document.querySelector("#date").textContent = currentDate.toLocaleDateString("en-US", {dateStyle: "full"});
document.querySelector("#currentYear").textContent = year;

function toggleMenu() {
    console.log(document.getElementById("primaryNav").classList);
    document.getElementById("primaryNav").classList.toggle("hide")
}