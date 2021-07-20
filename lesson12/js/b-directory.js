function getBusinessData() {
    const requestURL = "https://emlemmon.github.io/lesson12/directory-info.json";

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
            let website = document.createElement('a');
            let address = document.createElement('p');
            let description = document.createElement('p');
            let logo = document.createElement('img');
            let space = document.createElement('br');

            name.textContent = businesses[i].name;
            phone.textContent = businesses[i].number;
            website.textContent = businesses[i].website;
            website.setAttribute("href", businesses[i].website);
            website.setAttribute("target", "blank");
            address.textContent = businesses[i].address;
            description.textContent = businesses[i].description;
            logo.setAttribute("src", businesses[i].logo.src);
            logo.setAttribute("alt", businesses[i].logo.alt);
            logo.setAttribute("width", businesses[i].logo.width);
            logo.setAttribute("height", businesses[i].logo.height);
            logo.setAttribute("loading", "lazy");

            card.appendChild(name);
            card.appendChild(logo);
            card.appendChild(space);
            card.appendChild(website);
            card.appendChild(phone);
            card.appendChild(address);
            card.appendChild(description);

            document.querySelector("div.businesses-directory").appendChild(card);
            
          }
    })
}

function toggleList() {
    document.querySelector("div.businesses-directory").style.gridTemplateColumns = "1fr";
}

function toggleGrid() {
    document.querySelector("div.businesses-directory").style.gridTemplateColumns = "repeat(auto-fit, minmax(300px, 1fr))";
}

getBusinessData();
