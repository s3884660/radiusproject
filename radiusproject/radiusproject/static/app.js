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
  x.innerHTML = "Latitude: " + latitude + 
  "<br>Longitude: " + longitude;
}
