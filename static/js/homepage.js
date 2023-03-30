const logout = document.querySelector(".logout");
const dropOpen = document.querySelector(".drop");
const dropmenu = document.querySelector(".drop-menu");
const dropClose = document.querySelector(".drop-menu .close");
const eventsDiv = document.querySelector(".events");
const createEvent = document.querySelector(".button.change-visualization");

async function deleteEvent(event) {
  const { id } = event.target.dataset;
  const auth = localStorage.getItem("auth");

  const response = await fetch(
    `http://127.0.0.1:5000/api/users/${auth}/events/${id}`,
    {
      method: "DELETE",
      mode: "same-origin",
    }
  );
  redirectTo("/homepage");
}

function addDeleteEvent() {
  document.querySelectorAll(".delete-event").forEach((component) => {
    component.addEventListener("click", deleteEvent);
  });
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

async function fetchEvents() {
  const auth = localStorage.getItem("auth");
  const response = await fetch(
    `http://127.0.0.1:5000/api/users/${auth}/events`
  );
  const events = await response.json();
  if (events.length === 0) {
    eventsDiv.innerHTML = "Sem eventos cadastrados";
    return;
  }
  for (let event of events) {
    eventsDiv.innerHTML += `
    <li class="event">
      <label class="event-name">${event.title} em ${
      event.datetime.split("T")[0]
    }</label>
      <label class="event-description">${event.description}</label>
      <button data-id="${event.id}" class="button primary delete-event">
          Deletar
      </button>
    </li>
  `;
  }
  addDeleteEvent();
}

function onCreateEvent() {
  redirectTo("/create-event");
}

function main() {
  logout.addEventListener("click", onLogout);
  dropOpen.addEventListener("click", toggleMenu);
  dropClose.addEventListener("click", toggleMenu);
  createEvent.addEventListener("click", onCreateEvent);
  fetchEvents();
}

main();
