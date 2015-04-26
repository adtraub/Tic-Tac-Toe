"""
Adam Traub
Tic-Tac-Toe Board
4/25/2015
"""

class Board:
    """Represents a Tic-Tac-Toe board with some handy functions

        Args:
          default (str): The default character left at blank spots

        Attributes:
          default (str): The default character left at blank spots.
          stage (list): A 2-dimensional list representing the board.
          spotsTaken (int): keeps track of the number of moves made.
     """

    def __init__(self, stage=None, default=""):
        self.default = default
        if stage and isProperStage(stage):
            self.stage = stage
        else:
            self.stage = [[default for i in range(3)] for x in range(3)]

        self.spotsTaken = 0

    def makeMove(self,x,y,value):
        """Makes a Move at the given coords.

            Args:
              x (int): The value corresponding to x on a cartesian plane.
              y (int): The value corresponding to y on a cartesian plane.
              value (str): The value to place onto the board.

            Raises:
              IndexError: If index out of bounds or spot is taken.
         """
        if self.spotIsEmpty(x,y):
            self.stage[x][y] = value
            self.spotsTaken += 1
        else:
            raise IndexError("That spot is taken")

    def spotIsEmpty(self,x,y):
        """Check if a given location is empty.

            Args:
              x (int): The value corresponding to x on a cartesian plane.
              y (int): The value corresponding to y on a cartesian plane.

            Returns:
              (bool): True if empty False otherwise.
         """
        return self.stage[x][y] == self.default

    def spot(self,x,y):
        """Returns element at the given spot

            Args:
              x (int): The value corresponding to x on a cartesian plane.
              y (int): The value corresponding to y on a cartesian plane.

            Returns:
              (probably a string): value located at the given coordinates.
         """
        return self.stage[x][y]

    #Returns a list of all open spots on the board
    def openSpots(self):
        """Returns a list of all empty coordinates

            Returns:
              (list of tuples): all available coordinates
         """
        return [(i,j) for i in range(3) for j in range(3) if self.spotIsEmpty(i,j)]

    def __len__(self):
        """Returns the number spots filled (moves made)

            Returns:
              (int): number of moves made
         """
        return self.spotsTaken

    def __str__(self):
        """Simple String representation of the board
            Returns:
              (str): representation of the board using list unpacking magic
        """
        return"""{0:^3}|{1:^3}|{2:^3}
-----------
{3:^3}|{4:^3}|{5:^3}
-----------
{6:^3}|{7:^3}|{8:^3}
""".format(*(self.stage[0] + self.stage[1] + self.stage[2]))


    def gameOver(self):
        """Checks if the game is over

            Returns:
              (bool) True if the game is over, False otherwise.
              (str) Character of winning player if there is one
                    default character if no winner.
        """
        for i in range(3):
            #Row win
            if self.stage[i][0] == self.stage[i][1] == self.stage[i][2] != self.default:
                return True,self.stage[i][0]
            #column win
            if self.stage[0][i] == self.stage[1][i] == self.stage[2][i] != self.default:
                return True,self.stage[0][i]
        #diagnoal win \
        if self.stage[0][0] == self.stage[1][1] == self.stage[2][2] != self.default:
            return True,self.stage[1][1]
        #diagonal win /
        if  self.stage[0][2] == self.stage[1][1] == self.stage[2][0] != self.default:
            return True,self.stage[1][1]
        #stalemate
        if self.spotsTaken >= 9:
            return True,self.default
        #No winner
        return False,""

def isProperStage(stage):
    """Checks if the stage is a proper stage

        Arguments:
          stage(list) a 3x3 list containg a tic-tac-toe stage

        Returns:
          retVal(bool) True if the stage is a 3x3 list
    """
    retVal = True
    if type(stage) == list and len(stage) == 3:
        for row in stage:
            if not (type(row) == list and len(row) == 3):
                retVal = False
                break #No need to continue if even 1 row is bad
    else:
        retVal = False

    return retVal
