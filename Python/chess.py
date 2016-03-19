#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# chess.py#
# a python script to play chess on the command line.#
# The intention of this code is create a script that can play chess.#
##
# date: 16/03/2016#
# author: vaemavric#
# site: github.com/vaemavric/projects#
# written in notepad++#
#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
turn = 0
def createBoard():
# createBoard() creates an 9x9 grid in the starting position of chess with labels on grid.
#white at top, black at bottom.
	board = [[0 for x in range(9)]for x in range(9)]
	d= {}
	for x in range(9):
		board[2][x]="W"+ str(x)
		board[7][x]="B" + str(x)
		if x == 1 or x==8:
			c =""
			if x ==1:
				c = "W"
			else: 
				c = "B"
			board[x][1]=c+"R";board[x][2]=c+"N";
			board[x][3]=c+"B";board[x][4]=c+"K";
			board[x][5]=c+"Q";board[x][6]=c+"b";
			board[x][7]=c+"n";board[x][8]=c+"r";
		board[x][0] = x
		board[0][x] = " "+ str(unichr(x+96))
		board[0][0] = 0
	for x in range(2,6):
		for y in range(8):
			board[x+1][y+1]= "  "
	
	return board

def initLoc(board):
#currentLoc(b) takes the board and creates a dictionary.
#b is the array describing the board, The keys are the
# pieces and each value is an array containing the position of the piece.
	dic	= {}
	for x in range (8):
		for y in range (8):
			dic[board[x+1][y+1]] = [x+1,y+1]
	del dic['  ']
	return dic

def printBoard(board):
#printBoard(board) prints the board in its current state.
#b is the array describing the board
	for x in range(9):
		print board[x]
		print "\n"

def nextTurn():
#nextTurn method updates the global turn, turn 0mod2 is white, 1mod2 is black
	global turn
	turn +=1
def prevTurn():
#prevTurn() removes  1 from the turn counter, used when incorrect move made
	global turn
	turn -=1
def getTurn():
#getTurn() returns the value of turn
	return turn

def isNumber(s):
#isNumber takes the string and returns whether it is a number
	try:
		int(s)
		return True
	except ValueError:
		return False
def canTake(piece, pos, loc, board):
#cantTake(Piece, pos, loc, board) tests whether a piece can take the piece in 
#the new locations
	if(piece[0] == board[pos[0]][pos[1]][0]):
		return False
	else:
		return True
		
def isLegal(piece, pos, loc, board):
	p = list(piece)
	if pos == loc[piece]:
		print "Piece already in that position"
		return False
	elif board[pos[0]][pos[1]] != "  " and  not canTake(piece, pos, loc, board):
		print "Cannot take your own piece"
	elif piece in taken:
		print "Piece has been taken"
		return False
	#'must be out of check condition'
	#pawn rules, still needs 'enpasson', can be coded in 'can take condition'
	elif isNumber(p[1]):
		if((pos[1]-loc[piece][1] != 0) and not canTake()):
			return False
		elif((abs(pos[0]-loc[piece][0]) == 2) and (loc[piece][0] != 2 and 
		loc[piece][0] != 7)):
			return False
		elif p[0] == "W":
			if(((pos[0]-loc[piece][0]) > 2) or (pos[0]-loc[piece][0])< 0 ):
				return False
			else:
				return True
		else:
			if(((pos[0]-loc[piece][0]) < -2) or (pos[0]-loc[piece][0])> 0 ):
				return False
			else:
				return True		
	#king rules # needs new position is not check test and castle king
	elif p[1] == "K":
		print "king"
		if(abs(pos[0]-loc[piece][0]) !=1):
			print (abs(pos[0]-loc[piece][0]))
			return False
		else:
			return True
	#queen rules
	elif p[1] == "Q":
		
		if(not(pos[1]-loc[piece][1] == 0 or  pos[0]-loc[piece][0] ==0) and ( abs(pos[0]-loc[piece][0]) != abs(pos[1]-loc[piece][1]))):
			return False
		else:
			return True
	#bishop rules
	
	#knight rules
	#rook rules
	else:
		return True
	
def doMove(piece, pos, loc, board):
#doMove(m, d) moves a piece based on user input in algebraic chess
#notation. Checks to see if move is legal using method isLegal()
# m is the users move
# loc is the dictionary of current piece location
# updates 'd' the dictionary with current positions to the new positions
# updates the board to reflect the new positions
	try:
		if isLegal(piece, pos, loc, board):
			#puts piece in new position on the board array
			board[pos[0]][pos[1]] = piece
			f = loc[piece]
			#removes the piece from the old location
			board[f[0]][f[1]] = "  "
			#updates the dictionary to contain the new position
			loc[piece] = [pos[0],pos[1]]
			d= loc
		else:
			print "Piece cannot do that move."
			prevTurn()
	except:
		prevTurn()
		print("Please enter a valid move")
	
def getMove(loc, board):
#getMove(loc, board) asks the user for a move in algebraic form and returns it 
#as a string. Requires the dictionary containing the current locations and the
#current board array in order to pass the move to the 'doMove' function.
	m =raw_input("Please enter your move in algebraic form: \n")
	a = list(m)
	t = getTurn()
	if t%2 == 0:
		piece = "W"+ a[0]
	else:
		piece = "B" +a[0]
	pos= [int(a[3]),ord(a[2])-96]
	doMove(piece, pos, loc, board)
	
b = createBoard()
d = initLoc(b)
taken = []
print d["W8"]

while True:
#While loop.
	try:
		printBoard(b)
		getMove(d, b)
		nextTurn()
	except:
		print"Quiting chess"
		quit()