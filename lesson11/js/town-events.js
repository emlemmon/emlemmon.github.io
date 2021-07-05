function getEventData(townName) {
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