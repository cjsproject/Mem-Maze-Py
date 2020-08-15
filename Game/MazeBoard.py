from Game.PosHandler import Point
import random


class Board:
    def __init__(self, dim=10):
        self.__dim = dim
        self.__board = [[(a, b) for a in range(dim)] for b in range(dim)]

    def validMove(self, point):
        coords = point.getcoord()
        return coords[1] < 0 or coords[1] > self.__dim - 1 or coords[0] < 0 or coords[0] > self.__dim - 1

    #def won(self): return False


class BoardGame(Board):
    x = 0
    y = 0

    def __init__(self):
        super().__init__()
        self.__mazePoints = []
        self.__genBoard()

    def up(self):
        self.y += 1
        self.__mazePoints.append((self.x, self.y))
        return

    def down(self):
        self.y -= 1
        self.__mazePoints.append((self.x, self.y))
        return

    def left(self):
        self.x -= 1
        self.__mazePoints.append((self.x, self.y))
        return

    def right(self):
        self.x += 1
        self.__mazePoints.append((self.x, self.y))
        return

    def __genBoard(self):
        length = self._Board__dim
        self.__mazePoints.append((self.x, self.y))
        while self.y < length - 1:  # issue is that points can get stuck when going backwards on y axis
            direction = random.randrange(4)
            print(direction)
            current = self.__mazePoints[-1]
            # if all possible next points are in mazepoints already, backtrack and direction
            if (current[0] + 1, current[1]) in self.__mazePoints and (
                    current[0] - 1, current[1]) in self.__mazePoints and (
                    current[0], current[1] - 1) in self.__mazePoints and (
                    current[0], current[1] + 1) in self.__mazePoints:
                del self.__mazePoints[1:]
                current = self.__mazePoints[0]
                self.x = 0
                self.y = 0
            elif (current[0] + 1, current[1]) in self.__mazePoints and (
                    current[0] - 1, current[1]) in self.__mazePoints and self.y == 0:
                del self.__mazePoints[1:]
                self.x = 0
                self.y = 0
            elif (current[0], current[1] - 1) in self.__mazePoints and (
                    current[0], current[1] + 1) in self.__mazePoints and self.x == 0 or self.x == 9:
                del self.__mazePoints[1:]
                current = self.__mazePoints[0]
                self.x = 0
                self.y = 0

            if direction == 0 and self.y + 1 < length and (current[0], current[1] + 1) not in self.__mazePoints:
                self.up()
            elif direction == 1 and self.y > 0 and (current[0], current[1] - 1) not in self.__mazePoints:
                self.down()
            elif direction == 2 and self.x > 0 and (current[0] - 1, current[1]) not in self.__mazePoints:
                self.left()
            elif direction == 3 and self.x + 1 < length and (current[0] + 1, current[1]) not in self.__mazePoints:
                self.right()

    def __str__(self):
        for i in self._Board__board:
            for j in i:
                if j in self.__mazePoints:
                    print("(", self.__mazePoints.index(j) + 1, ")", end='\t')
                else:
                    print(j, end='\t')
            print()
        return "Maze Points: " + str(self.__mazePoints)


#d = BoardGame()

#print(d)
#print("\n",d._BoardGame__mazePoints[0], d._BoardGame__mazePoints[0][1]+1, sep='\t')
