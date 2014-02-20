import engine
import random

g = engine.game

class NaiveAI(object):
    def __init__(self):
        self.possibleTiles == [1,2,3,4,5,6,7]

    def move(self):
        return self.possibleTiles[random.randint(0, len(self.possibleTiles))]

while True:
    activePlayer = g.getPlayerByID(g.activePlayerID)
    if activePlayer.playerName == "AI":
        pass
    print "-----"
    print "your move, {}!".format(activePlayer.playerName)
    print "you can see these tiles:"
    for area in activePlayer.viewTiles():
        print area
    move = raw_input("what's your guess?")
    activePlayer.guess(int(move))
