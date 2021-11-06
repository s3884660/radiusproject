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
  //just for debug
  x.innerHTML = "Latitude: " + latitude + 
  "<br>Longitude: " + longitude;
  //updates location of map to current user's location (if permission granted)
  map.flyTo({
    center: [longitude, latitude],
    essential: true
  });
}

function signUp() {
window.location.href = "/signup"
}

function createActivity() {
  window.location.href = "/activity/create"
}

