let selectedAttacker = null;
let selectedDefender = null;

// Fetch data from Flask route
function loadGameState() {
  fetch("/game_state")
    .then((response) => response.json())
    .then((data) => {
      renderBoard(data);
    });
}

// Create country cards
function renderBoard(gameState) {
  const board = document.getElementById("board");
  board.innerHTML = ""; // Clear any previous information

  gameState.country_list.forEach((country) => {
    const card = document.createElement("div");
    card.className = "country-card " + country.owner;

    card.innerHTML = `
            <h3>${country.name}</h3>
            <p>Owner: ${country.owner}</p>
            <p>Soldiers: ${country.soldiers}</p>
            <p>Population: ${country.population} Million</p>
        `;

    card.addEventListener("click", () => {
      selectCountry(country);
    });

    board.appendChild(card);
  });
}

function selectCountry(country) {
  if (country.owner === "player") {
    selectedAttacker = country.name;
    document.getElementById("selected-attacker").textContent = selectedAttacker;
  } else if (country.owner === "npc") {
    selectedDefender = country.name;
    document.getElementById("selected-defender").textContent = selectedDefender;
  }
}

// Run upon loading page
loadGameState();
