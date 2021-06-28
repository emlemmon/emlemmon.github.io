const currentDate = new Date();

if (currentDate.getDay() === 5) {
    document.querySelector(".ifFriday").style.display = "block";
}