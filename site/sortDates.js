export function sortDates(date_from_parameter, numEvents, path) {
    // Default values if parameters are not provided
    path = path || "./assets/stored_event_data.csv";
    numEvents = numEvents || 1;

    Papa.parse(path, {
        download: true,
        header: true,
        complete: function (results) {
            const timeZone = 'Europe/Stockholm'; // Change this to your actual time zone

            const events = results.data.map(function (row) {
                const dateStr = row['DATUM'];
                const dateObj = new Date(dateStr + 'T24:00:00');
                const event = {
                    date: dateObj,
                    title: row['HANDELSE'],
                    description: row['BESKRIVNING']
                };
                return event;
            });



            const sortedEvents = events.sort(function (a, b) {
                return a.date.getTime() - b.date.getTime();
            });

            // If date_from_parameter is provided, use it; otherwise, use today's date
            date_from_parameter = date_from_parameter ? new Date(date_from_parameter) : new Date();
            date_from_parameter.setHours(0, 0, 0, 0);

            const upcomingEvents = sortedEvents.filter(function (event) {
                const dateOptions = { timeZone, year: 'numeric', month: '2-digit', day: '2-digit' };
                const formattedDate = event.date.toLocaleDateString('sv-SE', dateOptions);
                const formatteddate_from_parameter = date_from_parameter.toLocaleDateString('sv-SE', dateOptions);
                return formattedDate >= formatteddate_from_parameter;
            });

            // Display the top numEvents upcoming events
            for (let i = 0; i < numEvents && i < upcomingEvents.length; i++) {
                const currentEvent = upcomingEvents[i];
                const sortedDate = currentEvent.date.toISOString().split('T')[0];
                let date_parse = new Date(sortedDate);
                let difference_in_time = date_parse.getTime() - date_from_parameter.getTime();
                let difference_in_days = Math.round(difference_in_time / (1000 * 60 * 60 * 24));

                const day_limit = 14;

                // Check if the element with ID 'sortedDateContainer' exists
                const eventDescription = document.getElementById("eventDescription");
                const sortedDateContainer = document.getElementById(`sortedDateContainer${i + 1}`);
                if (sortedDateContainer) {
                    // Display the event information with countdown on the HTML page
                    if (difference_in_days < day_limit) {
                        sortedDateContainer.innerHTML = `<strong>${currentEvent.title} <br></strong>${sortedDate} (om  ${difference_in_days} dagar)`;
                        eventDescription.innerHTML = `${currentEvent.description}`;

                        // Ensure that the 'event' element is visible
                        const event_id = document.getElementById(`event${i + 1}`);
                        event_id.classList.add('item');
                        event_id.classList.remove('hidden');
                    } else {
                        // Hide the 'event' element
                        const event_id = document.getElementById(`event${i + 1}`);
                        event_id.classList.remove('item');
                        event_id.classList.add('hidden');
                    }
                } else {
                    console.error(`Element with ID 'sortedDateContainer${i + 1}' not found!`);
                }
            }

            console.log('Results:', results);
            console.log('Upcoming Events:', upcomingEvents);
        }
    });
}


// sortDates();
// sortDates("2023-12-19", 1);
