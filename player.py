class Player:

    # damage, elims, healing, deaths, objTime

    def __init__(self, name, index):
        self.name = name
        self.index = index
        
        self.stats = {
            "damage": 0,
            "eliminations": 0,
            "healing": 0,
            "objTime": 0,
            "objKills": 0,
            "deaths": 0
        }

        self.medals = {
            "damage": None,
            "eliminations": None,
            "healing": None,
            "objTime": None,
            "objKills": None,
            "deaths": None
        }