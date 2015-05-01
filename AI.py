"""
Adam Traub
Tic-Tac-Toe AI
4/25/2015

Overhaul of the ai class that won't require
a persistent board object to intelligently
(or not intelligently) make moves.
"""
import random

#Code to run on import
CORNERS = {
         "tl":(0,0,),
         "tr":(0,2,),
         "bl":(2,0,),
         "br":(2,2,),
         }
SIDES = {
         "tm":(0,1,),
         "ml":(1,0,),
         "mr":(1,2,),
         "bm":(2,1,),
     }
RANDOMSIDES = SIDES.values()
RANDOMCORNERS = CORNERS.values()

def reshuffle():
    #helps make behavior less predictable
    random.shuffle(RANDOMSIDES)
    random.shuffle(RANDOMCORNERS)

def findBestSpot(board, aiChar, playerChar):
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
    stage = board.stage
    default = board.default
    def couldEnd(who):
        """Check if the game could end in the next move

            Notes:
              Sub-Method of findBestSpot
              by making the aiCharacter in question a parameter,
              this method works equally well for finding winning
              combinations for the AI and the opponent.

            Arguments:
              who (str) aiCharacter that might achieve the win

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
            if (stage[2][i] == stage[0][i] == who) and (stage[1][i] == default):
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


    #Check for the 2 way Corner win
    def checkFork(who):
        """Check if the opponent can make a fork

            Notes:
              Sub-Method of findBestSpot
              by making the aiCharacter in question a parameter,
              this method works equally well for finding forks
              for the AI or the opponent

            Arguments:
              who (str) aiCharacter that might get a fork

            Returns:
              coords (tuple) coordinates of potential fork or None
         """
        def checkCorners(takenA,takenB,emptyA,emptyB):
            """Checks if 2 CORNERS are taken and a third is empty

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

        #All possible corner fork victory combinations
        cornerCombos = ((CORNERS["tl"],CORNERS["tr"],CORNERS["br"],CORNERS["bl"]),
                        (CORNERS["tr"],CORNERS["br"],CORNERS["bl"],CORNERS["tl"]),
                        (CORNERS["br"],CORNERS["bl"],CORNERS["tl"],CORNERS["tr"]),
                        (CORNERS["bl"],CORNERS["tl"],CORNERS["tr"],CORNERS["br"]),
                        (CORNERS["tl"],CORNERS["br"],CORNERS["tr"],CORNERS["bl"]),
                        (CORNERS["tr"],CORNERS["bl"],CORNERS["tl"],CORNERS["br"]),)

        for combo in cornerCombos:
            fork = checkCorners(*combo)
            if fork: return fork, combo[0], combo[1]

    def checkSides(side1, side2):
        """Checks if 2 Sides surrounding a corner are taken

            Arguments:
              side1 (tuple) coordinates of possibly filled side
              side2 (tuple) coordinates of possibly filled side

            Returns:
              corner (tuple) coordinates of a corner to take to block the 2-way win
         """
        if board.spot(*side1) == board.spot(*side2) == playerChar:
            corner = (side1[0]*side2[0],side1[1]*side2[1])
            if board.spotIsEmpty(*corner):
                return corner


    #Game can't end before 3 moves
    if len(board) >= 3:
        #Checks if AI can win
        willWin = couldEnd(aiChar)
        if willWin:
            return willWin

        #Checks if AI can lose next turn
        couldLose = couldEnd(playerChar)
        if couldLose:
            return couldLose

        #checks if AI can fork
        iCanFork = checkFork(aiChar)
        if iCanFork:
            return iCanFork[0]

        #checks if player can fork
        theyCanFork = checkFork(playerChar)
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
                for side in RANDOMSIDES:
                    if board.spotIsEmpty(*side):
                        return side#take a random available side

        #check if player can make a 2-way side play
        for combo in ((SIDES["tm"], SIDES["ml"]),
                      (SIDES["tm"], SIDES["mr"]),
                      (SIDES["bm"], SIDES["ml"]),
                      (SIDES["bm"], SIDES["mr"])):

            sideSetup = checkSides(*combo)
            if sideSetup is not None:
                return sideSetup

    #grab center
    if board.spotIsEmpty(1,1):
        return 1,1

    #grab any corner
    for corner in RANDOMCORNERS:
        if board.spotIsEmpty(*corner):
            return corner

    #grab any side
    for side in RANDOMSIDES:
        if board.spotIsEmpty(*side):
            return side

def findRandomSpot(board):
    """Finds any random spot for the next move

       Returns:
         coords (tuple) coordinates of a random empty spot
    """
    return random.choice(board.openSpots())

def takeTurn(board, aiChar, playerChar, easyMode=False):
    """Finds the spot for the next move and makes the move"""
    if easyMode:
        spot = findRandomSpot(board)
    else:
        spot = findBestSpot(board, aiChar, playerChar)
    return spot

reshuffle()
