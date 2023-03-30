const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  onCreate();
});

async function onCreate() {
  const object = parseForm(form);
  const response = await fetch(`http://127.0.0.1:5000/api/users`, {
    method: "POST",
    mode: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      ...object,
      status: 0,
      user_id: "default",
    }),
  });
  const json = await response.json();
  if (json) return redirectTo("/login");
  errorLabel.innerHTML = "Erro ao cadastrar usuário. Tente novamente!";
}
