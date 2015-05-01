"""
AIHandler.py

View that handles the communication from
clientside to the AI.
"""
import json
import Tools
import AI
import logging

from Board import Board
from ViewHandler import Handler
from Tools import pieces

class AIHandler(Handler):
    """Checks local dictionary for word"""
    def get(self):
        try:
            stage = json.loads(self.request.get("stage"))
            aiChar = pieces["aiChar"]
            playerChar = pieces["playerChar"]
            board = Board(stage)

            logging.info("Stage: {}".format(stage))
            logging.info("AIChar: {}".format(aiChar))
            logging.info("Player Char: {}".format(playerChar))
            logging.info("Turn count {}".format(len(board)))
            logging.info("Game Board:\n"+str(board))

            over,winner = board.gameOver()
            output = {"over":over,
                      "winner":winner,
                      "aiMove":-1,}
            if not over:
                aiMove = AI.takeTurn(board, aiChar, playerChar)
                board.makeMove(*(list(aiMove)+[aiChar]))
                logging.info("\n"+str(board))
                output["over"], output["winner"] = board.gameOver()
                output["aiMove"] = ((aiMove[0]*3)+aiMove[1])

            if output["over"]:
                AI.reshuffle()

            self.write(json.dumps(output))
        except:
            self.render("bad.html")
