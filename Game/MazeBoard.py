
class Board:
    def __init__(self, dim=6):
        self.__dim = dim
        self.__board = [[ (x,y) for x in range(dim)] for y in range(dim)]

    def __str__(self):
        for i in self.__board:
            return str(self.__board)

    def validMove(self, point):
        coords = point.getcoord()
        return coords[1] < 0 or coords[1] > self.__dim-1 or coords[0] < 0 or coords[0] > self.__dim-1

    def won(self): return False

brd = Board(3)
print(brd)
