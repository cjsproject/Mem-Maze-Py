from Game.PosHandler import Point
import random
from time import time
class Board:
    def __init__(self, dim=10):
        random.seed(time())
        self.__dim = dim
        self.__board = [[(x, y) for x in range(dim)] for y in range(dim)]

#    def __str__(self):
#        for i in self.__board:
 #           return str(self.__board)

    def validMove(self, point):
        coords = point.getcoord()
        return coords[1] < 0 or coords[1] > self.__dim-1 or coords[0] < 0 or coords[0] > self.__dim-1

    def won(self): return False


class BoardGame(Board):
    def __init__(self):
        super().__init__()
        self.__mazePoints = []
        self.__playerTileCount = 0;
        self.__genBoard()


    def __genBoard(self):
        y = 0
        i = 0
        xp = random.randint(0, self._Board__dim-1)
        self.__mazePoints.append((xp, y))
        #current = self.__mazePoints[0]

        while y < self._Board__dim-1:
            random.seed(time())
            direction = random.randint(0, 3)
            print(direction)
            current = self.__mazePoints[i]
            if direction == 0 and y+1 < self._Board__dim and (current[0], current[1]+1) not in self.__mazePoints: #up
                self.__mazePoints.append(
                    (current[0], current[1]+1)
                )
                y += 1
                i += 1
                continue
            elif direction == 1 and y != 0 and (current[0], current[1]-1) not in self.__mazePoints: #down, y is not 0, and is not equal to the point before
                self.__mazePoints.append(
                    (current[0], current[1]-1)
                )
                y -= 1
                i += 1
                continue
            elif direction == 2 and xp != 0 and (current[0]-1, current[1]) not in self.__mazePoints:
                #randomDirection == Direction.LEFT && prevX - 1 >= 0 && board[y][prevX - 1].equals("-")
                #left, current x is not next x
                self.__mazePoints.append(
                    (current[0]-1, current[1])
                )
                xp -= 1
                i += 1
                continue
            elif direction == 3 and xp+1 < self._Board__dim and (current[0]+1, current[1]) not in self.__mazePoints:
                self.__mazePoints.append(
                    (current[0]+1, current[1])
                )
                xp += 1
                i += 1
                continue
            else:
                continue

    def __str__(self):
        for i in self._Board__board:
            for j in i:
                if j in self.__mazePoints:
                    print("(", self.__mazePoints.index(j) + 1, ")", end='\t')
                else:
                    print(j, end='\t')
            print()
        return "Maze Points: " + str(self.__mazePoints)


#x = BoardGame()

#print("\n",x._BoardGame__mazePoints[0], x._BoardGame__mazePoints[0][0]+1, sep='\t')
#print(x)

