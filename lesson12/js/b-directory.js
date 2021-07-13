function getBusinessData() {
    const requestURL = "https://emlemmon.github.io/lesson12/js/directory-info.json";

    fetch(requestURL)
    .then(function (response) {
        return response.json();
    })
    .then(function (jsonObject) {
       
        const businesses = jsonObject['businesses']
        
        for (let i = 0; i < businesses.length; i++) {
            let card = document.createElement('section');
            let name = document.createElement('h3');
            let phone = document.createElement('p');
            let website = document.createElement('p');
            let address = document.createElement('p');
            let description = document.createElement('p');
            let logo = document.createElement('img');

            name.textContent = businesses[i].name;
            phone.textContent = businesses[i].number;
            website.textContent = businesses[i].website;
            address.textContent = businesses[i].address;
            description.textContent = businesses[i].description;
            logo.setAttribute("src", businesses[i].logo.source);
            logo.setAttribute("alt", businesses[i].logo.alt);
            logo.setAttribute("width", businesses[i].logo.width);
            logo.setAttribute("height", businesses[i].logo.height);

            card.appendChild(name);
            card.appendChild(logo);
            card.appendChild(website);
            card.appendChild(phone);
            card.appendChild(address);
            card.appendChild(description);

            document.querySelector("div.businesses-directory").appendChild(card);
            
          }
    })
}
getBusinessData();