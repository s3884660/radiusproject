var latitude;
var longitude;
var x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  }
}

function showPosition(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;

  //updates location of map to current user's location (if permission granted)
  map.flyTo({
    center: [longitude, latitude],
    essential: true
  });
}

function addMarkers(coordinates,title,tags,address,url) {
  const el = document.createElement('div');
  el.className = 'marker';

  new mapboxgl.Marker(el)
  .setLngLat(coordinates)
  .setPopup(
    new mapboxgl.Popup({ offset: 25 }) // add popups
      .setHTML(
        "<h3>"+title+"</h3><p>Tags: "+tags+"<br>Address: "+address+" <br><button onclick='window.location.href=\"/activities/"+url+"\"' class='popup_button'>View</button></p>"
      )
  )
  .addTo(map);
}

function signUp() {
window.location.href = "/signup"
}

function createActivity() {
  window.location.href = "/activity/create"
}

