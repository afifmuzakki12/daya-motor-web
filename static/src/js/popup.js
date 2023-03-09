var modal = document.getElementById("myModal");

function popupFunction() {
  modal.style.display = "block";
  return false;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-popup")[0];
// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
  // location.reload();
  document.getElementById("form_submit_form").submit();
};
