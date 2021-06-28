let lastVisit = localStorage.getItem("lastVisited");
lastVisit = lastVisit ? new Date(lastVisit) : new Date();
let difference_in_time = currentDate.getTime() - lastVisit.getTime();
let difference_in_days = difference_in_time / (1000 * 3600 * 24);
document.querySelector("#days").innerText = Math.round(difference_in_days);
localStorage.setItem("lastVisited", currentDate.toISOString());