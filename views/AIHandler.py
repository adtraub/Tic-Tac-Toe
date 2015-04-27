"""
AIHandler.py

View that handles the communication from
clientside to the AI.
"""
import json
import Tools
import StaticAI
import logging
from Board import Board
from ViewHandler import Handler

class AIHandler(Handler):
    """Checks local dictionary for word"""
    def get(self):
        stage = json.loads(self.request.get("stage"))
        char = self.request.get("aiChar")
        opponentChar = self.request.get("playerChar")

        logging.info("Stage: {}".format(stage))
        logging.info("Stage type: {}".format(type(stage)))
        logging.info("AIchar: {}".format(char))
        logging.info("Player Char: {}".format(opponentChar))
        logging.info("Player In Middle: {}".format(opponentChar == stage[4]))

        board = Board(stage)
        logging.info("\n"+str(board))

        over,winner = board.gameOver()
        output = {"over":over,
                  "winner":winner,
                  "aiMove":-1,}
        if not over:
            aiMove = StaticAI.takeTurn(board, char, opponentChar)
            board.makeMove(*(list(aiMove)+[char]))
            logging.info("\n"+str(board))
            output["over"], output["winner"] = board.gameOver()

            if not output["over"]:
                output["aiMove"] = ((aiMove[0]*3)+aiMove[1])

        self.write(json.dumps(output))
