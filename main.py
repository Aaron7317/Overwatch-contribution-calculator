import player
import math

players = []
playerCount = 0

def calculateMedals():
    pass


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
    players[i].stats["damage"] = input("How much damage has " + players[i].name + " dealt? ")
    players[i].stats["eliminations"] = input("How many kills has " + players[i].name + " gotten? ")
    players[i].stats["healing"] = input("How much healing has " + players[i].name + " given? ")
    players[i].stats["objTime"] = input("How much objective time does " + players[i].name + " have? ")
    players[i].stats["objKills"] = input("How many objective kills has " + players[i].name + " gotten? ")
    players[i].stats["deaths"] = input("How many times has " + players[i].name + " died? ")
    print(players[i].stats)