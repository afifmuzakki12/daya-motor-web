const validate = (el) => {
  const checkboxes = el.querySelectorAll('input[type="checkbox"]');
  return [...checkboxes].some((e) => e.checked);
};

const formEl = document.querySelector("form");
const statusEl = formEl.querySelector(".status-message");
const checkboxGroupEl = formEl.querySelector(".checkbox-group-required");

checkboxGroupEl.addEventListener("click", (e) => {
  statusEl.textContent = validate(checkboxGroupEl) ? "valid" : "invalid";
});

formEl.addEventListener("submit", (e) => {
  e.preventDefault();

  if (validate(checkboxGroupEl)) {
    statusEl.textContent = "Form submitted!";
    // Send data from e.target to your backend
  } else {
    // statusEl.textContent = "Error: select at least one checkbox";
    alert("Select one of checkbox");
  }
});
