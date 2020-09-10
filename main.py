import player
import math

players = []
playerCount = 0

def confirmPositiveInt(message):
    output = None
    while type(output) != int or output < 0:
        try:
            output = int(input(message))
        except:
            print("Invalid value.")
    return output
        

def calculateMedals(stat):
    valueList = []
    for i in players:
        valueList.append(i.stats[stat])
    valueList = sorted(valueList, reverse=True)
    for i in players:
        if i.stats[stat] == valueList[2]:
            i.medals[stat] = "Bronze"
        if i.stats[stat] == valueList[1]:
            i.medals[stat] = "Silver"
        if i.stats[stat] == valueList[0]:
            i.medals[stat] = "Gold"


while playerCount < 1 or playerCount > 6:
    try:
        playerCount = int(input("Number of players: "))
        if not (playerCount >= 1 and playerCount <= 6):
            print("Invalid number of players.") 
    except ValueError:
        print("Enter a valid number.")
        playerCount = 0
    


for i in range(playerCount):
    players.append(player.Player(input("Name: "), i))
    players[i].stats["damage"] = confirmPositiveInt("How much damage has " + players[i].name + " dealt? ")
    players[i].stats["eliminations"] = confirmPositiveInt("How many kills has " + players[i].name + " gotten? ")
    players[i].stats["healing"] = confirmPositiveInt("How much healing has " + players[i].name + " given? ")
    players[i].stats["objTime"] = confirmPositiveInt("How much objective time does " + players[i].name + " have? ")
    players[i].stats["objKills"] = confirmPositiveInt("How many objective kills has " + players[i].name + " gotten? ")
    players[i].stats["deaths"] = confirmPositiveInt("How many times has " + players[i].name + " died? ")

calculateMedals("damage")
calculateMedals("eliminations")
calculateMedals("healing")
calculateMedals("objTime")
calculateMedals("objKills")

calculateMedals("deaths")

for i in players:
    print(i.medals)