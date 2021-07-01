function load_weather(location_id) { 
  const apiURL = "https://api.openweathermap.org/data/2.5/weather?id=" + location_id + "&appid=9c9e5d67da27a42dc6296ab1c41bc7c4&units=imperial";

  fetch(apiURL)
    .then((response) => response.json())
    .then((jsObject) => {
      console.log(jsObject);  

      document.getElementById('description').textContent = jsObject.weather[0].main;
      document.getElementById('current-temp').textContent = jsObject.main.temp;
      document.getElementById('wind-speed').textContent = jsObject.wind.speed;
      document.getElementById('humidity').textContent = jsObject.main.humidity;
      document.getElementById('current-temp').textContent = jsObject.main.temp;    

      const imagesrc = 'https://openweathermap.org/img/w/' + jsObject.weather[0].icon + '.png';  // note the concatenation
      const desc = jsObject.weather[0].description;  // note how we reference the weather array
      //document.getElementById('imagesrc').textContent = imagesrc;  // informational specification only
      document.getElementById('icon').setAttribute('src', imagesrc);  // focus on the setAttribute() method
      document.getElementById('icon').setAttribute('alt', desc);
    });

  const forecastAPI_URL = "https://api.openweathermap.org/data/2.5/forecast?id=" + location_id + "&appid=9c9e5d67da27a42dc6296ab1c41bc7c4&units=imperial";

  fetch(forecastAPI_URL)
    .then((response) => response.json())
    .then((jsObject) => {

      console.log(jsObject);

      const forecast_data = jsObject['list'].filter(item => item.dt_txt.endsWith("18:00:00"));
      for (let i = 0; i < forecast_data.length; i++) {
        const current = forecast_data[i];
        document.getElementById("forecast-img" + i).setAttribute("src", 'https://openweathermap.org/img/w/' + current.weather[0].icon + '.png');
        document.getElementById("forecast-img" + i).setAttribute("alt", current.weather[0].description);
        document.getElementById('forecast-span' + i).textContent = current.main.temp;
      }
    })
}