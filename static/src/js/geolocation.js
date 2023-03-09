function findMyState() {
  const status = document.querySelector("#status");
  const userLat = document.querySelector("#user-lat");
  const userLong = document.querySelector("#user-long");

  const success = (position) => {
    console.log(position);
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    const geoApiUrl = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en`;

    fetch(geoApiUrl)
      .then((res) => res.json())
      .then((data) => {
        status.textContent = data.city;
        if (status.textContent == "") {
          status.textContent = "Can't Get Your Location";
        }
        userLat.textContent = data.latitude;
        userLong.textContent = data.longitude;
      });
  };

  const error = () => {
    status.textContent = "Unable to retrieve your location";
    userLat.textContent = "Unable to retrieve your location";
    userLong.textContent = "Unable to retrieve your location";
  };
  navigator.geolocation.getCurrentPosition(success, error);
}
