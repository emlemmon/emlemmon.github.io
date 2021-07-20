document.getElementById("lastMod").textContent = document.lastModified;

function toggleMenu() {
  document.getElementById("primaryNav").classList.toggle("hide")
}

const hambutton = document.querySelector('.ham');
const primaryNav = document.querySelector('.primaryNav')

//hambutton.addEventListener('click', () => {primaryNav.classList.toggle('responsive')}, false);
window.onresize = () => {if (window.innerWidth > 760) primaryNav.classList.remove('responsive')};


// Get the container element
var btnContainer = document.getElementsByClassName("nav");

// Get all buttons with class="Navbtn" inside the container
var btns = btnContainer.getElementsByClassName("navBtn");

// Loop through the buttons and add the active class to the current/clicked button
for (let i = 0; i < btns.length; i++) {
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
toggleMenu();