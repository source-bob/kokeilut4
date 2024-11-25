let map;
let currentRouteLayer;

function initializeMap() {
    if (map) {
        map.remove();
    }

    map = L.map('map').setView([60.1699, 24.9384], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
}

initializeMap();

const schoolLocation = [60.1863, 24.8293];
L.marker(schoolLocation).addTo(map).bindPopup("Karaportti 2").openPopup();

document.getElementById('routeForm').addEventListener('submit', async function (event) {
    event.preventDefault(); 

    const address = document.getElementById('address').value;

    const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${address}`);
    const data = await response.json();

    initializeMap();

    L.marker(schoolLocation).addTo(map).bindPopup("Karaportti 2").openPopup();

    if (data.length > 0) {
        const userLocation = [data[0].lat, data[0].lon];
        L.marker(userLocation).addTo(map).bindPopup("Your Location").openPopup();

        const osrmResponse = await fetch(`https://router.project-osrm.org/route/v1/driving/${userLocation[1]},${userLocation[0]};${schoolLocation[1]},${schoolLocation[0]}?overview=false`);
        const osrmData = await osrmResponse.json();

        if (osrmData.routes && osrmData.routes.length > 0) {
            const duration = osrmData.routes[0].duration;
            const startTime = new Date().toLocaleTimeString();
            const endTime = new Date(new Date().getTime() + duration * 1000).toLocaleTimeString();

            document.getElementById('routeDetails').innerHTML = `
                <p>Start time: ${startTime}</p>
                <p>End time: ${endTime}</p>
            `;
        } else {
            alert('Route not found. Please try again.');
        }

        currentRouteLayer = L.Routing.control({
            waypoints: [
                L.latLng(userLocation),
                L.latLng(schoolLocation)
            ],
            routeWhileDragging: true,
            collapsible: true,
            show: false,
            collapsed: true,
        }).addTo(map);

    } else {
        alert('Address not found. Please try again.');
    }
});
