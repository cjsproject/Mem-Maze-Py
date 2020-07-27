from Game.PosHandler import Point
import random
import time
class Board:
    def __init__(self, dim=6):
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
        random.seed(time.time())
        y = 0
        i = 0
        xp = random.randint(0, self._Board__dim-1)
        self.__mazePoints.append((xp, y))
        #current = self.__mazePoints[0]

        while y < self._Board__dim-1:
            random.seed(time.time())
            direction = random.randint(0, 4)
            print(direction)
            current = self.__mazePoints[i]
            if direction == 0 and y+1 < self._Board__dim and self.__mazePoints[i-1] != (current[0], current[1]+1): #up
                self.__mazePoints.append(
                    (current[0], current[1]+1)
                )
                y += 1
                i += 1
                continue
            elif direction == 1 and y != 0 and self.__mazePoints[i-1][1] != current[1]-1: #down, y is not 0, and is not equal to the point before
                self.__mazePoints.append(
                    (current[0], current[1]-1)
                )
                y -= 1
                i += 1
                continue
            elif direction == 2 and xp != 0 and self.__mazePoints[i-1] != (current[0]-1, current[1]):
                #randomDirection == Direction.LEFT && prevX - 1 >= 0 && board[y][prevX - 1].equals("-")
                #left, current x is not next x
                self.__mazePoints.append(
                    (current[0]-1, current[1])
                )
                xp -= 1
                i += 1
                continue
            elif direction == 3 and xp+1 < self._Board__dim:
                self.__mazePoints.append(
                    (current[0]+1, current[1])
                )
                xp += 1
                i += 1
                continue
            else:
                continue

    def __str__(self):
        return str(self.__mazePoints)


x = BoardGame()

#print("\n",x._BoardGame__mazePoints[0], x._BoardGame__mazePoints[0][0]+1, sep='\t')
print(x)
z = [[ (x,y) for x in range(3)] for y in range(3)]

print(z[0][0])



"""
    private void generateBoard() {

        Random rand = new Random();
        int tileCount = 1;
        int y = 0;
        int prevX = rand.nextInt(board.length - 1);
        Direction[] directionChoices = {
                Direction.DOWN,
                Direction.LEFT,
                Direction.RIGHT
        };
        boardPoints.add(new Point(prevX,y, tileCount));
        board[y][prevX] = tileCount++ + "";
        while (y < board.length) {
            boolean directionFound = false;
            while (!directionFound) {
                Direction randomDirection = directionChoices[rand.nextInt(directionChoices.length)];
                if (randomDirection == Direction.LEFT && prevX - 1 >= 0 && board[y][prevX - 1].equals("-")) {
                    board[y][prevX - 1] = tileCount + "";
                    boardPoints.add(new Point(prevX-1,y, tileCount));
                    prevX -= 1;
                    tileCount++;
                    directionFound = true;
                } else if (randomDirection == Direction.RIGHT && prevX + 1 < board.length && board[y][prevX + 1].equals("-")) {
                    board[y][prevX + 1] = tileCount + "";
                    boardPoints.add(new Point(prevX+1,y, tileCount));
                    prevX += 1;
                    tileCount++;
                    directionFound = true;
                } else if (randomDirection == Direction.DOWN) {
                    if (y + 1 >= board.length) {
                        y++;
                        break;
                    }
                    board[++y][prevX] = tileCount + "";
                    boardPoints.add(new Point(prevX,y, tileCount));
                    tileCount++;
                    directionFound = true;
                }
                if (y + 1 >= board.length) {
                    y++;
                    break;
                }
            }
        }
    }

    public ArrayList<Point> getBoardPoints() {
        return boardPoints;
    }

    public void setBoardPoints(ArrayList<Point> x){
        boardPoints = x;
    }

    public int getPlayerTileCount() {
        return playerTileCount;
    }

    public void setPlayerTileCount(int playerTileCount) {
        this.playerTileCount = playerTileCount;
    }


/*    public Difficulty getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(Difficulty difficulty) {
        this.difficulty = difficulty;
    }*/
}
"""
