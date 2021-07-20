function load_weather() { 
    const apiURL = "https://api.openweathermap.org/data/2.5/onecall?lat=39.82444480667083&lon=-105.11842853061769&exclude=minutely,hourly&appid=9c9e5d67da27a42dc6296ab1c41bc7c4&units=imperial"

    fetch(apiURL)
      .then((response) => response.json())
      .then((jsObject) => {
        
        if (jsObject.alerts) {
          document.getElementById("weather-alert").style.display = "block";
          document.getElementById("alert-title").textContent = jsObject.alerts[0].event;
          document.getElementById("alert-p").textContent = jsObject.alerts[0].description;
        } 
        document.getElementById("weather-img").setAttribute("src", "https://openweathermap.org/img/w/" + jsObject.current.weather[0].icon + ".png")
        document.getElementById("description").textContent = jsObject.current.weather[0].description;
        document.getElementById("current-temp").textContent = jsObject.current.temp;       
        document.getElementById("humidity").textContent = jsObject.current.humidity;  
        
        for (let i=0; i<3; i++) {
          let unixTime = jsObject.daily[i].dt;
          let milliseconds = unixTime * 1000;
          let dateObject = new Date(milliseconds);

          document.getElementById("forecast-heading" + i).textContent = dateObject.toLocaleDateString("en-us");
          document.getElementById("forecast-span" + i).textContent = jsObject.daily[i].temp.max;
          document.getElementById("forecast-img" + i).setAttribute("src", "https://openweathermap.org/img/w/" + jsObject.daily[i].weather[0].icon + ".png");
          document.getElementById("forecast-img" + i).setAttribute("alt", jsObject.daily[i].weather[0].description);
        }
      });
  }
  load_weather();