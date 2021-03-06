#!/bin/env python2.7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                       chess.py                                                               #
#                                    python script to play chess on the command line.                                          #
#                            The intention of this code is create a script that can play chess.                                #
#                                                                                                                              #
#                                                   date:16/03/2016                                                            #
#                                                  author: vaemavric                                                           #
#                                         site: github.com/vaemavric/projects                                                  #
#                                                 written in notepad++                                                         #
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#board: multidimensional array, board[row][column]
#loc: dictionary, loc[piece]
#pos: list, pos=[row,column]
turn = 0
def createBoard():
# createBoard() creates an 9x9 grid in the starting position of chess with labels on grid. white at top, black at bottom.
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
#currentLoc(b) takes the board and creates a dictionary. b is the array describing the board, The keys are the pieces and 
#each value is an array containing the position of the piece.
	dic	= {}
	for x in range (8):
		for y in range (8):
			dic[board[x+1][y+1]] = [x+1,y+1]
	del dic['  ']
	return dic

def printBoard(board):
#printBoard(board) prints the board in its current state. b is the array describing the board
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
#cantTake(Piece, pos, loc, board) tests whether a piece can take the piece in the new locations
	if(piece[0] == board[pos[0]][pos[1]][0]):
		print "Can't take"
		return False
	elif(board[pos[0]][pos[1]][1]=="K"):
		print "Can't take King"
		return False
	else:
		print " Can take"
		return True
def isBlocked(piece, pos, loc, board):
	hor = abs(pos[0]-loc[piece][0])
	ver = abs(pos[1]-loc[piece][1])
	#Vertical check
	if((pos[0]-loc[piece][0]) ==0):
		for x in range (1, ver):
			if (pos[1]-loc[piece][1] <0):
				if board[loc[piece][0]][loc[piece][1] - x] != "  ":
					print "Blocked by "+ board[loc[piece][0]][loc[piece][1] - x]
					return True
			elif(pos[1]-loc[piece][1] >0):
				if board[loc[piece][0]][loc[piece][1] + x] != "  ":
					print "Bloced by "+ board[loc[piece][0]][loc[piece][1] + x]
					return True
			else:
				return False
		
	#Horizontal check
	if((pos[1]-loc[piece][1]) ==0):
		for x in range (1, hor):
			if (pos[0]-loc[piece][0] <0):
				if board[loc[piece][0] - x][loc[piece][1]] != "  ":
					print "Blocked by "+ board[loc[piece][0] - x][loc[piece][1]]
					return True
			elif(pos[0]-loc[piece][0] >0):
				if board[loc[piece][0] + x][loc[piece][1]] != "  ":
					print "Blocked by " +board[loc[piece][0] + x][loc[piece][1]]
					return True
			else:
				return False
		
	#Diagonal check
	else:
		for x in range (1, ver):
			if(pos[0]-loc[piece][0] <0):
				if (pos[1]-loc[piece][1] <0):
					if board[loc[piece][0]-x][loc[piece][1] - x] != "  ":
						print "Blocked by "+ board[loc[piece][0]-x][loc[piece][1] - x]
						blocked =  True
				elif (pos[1]-loc[piece][1] >0):
					if board[loc[piece][0]-x][loc[piece][1] + x] != "  ":
						print "Blocked by "+ board[loc[piece][0]+x][loc[piece][1] + x]
						return True
				else:
					return False
			else:
				if (pos[1]-loc[piece][1] <0):
					if board[loc[piece][0]+x][loc[piece][1] - x] != "  ":
						print "Blocked by "+ board[loc[piece][0]-x][loc[piece][1] - x]
						return True
				elif (pos[1]-loc[piece][1] >0):
					if board[loc[piece][0]+x][loc[piece][1] + x] != "  ":
						print "Blocked by "+ board[loc[piece][0]+x][loc[piece][1] + x]
						return True
				else:
					return False
def inCheck(loc, board, pos):
	#Need to change the code so it returns whether the position it in check
	#Best achieved by returning the first non zero piece and seeing if its a
	#piece that could cause check from that postion
	P = pos
	check = False
	#vertical check
	#veritcal down
	for x in range (1, 9-P[0]):
		if board[P[0]+x][P[1]] == "  ":
			pass
		elif turn%2 == 0 :
			if board[P[0]+x][P[1]][0] == "W":
				break
			else:
				print board[P[0]+x][P[1]]
		else:
			if board[P[0]+x][P[1]][0] == "B":
				break
			else:
				print board[P[0]+x][P[1]]
	#vertical up
	for x in range (1, P[0]):
		if board[P[0]-x][P[1]] == "  ":
			pass
		elif turn%2==0:
			if board[P[0]-x][P[1]][0] == "W":
				break
			else:
				print board[P[0]-x][P[1]]
		else:
			if board[P[0]-x][P[1]][0] == "B":
				break
			else:
				print board[P[0]-x][P[1]]
					
	#horizontal check
	#horizontal right
	for x in range (1, 9-P[1]):
		if board[P[0]][P[1]+x] == "  ":
			pass
		elif turn%2==0:
			if board[P[0]][P[1]+x][0] == "W":
				break
			else:
				print board[P[0]][P[1]+x]
		else:
			if board[P[0]][P[1]+x][0] == "B":
				break
			else:
				print board[P[0]][P[1]+x]
	#horizontal left
	for x in range (1, P[1]):
		if board[P[0]][P[1]-x] == "  ":
			pass
		elif turn%2==0:
			if board[P[0]][P[1]-x][0] == "W":
				break
			else:
				print board[P[0]][P[1]-x]
		else:
			if board[P[0]][P[1]-x][0] == "B":
				break
			else:
				print board[P[0]][P[1]-x]
	#diagonal check
	UR = min(P[0], 9-P[1])
	UL = min(P[0], P[1])
	DR = min(9-P[0], 9-P[1])
	DL = min(9-P[0], P[1])
	for x in range (1, UR):
		if board[P[0]-x][P[1]+x] == "  ":
			pass
		elif turn%2==0:
			if board[P[0]-x][P[1]+x][0] == "W":
				break
			else:
				print board[P[0]-x][P[1]+x]
		else:
			if board[P[0]-x][P[1]+x][0] == "B":
				break
			else:
				print board[P[0]-x][P[1]+x]
	for x in range (1, UL):
		if board[P[0]-x][P[1]-x] == "  ":
			pass
		elif turn%2==0:
			if board[P[0]-x][P[1]-x][0] == "W":
				break
			else:
				print board[P[0]-x][P[1]-x]
		else:
			if board[P[0]-x][P[1]-x][0] == "B":
				break
			else:
				print board[P[0]-x][P[1]-x]
	for x in range (1, DR):
		if board[P[0]+x][P[1]+x] == "  ":
			pass
		elif turn%2==0:
			if board[P[0]+x][P[1]+x][0] == "W":
				break
			else:
				print board[P[0]+x][P[1]+x]
		else:
			if board[P[0]+x][P[1]+x][0] == "B":
				break
			else:
				print board[P[0]+x][P[1]+x]
	for x in range (1, DL):
		if board[P[0]+x][P[1]-x] == "  ":
			pass
		elif turn%2==0:
			if board[P[0]+x][P[1]-x][0] == "W":
				break
			else:
				print board[P[0]+x][P[1]-x]
		else:
			if board[P[0]+x][P[1]-x][0] == "B":
				break
			else:
				print board[P[0]+x][P[1]-x]
	#knight check
	if (0<P[0]+2<9 and 0<P[1]+1<9):
		if board[P[0]+2][P[1]+1] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]+2][P[1]+1][0] == "W":
				pass
			else:
				print board[P[0]+2][P[1]+1]
		else:
			if board[P[0]+2][P[1]+1][0] == "B":
				pass
			else:
				print board[P[0]+2][P[1]+1]
	if (0<P[0]+2<9 and 0<P[1]-1<9):
		if board[P[0]+2][P[1]-1] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]+2][P[1]-1][0] == "W":
				pass
			else:
				print board[P[0]+2][P[1]-1]
		else:
			if board[P[0]+2][P[1]-1][0] == "B":
				pass
			else:
				print board[P[0]+2][P[1]-1]
	if (0<P[0]-2<9 and 0<P[1]+1<9):
		if board[P[0]-2][P[1]+1] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]-2][P[1]+1][0] == "W":
				pass
			else:
				print board[P[0]-2][P[1]+1]
		else:
			if board[P[0]-2][P[1]+1][0] == "B":
				pass
			else:
				print board[P[0]-2][P[1]+1]
	if (0<P[0]-2<9 and 0<P[1]-1<9):
		if board[P[0]-2][P[1]-1] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]-2][P[1]-1][0] == "W":
				pass
			else:
				print board[P[0]-2][P[1]-1]
		else:
			if board[P[0]-2][P[1]-1][0] == "B":
				pass
			else:
				print board[P[0]-2][P[1]-1]
	if (0<P[0]+1<9 and 0<P[1]+2<9):
		if board[P[0]+1][P[1]+2] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]+1][P[1]+2][0] == "W":
				pass
			else:
				print board[P[0]+1][P[1]+2]
		else:
			if board[P[0]+1][P[1]+2][0] == "B":
				pass
			else:
				print board[P[0]+1][P[1]+2]
	if (0<P[0]+1<9 and 0<P[1]-2<9):
		if board[P[0]+1][P[1]-2] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]+1][P[1]-2][0] == "W":
				pass
			else:
				print board[P[0]+1][P[1]-2]
		else:
			if board[P[0]+1][P[1]-2][0] == "B":
				pass
			else:
				print board[P[0]+1][P[1]-2]
	if (0<P[0]-1<9 and 0<P[1]+2<9):
		print board[P[0]-1][P[1]+2]
		
		if board[P[0]-1][P[1]+2] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]-1][P[1]+2][0] == "W":
				pass
			else:
				print board[P[0]-1][P[1]+2]
		else:
			if board[P[0]-1][P[1]+2][0] == "B":
				pass
			else:
				print board[P[0]-1][P[1]+2]
	if (0<P[0]-1<9 and 0<P[1]-2<9):
		if board[P[0]-1][P[1]-2] == "  ":
			pass
		if turn%2 == 0:
			if board[P[0]-1][P[1]-2][0] == "W":
				pass
			else:
				print board[P[0]-1][P[1]-2]
		else:
			if board[P[0]-1][P[1]-2][0] == "B":
				pass
			else:
				print board[P[0]-1][P[1]-2]

def isLegal(piece, pos, loc, board):
	p = list(piece)
	#check to see if move is actually a move
	if pos == loc[piece]:
		print "Piece already in that position"
		return False
	#checks to see if piece can move to that position 
	elif board[pos[0]][pos[1]] != "  " and  not canTake(piece, pos, loc, board):
		print "Cannot take your own piece"
	#checks to see if piece is taken
	elif piece in taken:
		print "Piece has been taken"
		return False
	#'must be out of check condition'
	#pawn rules, still needs 'enpasson', can be coded in 'can take condition'
	elif isNumber(p[1]):
		if((pos[1]-loc[piece][1] != 0) and not canTake()):
			return False
		elif((abs(pos[0]-loc[piece][0]) == 2) and (loc[piece][0] != 2 and loc[piece][0] != 7)):
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
		if(abs(pos[0]-loc[piece][0]) !=1):
			print "King cannot do that move"
			return False
		else:
			return True
	#knight rules
	elif p[1].lower() == "n":
		if (((abs(pos[0]-loc[piece][0]) == 2) and abs(pos[1]-loc[piece][1]) ==1) or ((abs(pos[1]-loc[piece][1]) == 2) and 
		abs(pos[0]-loc[piece][0]) ==1)):
			return True
		else:
			print " Knight cannot do that move"
			return False
	#blocked condition
	elif(isBlocked(piece, pos, loc, board)):
		return False
	#queen rules
	elif p[1] == "Q":
		if(not(pos[1]-loc[piece][1] == 0 or  pos[0]-loc[piece][0] ==0) and (abs(pos[0]-loc[piece][0]) != 
		abs(pos[1]-loc[piece][1]))):
			print "Queen cannot do that move"
			return False
		else:
			return True
	#bishop rules
	elif p[1].lower() == "b":
		if(abs(pos[0]-loc[piece][0]) != abs(pos[1]-loc[piece][1])):
			print "Bishop cannot do that move"
			return False
		else:
			return True
	#rook rules
	elif p[1].lower() == "r":
		if not(pos[1]-loc[piece][1] == 0 or  pos[0]-loc[piece][0] ==0):
			print "Rook cannot do that move"
			return False
		else:
			return True
	else:
		return True
	
def doMove(piece, pos, loc, board):
#doMove(m, d) moves a piece based on user input in algebraic chess notation. Checks to see if move is legal using method 
#isLegal(). m is the users move, loc is the dictionary of current piece location, updates 'd' the dictionary with current
#positions to the new positions updates the board to reflect the new positions
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
	B = loc["WK"]
	inCheck(loc, board, B)
	doMove(piece, pos, loc, board)
	
b = createBoard()
d = initLoc(b)
taken = []

while True:
#While loop.
	#try:
		printBoard(b)
		getMove(d, b)
		nextTurn()
	#except:
	#	print"Quiting chess"
	#	quit()