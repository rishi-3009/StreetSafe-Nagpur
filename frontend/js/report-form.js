// --- Report Form Logic ---
// Handles: entering "pick a location" mode, capturing the clicked point,
// opening the report modal, and (for now) logging the submitted report.
// Phase 3 will replace the console.log below with a real POST request
// to the FastAPI backend, so the report is actually saved to the database.

const reportBtn = document.getElementById('reportBtn');
const pickBanner = document.getElementById('pickLocationBanner');
const cancelPickBtn = document.getElementById('cancelPick');
const reportForm = document.getElementById('reportForm');
const categoryInput = document.getElementById('category');
const timeInput = document.getElementById('incidentTime');
const selectedCoordsText = document.getElementById('selectedCoords');

const reportModalEl = document.getElementById('reportModal');
const reportModal = new bootstrap.Modal(reportModalEl);

let isPicking = false;
let selectedLatLng = null;

// Marker color per category — used for the pin dropped after submission
const CATEGORY_COLORS = {
  'Harassment': '#FF0000',    // bright red
  'Poor Lighting': '#FFD700', // yellow
  'Accident': '#FF8C00',      // orange
  'Crime': '#000000'          // black
};

// Build the legend dynamically from CATEGORY_COLORS,
// so it always stays in sync if colors change later.
function buildLegend() {
  const legendEl = document.getElementById('mapLegend');
  let html = '<h6>Legend</h6>';
  for (const [category, color] of Object.entries(CATEGORY_COLORS)) {
    html += `
      <div class="legend-item">
        <span class="legend-dot" style="background:${color};"></span>
        <span>${category}</span>
      </div>`;
  }
  legendEl.innerHTML = html;
}
buildLegend();

// Formats the current local date/time into the exact string format
// the datetime-local input expects: "YYYY-MM-DDTHH:mm"
function getLocalDateTimeString() {
  const now = new Date();
  const tzOffsetMs = now.getTimezoneOffset() * 60000;
  return new Date(now.getTime() - tzOffsetMs).toISOString().slice(0, 16);
}

// Step 1: user clicks the floating "+" button to start reporting
reportBtn.addEventListener('click', () => {
  isPicking = true;
  reportBtn.classList.add('d-none');
  pickBanner.classList.remove('d-none');
});

// User cancels picking a location
cancelPickBtn.addEventListener('click', () => {
  isPicking = false;
  pickBanner.classList.add('d-none');
  reportBtn.classList.remove('d-none');
});

// Step 2: user clicks on the map to drop a pin
map.on('click', (e) => {
  if (!isPicking) return;

  selectedLatLng = e.latlng;
  isPicking = false;
  pickBanner.classList.add('d-none');
  reportBtn.classList.remove('d-none');

  selectedCoordsText.textContent =
    `Lat: ${selectedLatLng.lat.toFixed(5)}, Lng: ${selectedLatLng.lng.toFixed(5)}`;

  // Pre-fill with "now" so the field is already valid — user can still edit it
  timeInput.value = getLocalDateTimeString();

  reportModal.show();
});

// Step 3: user fills the form and submits
reportForm.addEventListener('submit', (e) => {
  e.preventDefault();

  if (!selectedLatLng) return;

  const report = {
    category: categoryInput.value,
    incident_time: timeInput.value,
    latitude: selectedLatLng.lat,
    longitude: selectedLatLng.lng,
    reported_at: new Date().toISOString()
  };

  // Phase 3 will replace this with a real POST request to the backend API.
  console.log('New report (not yet saved to a server):', report);

  // Drop a colored marker immediately so the user gets visual feedback
  const color = CATEGORY_COLORS[report.category] || '#6c757d';
  L.circleMarker([report.latitude, report.longitude], {
    radius: 8,
    color: '#000',
    weight: 1,
    fillColor: color,
    fillOpacity: 0.9
  })
    .addTo(map)
    .bindPopup(`<b>${report.category}</b><br>${new Date(report.incident_time).toLocaleString()}`);

  // Reset everything for the next report
  reportForm.reset();
  selectedLatLng = null;
  reportModal.hide();
});
