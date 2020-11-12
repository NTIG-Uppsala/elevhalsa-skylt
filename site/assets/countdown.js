---
---

"use strict";

var data = [
    {% for event in site.data.important_events %}
        {name: "{{event.HANDELSE}}", info: "{{event.INFO_TEXT}}", date: new Date("{{event.DATUM}}")}
        {% if forloop.last %}{% else %},{% endif %}
    {% endfor %}
];

var events_slide;
var events;

// Calculate number of days from start date to target date
function GetDayDiff(date, startDate) {
    var diff = new Date(date - startDate);

    return Math.floor(diff.getTime() / 24 / 60 / 60 / 1000);
}

function GetCountdownString(date, today) {
    var daysDiff = GetDayDiff(date, today);

    
    if (daysDiff == 0) {
        // TODO: Calculate time diff here if time is to be implemented

        return "Idag!";
    } else if (daysDiff == 1) {
        return "Imorgon!";
    } else if (daysDiff < 14) {
        return `${daysDiff} dagar kvar`;
    } else if (daysDiff <= 28) {
        var weeksDiff = Math.round(daysDiff / 7);

        return `${weeksDiff} veckor kvar`;
    } else {
        if (date.getYear() == today.getYear()) {
            return `${date.toLocaleString("sv-SE", {month: 'long', day: 'numeric'})}`;
        } else {
            return `${date.toLocaleString("sv-SE", {year: 'numeric', month: 'long', day: 'numeric'})}`;
        }
    }
}

function UpdateSlide(today) {

    // Sets time to 00:00:00 because only dates are provided for events
    // TODO: Remove these lines if time is to be implemented
    today.setSeconds(0);
    today.setMinutes(0);
    today.setHours(0);

    data = data.filter(function(a) {
        return a.date >= today && GetDayDiff(a.date, today) <= 28;
    });

    if (data.length > 0) {
        data.sort(function(a, b) {
            return a.date > b.date;
        });

        for (var index = 3; index >= 0; index--) {

            var num_countdown_boxes = $(".countdown-box").length;
            if (data.length <= index) {
                if (index < num_countdown_boxes) events.eq(index).detach();
            } else {
                $(".row", events_slide).prepend(events.eq(index));

                console.log(data[index]);
                
                $(".name > .event", events.eq(index)).text(data[index].name);
                $(".name > .timer", events.eq(index)).text(GetCountdownString(data[index].date, today));
                $("p", events.eq(index)).text(data[index].info);
            }
        }
        
    } else {
        events_slide.detach();
    }
}

function SetData(newData, date=new Date()) {
    data = newData;
    $(".carousel-inner").append(events_slide);
    console.log(data);
    UpdateSlide(date);
}

$(function() {
    events_slide = $(".carousel-item#events");
    events = $(".row", events_slide).children();

    UpdateSlide(new Date());
});
