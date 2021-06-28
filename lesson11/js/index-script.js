const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

fetch(requestURL)
  .then(function (response) {
    return response.json();
  })
  .then(function (jsonObject) {
    //console.table(jsonObject);  //temporary checking for valid response and data parsing
    
    const customImages = {
        "Preston": {order: 0, src: "images/monica-bourgeau-QrgRXH81DXk-unsplash.jpg", alt: "Downtown Preston" },
        "Soda Springs": { order: 1, src: "images/illiya-vjestica-BJzV7Ie6YBY-unsplash.jpg", alt: "Soda Springs Farmland" },
        "Fish Haven": { order: 2, src: "images/timothy-eberly-XemjjFd_4qE-unsplash.jpg", alt: "Sunrise in Fish Haven" },
    }

    const towns = jsonObject['towns'].filter(item => customImages[item.name]);
    towns.sort((first, second) => customImages[first.name].order - customImages[second.name].order);

    for (let i = 0; i < towns.length; i++ ) {
        let card = document.createElement('section');
        let name = document.createElement('h2');
        let motto = document.createElement('p');
        let year_founded = document.createElement('p');
        let current_pop = document.createElement('p');
        let avr_rain = document.createElement('p');
        let image = document.createElement('img');
       

        name.textContent = towns[i].name
        motto.textContent = towns[i].motto;
        year_founded.textContent = 'Year Founded: ' + towns[i].yearFounded;
        current_pop.textContent = 'Current Population: ' + towns[i].currentPopulation;
        avr_rain.textContent = 'Average Yearly Rainfall: ' + towns[i].averageRainfall;
        
        let custom_img = customImages[towns[i].name];
        image.setAttribute("src", custom_img.src);
        image.setAttribute("alt", custom_img.alt);


        card.appendChild(name);
        card.appendChild(image);
        card.appendChild(motto);
        card.appendChild(year_founded);
        card.appendChild(current_pop);
        card.appendChild(avr_rain);

        document.querySelector('div.towns').appendChild(card);
  }});
