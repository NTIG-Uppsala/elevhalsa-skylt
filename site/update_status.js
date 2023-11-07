$('.carousel').carousel({
    pause: "false"
});

let names = document.getElementsByClassName('name');
let status = document.getElementsByClassName('status');
let latestChanges = document.getElementsByClassName('latestChange');
moment.locale('sv');

// Stops carousel from pausing on mousehover
function updateDisplayedInfo(names, status, latestChanges) {
    $.getJSON('https://narvaro.ntig.net/api/get/users', function (data) {
        for (let i = 0; i < data.length; i++) {
            for (let x = 0; x < names.length; x++) {
                if (data[i].name == names[x].innerHTML) {
                    // Hide elements if status was updated more than 24 hours ago
                    let showTimeSinceChange = moment(data[i].latest_change).isAfter(moment().subtract(24, "hours"))
                    let visibility = showTimeSinceChange ? "visible" : "hidden";
                    latestChanges[x].style.visibility = visibility;
                    status[x].style.visibility = visibility;

                    latestChanges[x].innerHTML = 'Uppdaterad ' + moment(data[i].latest_change).fromNow();
                    if (data[i].status == true) {
                        status[x].innerHTML = 'Tillgänglig';
                        status[x].style.color = "#52FF42"
                    } else {
                        status[x].innerHTML = 'Inte tillgänglig'
                        status[x].style.color = "red"
                    }
                }
            }
        }
    });
}

updateDisplayedInfo(names, status, latestChanges);
setInterval(() => {
    updateDisplayedInfo(names, status, latestChanges);
}, 60000);