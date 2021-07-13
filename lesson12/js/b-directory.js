function getBusinessData() {
    const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

    fetch(requestURL)
    .then(function (response) {
        return response.json();
    })
    .then(function (jsonObject) {
       
        const town = jsonObject['towns'].find(item => item.name == townName);
        
        let card = document.createElement('section');
        let title = document.createElement('h3');

        title.textContent = town.name + " Upcoming Events";
        card.appendChild(title)

        for (let i = 0; i < town.events.length; i++) {
            let indEvent = document.createElement('p');
            indEvent.textContent = town.events[i];
            card.appendChild(indEvent);
        }
        document.querySelector('div.town-events').appendChild(card);
    })
}

const imagesrc = 'https://openweathermap.org/img/w/' + jsObject.weather[0].icon + '.png';  // note the concatenation
    const desc = jsObject.weather[0].description;  // note how we reference the weather array
    //document.getElementById('imagesrc').textContent = imagesrc;  // informational specification only
    document.getElementById('icon').setAttribute('src', imagesrc);  // focus on the setAttribute() method
    document.getElementById('icon').setAttribute('alt', desc);