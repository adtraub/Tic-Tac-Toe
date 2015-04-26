"""
Adam Traub
Tic-Tac-Toe AI
4/25/2015
"""
import random


class AI:
    """Unbeatable AI for Tic Tac Toe

        Args:
          board (Board): The board currently in play
          character (str): The character the AI places on the board
          opponentChar (str): The opponent's TTT character
          spotsTaken (int): keeps track of the number of moves made.

        Attributes:
          board (Board): The board currently in play
          character (str): The character the AI places on the board
          opponentChar (str): The opponent's TTT character
          corners (dict): contains a reference to all the corners
          sides (dict): contains a reference to all the sides
          randomSides (list): values from sides in random order
          randomCorners (list): values from corners in random order          
     """
    def __init__(self, board, character="O", opponentChar="X", easyMode=False):
        self.board = board
        self.character = character
        self.opponentChar = opponentChar
        self.easyMode = easyMode
        self.corners = {
                "tl":(0,0,),
                "tr":(0,2,),
                "bl":(2,0,),
                "br":(2,2,),
                }
        self.sides = {
                "tm":(0,1,),
                "ml":(1,0,),
                "mr":(1,2,),
                "bm":(2,1,),
            }
        self.randomSides = self.sides.values() 
        self.randomCorners = self.corners.values()

        #helps make behavior less predictable
        random.shuffle(self.randomSides)
        random.shuffle(self.randomCorners)

    def reset(self, board, character="O", opponentChar="X"):
        """resets the AI allowing it to play multiple games

            Args:
              board (Board): The board currently in play
              character (str): The character the AI places on the board
              opponentChar (str): The opponent's TTT character
              spotsTaken (int): keeps track of the number of moves made.

            Attributes:
              board (Board): The board currently in play
              character (str): The character the AI places on the board
              opponentChar (str): The opponent's TTT character        
         """
        self.board = board
        self.character = character
        self.opponentChar = opponentChar
        random.shuffle(self.randomSides)
        random.shuffle(self.randomCorners)
        

    def findBestSpot(self):
        """Finds the best spot for the next move

            Notes:
              This is the meat of the AI.  This large function
              follows the unbeatable TTT strategy on wikipedia
              to find the best available spot. it uses 2
              sub-methods in order to reduce a plethora of
              repeated code.

            Returns:
              coords (tuple)     
         """
        #These are just some shorter names to clean the code
        board = self.board
        stage = board.stage
        default = board.default
        char = self.character
        def couldEnd(who):            
            """Check if the game could end in the next move

                Notes:
                  Sub-Method of findBestSpot
                  by making the character in question a parameter,
                  this method works equally well for finding winning
                  combinations for the AI and the opponent.

                Arguments:
                  who (str) character that might achieve the win

                Returns:
                  coords (tuple) coordinates of winning spot or None     
             """
            for i in range(3):
                #Check for Horizontal win
                if (stage[i][0] == stage[i][1] == who) and (stage[i][2] == default):
                    return i,2
                if (stage[i][1] == stage[i][2] == who) and (stage[i][0] == default):
                    return i,0
                if (stage[i][2] == stage[i][0] == who) and (stage[i][1] == default):
                    return i,1

                #Check for vertical win
                if (stage[0][i] == stage[1][i] == who) and (stage[2][i] == default):
                    return 2,i
                if (stage[1][i] == stage[2][i] == who) and (stage[0][i] == default):
                    return 0,i
                if (stage[2][i] == stage[0][i] == who) and (stage[2][i] == default):
                    return 1,i

                #This stuff could be trimmed down with a loop but would yield no extra clarity or speed
                
                #check Diagonals \
                if (stage[0][0] == stage[1][1] == who) and (stage[2][2] == default):
                    return 2,2
                if (stage[1][1] == stage[2][2] == who) and (stage[0][0] == default):
                    return 0,0

                #Don't need to check mid, it'll already be taken by this point

                #check Diagonals /
                if (stage[0][2] == stage[1][1] == who) and (stage[2][0] == default):
                    return 2,0
                if (stage[1][1] == stage[2][0] == who) and (stage[0][2] == default):
                    return 0,2


        #Check for the 2 way win
        def checkFork(who):        
            """Check if the game could end in the next move

                Notes:
                  Sub-Method of findBestSpot
                  by making the character in question a parameter,
                  this method works equally well for finding forks
                  for the AI or the opponent

                Arguments:
                  who (str) character that might get a fork

                Returns:
                  coords (tuple) coordinates of potential fork or None     
             """
            def checkCorners(takenA,takenB,emptyA,emptyB):        
                """Checks if 2 corners are taken and a third is empty

                    Notes:
                      Sub-Method of checkFork
                      This method exists entirely to reduce
                      about 30 lines of repetitous code.

                    Arguments:
                      takenA (tuple) coordinates of possibly filled corner
                      takenB (tuple) coordinates of possibly filled corner
                      emptyA (tuple) coordinates of possibly empty corner
                      emptyB (tuple) coordinates of possibly empty corner

                    Returns:
                      coords (tuple) coordinates of good fork corner or None     
                 """
            #Check if takenA and takenB are taken
                if board.spot(*takenA) == board.spot(*takenB) == who:
                    #emptyA is empty
                    if board.spotIsEmpty(*emptyA):
                        return emptyA
                    #emptyB is empty
                    if board.spotIsEmpty(*emptyB):
                        return emptyB
            
            #Check top left and top right
            fork = checkCorners(self.corners["tl"],self.corners["tr"],self.corners["br"],self.corners["bl"])
            if fork: return fork,self.corners["tl"],self.corners["tr"]
            #check top right and bottom right
            fork = checkCorners(self.corners["tr"],self.corners["br"],self.corners["bl"],self.corners["tl"])
            if fork: return fork,self.corners["tr"],self.corners["br"]
            #check bottom right and bottom left
            fork = checkCorners(self.corners["br"],self.corners["bl"],self.corners["tl"],self.corners["tr"])
            if fork: return fork,self.corners["br"],self.corners["bl"]
            #check bottom left and top left
            fork = checkCorners(self.corners["bl"],self.corners["tl"],self.corners["tr"],self.corners["br"])
            if fork: return fork,self.corners["bl"],self.corners["tl"]
            #check diagonals \
            fork = checkCorners(self.corners["tl"],self.corners["br"],self.corners["tr"],self.corners["bl"])
            if fork: return fork,self.corners["tl"],self.corners["br"]
            #check diagonals /
            fork = checkCorners(self.corners["tr"],self.corners["bl"],self.corners["tl"],self.corners["br"])
            if fork: return fork,self.corners["tr"],self.corners["bl"]

        #Game can't end before 3 moves
        if len(board) >= 3:
            #Checks if AI can win
            willWin = couldEnd(char)
            if willWin:
                return willWin

            #Checks if AI can lose next turn
            couldLose = couldEnd(self.opponentChar)
            if couldLose:
                return couldLose

            #checks if AI can fork
            iCanFork = checkFork(char)
            if iCanFork:
                return iCanFork[0]

            #checks if player can fork
            theyCanFork = checkFork(self.opponentChar)
            if theyCanFork:
                row,col = 0,1
                cornerA, cornerB = theyCanFork[1:]
                #Does the opponent have two corners on the same row?
                if cornerA[row] == cornerB[row]: 
                    if board.spotIsEmpty(cornerA[row],1): #is it already blocked?
                        return cornerA[row],1 #if not, block it!
                #Does the opponent have two corners on the same column?
                elif cornerA[col] == cornerB[col]:
                    if board.spotIsEmpty(1,cornerA[col]): #is it already blocked?
                        return 1,cornerA[col] #if not, block it!
                else: #if the opponent has two diagonal corners
                    for side in self.randomSides:
                        if board.spotIsEmpty(*side):
                            return side#take a random available side

        #grab center
        if board.spotIsEmpty(1,1):
            return 1,1

        #grab any corner
        for corner in self.randomCorners:
            if board.spotIsEmpty(*corner):
                return corner

        #grab any side
        for side in self.randomSides:
            if board.spotIsEmpty(*side):
                return side

    def findRandomSpot(self):
        """Finds any random spot for the next move

        Returns:
          coords (tuple) coordinates of a random empty spot"""
        return random.choice(self.board.openSpots())

    def takeTurn(self):
        """Finds the spot for the next move and makes the move"""
        if self.easyMode:
            spot = findRandomSpot()
        else:
            spot = self.findBestSpot()
        self.board.makeMove(*(list(spot) + [self.character]))
