from graphics import *
from boards import *
import random

numRows = 9
numCols = 9
squareWidth = 50
## win is the window that is generated. 
win = GraphWin ("Sudoku Solver by Husan Sattarov", 460, 500)

def generateBoard(): ## This function generates a board that will then be solved using the backtracking algorithm. 
    whichBoard = random.randint(1,3)
    if whichBoard == 1:
        board = board1
    elif whichBoard == 2:
        board = board2
    else:
        board = board3
    return board

board = generateBoard()

def emptyPlace (board): ## This function returns the row and column of the first empty place on the board. 
    for i in range (numCols):
        for j in range (numRows):
            if board[i][j] == 0:
                return [i,j]


def valid(board, num, pos): ## This function checks to see if the num can be placed at the pos based on the current state of the board.
    y = pos[0]
    x = pos[1]

    ## Checking the validity of the column
    for i in range (numCols):
        if board[y][i] == num and x != i:
            return False
    
    ## Checking the validity of the row.
    for i in range (numRows):
        if board[i][x] == num and y != i:
            return False

    whichRow = pos[1] // 3
    whichCol = pos[0] // 3

    loopCalc_y = whichCol * 3
    loopCalc_x = whichRow * 3
    
    ## Checking the validity of the box. 
    for i in range (loopCalc_y, loopCalc_y + 3):
        for j in range (loopCalc_x, loopCalc_x + 3):
            if board[i][j] == num and [i,j] != pos:
                return False

    return True


def solveBoard(board): ## This function uses the backtracking algorithm and solves the board.
    time.sleep(0.15)
    firstEmpty = emptyPlace(board)

    if not firstEmpty: ## If there is no empty spots, it means we found a valid solution so we return True.
        return True

    whichRow = firstEmpty[0]
    whichCol = firstEmpty[1]

    for i in range (1,10):  ## Otherwise, we iterate through possible numbers that we can place and see which one is valid. 
        if valid(board,i,[whichRow, whichCol]):
            board[whichRow][whichCol] = i
            draw(whichRow, whichCol, i, "aqua")

            if solveBoard(board):  ## We recursively call the function to continue this process. 
                return True
            ##If the board cannot be solved based on the number we placed, we reset it and try more options. 
            board[whichRow][whichCol] = 0
            draw(whichRow, whichCol, 0, color_rgb(217,81,78))  
            time.sleep(0.15) 
    
    return False
 
def drawBoard(board): ## This function draws out the grid on the screen. 
  for row in range(numCols):
    for col in range(numRows):
      if board[row][col] == 0:
        draw(row, col, board[row][col], 'white')
      else:
        draw(row, col, board[row][col], 'green')

def rectangleContains(rect, point):  ## This function returns a boolean value indicating whether the point is within the bounds of the rectangle. 
    x = point.getX()
    y = point.getY()
    rect_p1 = rect.getP1()
    rect_p2 = rect.getP2()

    return x >= rect_p1.getX() and x <= rect_p2.getX() and y >= rect_p1.getY() and y <= rect_p2.getY()



def draw(row, col, val, color):  ## This function draws out the whole grid
    topLeft = Point(col * squareWidth, row * squareWidth)
    bottomRight = Point((col + 1) * squareWidth, (row + 1) * squareWidth)
    box = Rectangle(topLeft, bottomRight)
    box.setFill(color)
    box.draw(win)

    if val != 0:
        value = str(val)
        text_loc = Point(col * squareWidth + squareWidth/2, row * squareWidth + squareWidth/2)
        numToPlace = Text(text_loc, value)
        numToPlace.draw(win)

while True:
    drawBoard(board)
    solve = Rectangle(Point(180, 455), Point(280, 495))
    solveText = Text(Point(230, 475), "Solve")
    solve.draw(win)
    solveText.draw(win)

    solved = False
    while not solved:
        userInput = win.getMouse()
        ## If the mouse was clicked and was in the range of the button, we call the function to solve the board. 
        if rectangleContains(solve, userInput): 
            solveBoard(board)
        solved = True
    win.close()