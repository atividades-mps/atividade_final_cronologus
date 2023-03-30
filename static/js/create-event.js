const back = document.querySelector(".button.back");
const logout = document.querySelector(".logout");
const dropOpen = document.querySelector(".drop");
const dropmenu = document.querySelector(".drop-menu");
const dropClose = document.querySelector(".drop-menu .close");
const form = document.querySelector("form");

function onBack() {
  redirectTo("/homepage");
}

async function onLogout() {
  const auth = localStorage.getItem("auth");
  const response = await fetch(
    `http://127.0.0.1:5000/api/users/${auth}/logout`,
    {
      method: "POST",
      mode: "same-origin",
    }
  );

  const json = await response.json();
  if (json) {
    localStorage.removeItem("auth");
    return redirectTo("/login");
  }
  alert("Ocorreu um erro. Por favor tente novamente!");
}

function toggleMenu() {
  dropmenu.classList.toggle("hide");
}

async function onSubmit() {
  const auth = localStorage.getItem("auth");
  const object = parseForm(form);
  const response = await fetch(
    `http://127.0.0.1:5000/api/users/${auth}/events`,
    {
      method: "POST",
      mode: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...object,
        event_id: "string",
        status: 0,
        user_id: "string",
      }),
    }
  );
  const json = await response.json();
  if (json) return redirectTo("/homepage");
}

function main() {
  logout.addEventListener("click", onLogout);
  dropOpen.addEventListener("click", toggleMenu);
  dropClose.addEventListener("click", toggleMenu);
  back.addEventListener("click", onBack);
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    onSubmit();
  });
}

main();
