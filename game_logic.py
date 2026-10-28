import random
class Country:
    def __init__(self, name, population, owner):
        self.name = name
        self.population = population
        self.owner = owner
        self.base_soldier_value = self.initial_soldiers()
        self.soldiers = self.base_soldier_value

    # Assign soldiers based on population size
    def initial_soldiers(self):
        if self.population <= 5:
            return 1
        elif self.population <= 10:
            return 2
        elif self.population <= 25:
            return 3
        elif self.population <= 50:
            return 4
        elif self.population <= 75:
            return 5
        elif self.population <= 100:
            return 6
        elif self.population <= 125:
            return 7
        elif self.population <= 150:
            return 8
        else:
            return 9

    # Format values for JSON
    def to_dict(self):
        return {
            "name": self.name,
            "population": self.population,
            "owner": self.owner,
            "base_soldier_value": self.base_soldier_value,
            "soldiers": self.soldiers
        }

class Game:
    def __init__(self):
        self.countries = [
            Country("South Africa", 60, "npc"),
            Country("Chile", 20, "npc"),
            Country("Brazil", 215, "npc"),
            Country("Uganda", 53, "npc"),
            Country("Egypt", 110, "npc"),
            Country("Germany", 84, "npc"),
            Country("France", 68, "npc"),
            Country("India", 1400, "npc"),
            Country("New Zealand", 5, "npc"),
            Country("Japan", 125, "npc")
        ]

        # Choose random country to be the starting player
        starting_country = random.choice(self.countries)
        starting_country.owner = "player"

        self.game_over = False
        self.winner = None

    def battle(self, attacker, defender):
        attacker_dice = []
        for i in range(attacker.soldiers):
            attacker_dice.append(random.randint(1, 6))

        defender_dice = []
        for i in range(defender.soldiers):
            defender_dice.append(random.randint(1, 6))

        # Sort dice rolls in descending order for comparison
        attacker_dice.sort(reverse=True)
        defender_dice.sort(reverse=True)

        compare_rolls = min(len(attacker_dice), len(defender_dice))

        for i in range(compare_rolls):
            if attacker_dice[i] > defender_dice[i]:
                defender.soldiers -= 1
            else:
                attacker.soldiers -= 1

        captured = False

        # Handles when soldiers are captured on either side
        if defender.soldiers <= 0:
            captured = True
            defender.owner = attacker.owner  # Being captured shifts ownership
            defender.soldiers = defender.base_soldier_value
            attacker.soldiers += 1
        elif attacker.soldiers <= 0:
            captured = True
            attacker.owner = defender.owner  # Being captured shifts ownership
            attacker.soldiers = attacker.base_soldier_value
            defender.soldiers += 1
        else:
            captured = False

        # Checks for a winner after each battle
        self.verify_winner()

        # Format values for JSON
        return {
            "attacker_dice": attacker_dice,
            "defender_dice": defender_dice,
            "captured": captured
        }

    def verify_winner(self):
        player_count = 0
        npc_count = 0

        for country in self.countries:
            # Update the number of players/npc's after each battle
            if country.owner == "player":
                player_count += 1
            elif country.owner == "npc":
                npc_count += 1

        # End the game if either side is 10 or 0 and define a winner
        if player_count == 10 or npc_count == 0:
            self.game_over = True
            self.winner = "player"
        elif player_count == 0 or npc_count == 10:
            self.game_over = True
            self.winner = "npc"

    # Computers turn
    def npc_turn(self):
        if self.game_over == True:
            return None

        # Temp lists
        npc_countries = []
        player_countries = []

        for player_type in self.countries:
            if player_type.owner == "npc":
                npc_countries.append(player_type)
            elif player_type.owner == "player":
                player_countries.append(player_type)

        npc_attacker = random.choice(npc_countries)
        player_defender = random.choice(player_countries)

        self.battle(npc_attacker, player_defender)

        return {
            "npc_attacker": npc_attacker,
            "player_defender": player_defender
        }