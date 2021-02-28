//I got this idea from https://github.com/irinatu17/Art-of-Tea
//Initilizes the map from Google Maps API
//Load the place information into the HTML elements used by the info window.

function initMap() {
  const mapRef = document.getElementById('map');
  const contentRef = document.getElementById('info-window-content');
  const Location = { lat: 54.2766603, lng: -8.5018636 };
  const map = new google.maps.Map(mapRef, { zoom: 13, center: Location });
  const infowindow = new google.maps.InfoWindow({
    content: contentRef,
  });
  const marker = new google.maps.Marker({
    position: Location,
    map: map,
    title: 'PMP Training Center',
  });
  marker.addListener('click', () => {
    infowindow.open(map, marker);
  });
};