const currentDate = new Date();
const year = new Date().getFullYear();

document.querySelector("#date").textContent = currentDate.toLocaleDateString("en-US", {dateStyle: "full"});
document.querySelector("#currentYear").textContent = year;

function toggleMenu() {
    console.log(document.getElementById("primaryNav").classList);
    document.getElementById("primaryNav").classList.toggle("hide")
}

// Get the container element
var btnContainer = document.getElementById("primaryNav");

// Get all buttons with class="Navbtn" inside the container
var btns = btnContainer.getElementsByClassName("navBtn");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");

    // If there's no active class
    if (current.length > 0) {
      current[0].className = current[0].className.replace(" active", "");
    }

    // Add the active class to the current/clicked button
    this.className += " active";
  });
}
if (currentDate.getDay() === 5) {
    document.querySelector(".ifFriday").style.display = "block";
}

let lastVisit = localStorage.getItem("lastVisited");
lastVisit = lastVisit ? new Date(lastVisit) : new Date();
let difference_in_time = currentDate.getTime() - lastVisit.getTime();
let difference_in_days = difference_in_time / (1000 * 3600 * 24);
document.querySelector("#days").innerText = Math.round(difference_in_days);
localStorage.setItem("lastVisited", currentDate.toISOString());