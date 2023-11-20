
function sortDates(date_from_parameter) {
    Papa.parse("./assets/event_data.csv", {
        download: true,
        header: true,
        complete: function (results) {
            const timeZone = 'Europe/Stockholm'; // Change this to your actual time zone

            const dates = results.data.map(function (row) {
                const dateStr = row['DATUM'];
                const dateObj = new Date(dateStr + 'T24:00:00');
                return dateObj;
            });

            const sortedDates = dates.sort(function (a, b) {
                return a - b;
            });

            // If date_from_parameter is provided, use it; otherwise, use today's date
            date_from_parameter = date_from_parameter ? new Date(date_from_parameter) : new Date();
            date_from_parameter.setHours(0, 0, 0, 0);


            const upcomingDates = sortedDates.filter(function (date) {
                const dateOptions = { timeZone, year: 'numeric', month: '2-digit', day: '2-digit' };
                const formattedDate = date.toLocaleDateString('sv-SE', dateOptions);
                const formatteddate_from_parameter = date_from_parameter.toLocaleDateString('sv-SE', dateOptions);
                return formattedDate >= formatteddate_from_parameter;
            });

            if (upcomingDates.length > 0) {
                const sortedDate = upcomingDates[0].toISOString().split('T')[0];
                let date_parse
                date_parse = new Date(sortedDate);
                let diffrence_in_time = date_parse.getTime() - date_from_parameter.getTime();
                let diffrence_in_days = diffrence_in_time / (1000 * 60 * 60 * 24);

                const day_limit = 14
                // Display the sortedDate on the HTML page
                if (Math.round(diffrence_in_days) < day_limit) {
                    document.getElementById('sortedDateContainer').innerText = 'Nästa händelse är: ' + sortedDate;
                } else {
                    const event_id = document.getElementById("event")
                    event_id.classList.add('hidden');
                }
            }
            console.log('Results:', results);
            console.log('Upcoming Dates:', upcomingDates);
        }
    });
}
sortDates();
// sortDates("2023-12-19");