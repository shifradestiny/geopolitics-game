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

function attackCountry() {
  const battleLog = document.getElementById("battle-log");

  // Ensure attacker and defender are selected
  if (!selectedAttacker || !selectedDefender) {
    battleLog.innerHTML =
      "<p>Please select both an attacker and a defender.</p>";
    return;
  }

  // Send POST request
  fetch("/attack", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      attacker: selectedAttacker,
      defender: selectedDefender,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      const result = data.battle_outcome;

      if (result.error) {
        battleLog.innerHTML = `<p>${result.error}</p>`;
      } else {
        battleLog.innerHTML = `
        <p>Attacker Rolls: ${result.attacker_dice}</p>
        <p>Defender Rolls: ${result.defender_dice}</p>
        <p>Attacker Loss: ${result.attacker_loss}</p>
        <p>Defender Loss: ${result.defender_loss}</p>
        <p>Captured: ${result.captured}</p>
        `;
      }

      // Update the game state
      renderBoard(data.game_state);
    });
}

document.getElementById("attack-btn").addEventListener("click", attackCountry);

function resetGame() {
  fetch("/reset", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => {
      selectedAttacker = null;
      selectedDefender = null;

      document.getElementById("selected-attacker").textContent = "None";
      document.getElementById("selected-defender").textContent = "None";

      document.getElementById("battle-log").innerHTML = "";

      // Update the game state
      renderBoard(data.game_state);
    });
}

document.getElementById("reset-btn").addEventListener("click", resetGame);

function endTurn() {
  fetch("/npc_turn", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => {
      const npc = data.npc_outcome;
      const battleLog = document.getElementById("battle-log");

      if (!npc || npc.error) {
        battleLog.innerHTML = "<p>NPC could not make a move.</p>";
      } else {
        const result = npc.battle_result;
        battleLog.innerHTML = `
        <p><strong>NPC Turn: ${npc.npc_attacker} attacked ${npc.player_defender}</strong></p>
        <p>NPC Attacker: ${npc.npc_attacker}</p>
        <p>Player Defender: ${npc.player_defender}</p>
        <p>NPC Rolls: ${result.attacker_dice}</p>
        <p>Player Rolls: ${result.defender_dice}</p>
        <p>Captured: ${result.captured}</p>
        `;
      }
    });

  renderBoard(data.game_state);
}

document.getElementById("end-turn-btn").addEventListener("click", endTurn);

// Run upon loading page
loadGameState();
