document.addEventListener('DOMContentLoaded', () => {
    // Set links up to load new pages.
    document.querySelectorAll('.rad-link').forEach(radio => {
        radio.onchange = () => {
            document.querySelector('#features').innerHTML = " ";
            load_page(radio.dataset.ref);
            return false;
        };
    });
});

function fill_content(stats, response) {
        if (stats.speed != null) {
            var stemp = document.getElementById("builder-stats").content.cloneNode(true);
            stemp.querySelector("#template-legend").innerHTML = "Speed";
            stemp.querySelector("#template-feature").innerHTML = "Your speed is " + JSON.stringify(stats.speed) + " ft.";
            document.querySelector('#features').appendChild(stemp);
        }

        if (stats.darkvision != null) {
            var stemp = document.getElementById("builder-stats").content.cloneNode(true);
            stemp.querySelector("#template-legend").innerHTML = "Darkvision";
            stemp.querySelector("#template-feature").innerHTML = "You have darkvision " + JSON.stringify(stats.darkvision) + " ft.";
            document.querySelector('#features').appendChild(stemp);
        }
        

        var stemp = document.getElementById("builder-stats").content.cloneNode(true);
        stemp.querySelector("#template-legend").innerHTML = "Ability";
        var ab = "";
        if (name == "Human") {
            ab = "You get +1 to All abilities as a human"
        } else if (name == "Half-Elf") {
            ab = "You het + 2 CHA and +1 to an Ability of your choice"
        } else if (name == "Tiefling") {
            ab = "Your ability modifier depends on your subrace"
        } else {
            for (var i in stats.ability) {
                ab = ab + "Your " + i.toUpperCase() + " is: (+) " + stats.ability[i] + "<br>"
            }
        }
        stemp.querySelector("#template-feature").innerHTML = ab
        document.querySelector('#features').appendChild(stemp);


        for (var i in response) {
            var temp = document.getElementById("builder-template").content.cloneNode(true);
            temp.querySelector("#template-legend").innerHTML = response[i]['name'];
            temp.querySelector("#template-feature").innerHTML = response[i]['entries'][0];
            document.querySelector('#features').appendChild(temp);
        };
        if (Object.keys(stats['subraces']).length > 1) {
            var temp = document.getElementById("builder-template").content.cloneNode(true);
            temp.querySelector("#template-legend").innerHTML = "Available subraces";
            var sr = "";
            for (i in stats.subraces) {
                sr = sr + i + "<br>"
            }
            temp.querySelector("#template-feature").innerHTML = sr;
            document.querySelector('#features').appendChild(temp);
        };
};


function load_page(name) {
    const request = new XMLHttpRequest();
    request.open('GET', infolink+`${name}`);
    request.onload = () => {
        const response = (JSON.parse(request.responseText)).entries;
        const stats = (JSON.parse(request.responseText));
        if (response[0]['type'] == "inset") {
            var ftemp = document.getElementById("builder-template").content.cloneNode(true);
            ftemp.querySelector("#template-legend").innerHTML = "Choose 1 from the list:"
            var entries = response[0]['entries']
            for (var i in entries) {
                var temp = document.getElementById("builder-template").content.cloneNode(true);
                temp.querySelector("#template-legend").innerHTML = entries[i]['name'];
                temp.querySelector("#template-feature").innerHTML = entries[i]['entries'][0];
                ftemp.querySelector('#template-feature').appendChild(temp);
            };
            document.querySelector('#features').appendChild(ftemp);
        }
        else {
            fill_content(stats, response)
        };
    };
    request.send();
};

