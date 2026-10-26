class Country:
    def __init__(self, name, population, owner):
        self.name = name
        self.population = population
        self.owner = owner
        self.base_soldier_value = self.initial_soldiers()
        self.soldiers = self.base_soldier_value

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

    def to_dict(self):
        return {
            "name": self.name,
            "population": self.population,
            "owner": self.owner,
            "base_soldier_value": self.base_soldier_value,
            "soldiers": self.soldiers
        }

