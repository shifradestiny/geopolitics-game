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

    board.appendChild(card);
  });
}

// Run upon loading page
loadGameState();
