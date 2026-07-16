// Nagpur city center coordinates — must match backend/app/config.py
const NAGPUR_CENTER = [21.1458, 79.0882];
const DEFAULT_ZOOM = 12;

// Initialize the map inside the <div id="map"> element
const map = L.map('map').setView(NAGPUR_CENTER, DEFAULT_ZOOM);

// Add the actual visual map tiles from OpenStreetMap (100% free, no API key)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
