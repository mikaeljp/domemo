#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
import engine

app = Flask(__name__)


gameEngine = engine.engine

@app.route('/domemo/list', methods=['GET'])
def domemo():
    return jsonify({'activeGames':[str(game.gameID) for game in gameEngine.activeGames]})


@app.route('/domemo/newgame', methods=['GET'])
def newGame():
    gameID = gameEngine.createGame()
    return jsonify({'newGameID':gameID})

if __name__ == '__main__':
    app.run()
