import uuid
import random
from collections import namedtuple

class DomemoEngine(object):
    activeGames = []

    def listActiveGames(self):
        return self.activeGames

    def createGame(self):
        gameID = uuid.uuid4()
        self.activeGames.append(DomemoGame(gameID, self))
        return gameID

    def getGameByID(self, gameID):
        for game in self.activeGames:
            if game.gameID == gameID:
                return game
        raise IndexError("no active game matching id {}".format(gameID))

class DomemoGame(object):
    gameSetup = namedtuple("gameSetup", "playerTiles,hiddenTiles,publicTiles")

    def __init__(self, gameID, engine):
        self.moveCount = 0
        self.moveLog = []
        self.engine = engine
        self.gameID = gameID
        self.state = 'open'
        self.players = []
        self.activePlayerID = None
        self.tileSet = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7]
        random.shuffle(self.tileSet)
        self.hiddenTiles = []
        self.publicTiles = []
        self.setupByPlayerCount = {
            2: self.gameSetup._make([7, 7, 7]),
            3: self.gameSetup._make([7, 7, 0]),
            4: self.gameSetup._make([5, 4, 4]),
            5: self.gameSetup._make([4, 4, 4])
        }

    def addPlayer(self, PlayerName, PlayerID=None):
        if not self.state == 'open':
            return None
        if PlayerID is None:
            PlayerID = uuid.uuid4()
        self.players.append(DomemoPlayer(PlayerID, PlayerName, self))
        if len(self.players) == 5:
            self.state == 'full'
        return PlayerID

    def startGame(self):
        self.state = 'playing'
        random.shuffle(self.players)
        self.activePlayerID = self.players[0].playerID
        setup = self.setupByPlayerCount[len(self.players)]
        for player in self.players:
            player.addTiles(self.tileSet[0:setup.playerTiles])
            self.tileSet = self.tileSet[setup.playerTiles:]
        self.hiddenTiles.extend(self.tileSet[0:setup.hiddenTiles])
        self.tileSet = self.tileSet[setup.hiddenTiles:]
        self.publicTiles.extend(self.tileSet[0:setup.publicTiles])
        self.tileSet = self.tileSet[setup.publicTiles:]

    def getPlayerByID(self, playerID):
        for player in self.players:
            if player.playerID == playerID:
                return player
        raise IndexError("no active player matching id {}".format(playerID))

    def viewBoard(self, viewingPlayerID):
        viewableTiles = []
        for player in self.players:
            if not player.playerID == viewingPlayerID:
                viewableTiles.append((player.playerName, player.tiles))
        viewableTiles.append(("Public Tiles", self.publicTiles))
        viewableTiles.append(("Hidden Tiles", ['*']*len(self.hiddenTiles)))
        return viewableTiles

    def isActivePlayer(self, movingPlayer):
        if movingPlayer.playerID == self.activePlayerID:
            return True
        return False

    def advanceActivePlayer(self):
        idx = self.moveCount % len(self.players)
        self.activePlayerID = self.players[idx].playerID

    def makeSingleMove(self, movingPlayer, play):
        if not self.isActivePlayer(movingPlayer):
            raise IOError("it isn't your turn")
        if play in movingPlayer.tiles:
            self.publicTiles.append(movingPlayer.tiles.pop(movingPlayer.tiles.index(play)))
            print "correct!"
        self.moveCount += 1
        self.advanceActivePlayer()

class DomemoPlayer(object):
    def __init__(self, PlayerID, PlayerName, game):
        self.game = game
        self.playerID = PlayerID
        self.playerName = PlayerName
        self.tiles = []

    def addTiles(self, tileList):
        self.tiles.extend(tileList)

    def viewTiles(self):
        return self.game.viewBoard(self.playerID)

    def guess(self, value):
        self.game.makeSingleMove(self, value)

engine = DomemoEngine()
gameID = engine.createGame()
game = engine.getGameByID(gameID)
mikaelID = game.addPlayer("Mikael")
AIID = game.addPlayer("AI")
# momID = game.addPlayer("Mom")
# jonathanID = game.addPlayer("Jonathan")
# scottID = game.addPlayer("Scott")
game.startGame()

# print game.getPlayerByID(mikaelID).tiles
# print game.getPlayerByID(erikaID).tiles
# print game.getPlayerByID(momID).tiles
# print game.getPlayerByID(jonathanID).tiles
# print game.getPlayerByID(scottID).tiles

# print game.getPlayerByID(mikaelID).viewTiles()