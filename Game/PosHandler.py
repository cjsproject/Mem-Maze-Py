class Point:
    def __init__(self, x, y, step=None):
        self.__coord = (x, y)
        self.__step = step
        self.next = [lambda z: self.possibleMoves()]

    def possibleMoves(self):

        pass

    def equals(self, point):
        return point.getcoord() == self.__coord

    def getCoord(self):
        return self.__coord

    def setCoord(self, coord, xy):
        if xy:
            self.__coord = tuple(coord[0], self.__coord[1])
        else:
            self.__coord[1] = tuple(self.__coord[0], coord[1])

    def getStep(self):
        return self.__step

    def __str__(self):
        return str(self.__coord)
