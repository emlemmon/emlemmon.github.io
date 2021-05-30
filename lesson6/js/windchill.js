const temperatureSpan = document.querySelector("#temp");
const windSpeedSpan = document.querySelector("#wind");

//"Wind Chill Temperature is officially defined for 
//temperatures at or below 10 °C (50 °F) and wind speeds above 4.8 kilometers per hour (3.0 mph)."
function windChill(t, w) {
    if (t < 50 && w > 3) {
        //f=35.74+0.6215t−35.75s0.16+0.4275ts0.16, where f is the wind chill factor in Fahrenheit, 
        //t is the air average temperature in Fahrenheit, and s is the wind speed in miles per hour
        return Math.round(35.74 + 0.6215*t - (35.75*Math.pow(w, 0.16)) + (0.4275*t*Math.pow(w, 0.16))) + "°F"
    }
    else {
        return "Not Applicable"
    }
}
document.querySelector("#wind-chill").innerHTML = windChill(parseFloat(temperatureSpan.innerText), parseFloat(windSpeedSpan.innerText))