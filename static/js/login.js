const form = document.querySelector("form");
const errorLabel = document.querySelector(".error");

async function onLogin() {
  const object = parseForm(form);
  const response = await fetch(`http://127.0.0.1:5000/api/users/login`, {
    method: "POST",
    mode: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      ...object,
      email: "string",
      status: 0,
      user_id: "string",
    }),
  });
  const json = await response.json();
  if (json) {
    localStorage.setItem("auth", json);
    return redirectTo("/homepage");
  }
  errorLabel.innerHTML = "Usuário ou senha não existem. Tente novamente!";
}

function onLoad() {
  if (localStorage.getItem("auth")) return redirectTo("/homepage");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    onLogin();
  });
}

onLoad();
