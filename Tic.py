# Tic-Tac-Toe game using python

board = [' ' for x in range(10)]

def printBoard():
	 print('   '+'|'+'   '+'|'+'   ')
	 print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3]+' ')
	 print('   '+'|'+'   '+'|'+'   ')
	 print('-----------')

	 print('   '+'|'+'   '+'|'+'   ')
	 print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6]+' ')
	 print('   '+'|'+'   '+'|'+'   ')
	 print('-----------')

	 print('   '+'|'+'   '+'|'+'   ')
	 print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' ')
	 print('   '+'|'+'   '+'|'+'   ')

	 print(' \n ')


def insertLetter(letter,position):
	board[position]=letter

def compMove():
	#Listing the available positions
	possibleMoves = [x for x,letter in enumerate(board) if letter==' ' and x!=0 ]
	move=0

	#Finding if the computer can win and if not then,
	#Finding if the computer can block the user from winning
	for let in ['O','X']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i]=let
			if isWinner(boardCopy,let):
				move=i
				return move

	#Now since, none can win (in this step), So, find:
	#(1) If any corner is free,if not
	#(2) then find if the center is free , if not
	#(3) then find if any edge(apart from centr and corners) is free
	CornersFree=[]
	for i in possibleMoves :
		if i in [1,3,7,9]:
			CornersFree.append(i)
	if len(CornersFree)>0:
		move = selectRandomPos(CornersFree)
		return move

	if 5 in possibleMoves:
		move=5
		return move

	EdgesFree=[]
	for i in possibleMoves :
		if i in [2,4,6,8]:
			EdgesFree.append(i)
	if len(EdgesFree>0):
		move = selectRandomPos(EdgesFree)
		return move


def userMove():
	run = True
	while run :
		move=input("Please select a position to place an 'X':  ")
		move=int(move)
		if move>0 and move<10:
			if IsBlockFree(move):
				run=False
				insertLetter('X',move)
			else:
				print('Please select an unoccupied position !')
		else:
			print('Please enter a valid position index bw 0-9!')

def selectRandomPos(li):
	import random
	ln=len(li)
	r = random.randrange(0,ln)
	return li[r]
	

def isWinner(board,sign):
	return (board[1]==sign and board[2]==sign and board[3]==sign)or(board[4]==sign and board[5]==sign and board[6]==sign)or(board[7]==sign and board[8]==sign and board[9]==sign)or(board[1]==sign and board[4]==sign and board[7]==sign)or(board[2]==sign and board[5]==sign and board[8]==sign)or(board[3]==sign and board[6]==sign and board[9]==sign)or(board[1]==sign and board[5]==sign and board[9]==sign)or(board[3]==sign and board[5]==sign and board[7]==sign)


def IsBlockFree(position):
	return board[position]==' '

def isBoardFull(board):
	if board.count(' ')>1:
		return False
	else :
		return True

def main():
	print('Welcome to Tic-Tac-Toe!')
	printBoard()

	while not(isBoardFull(board)):
		if not(isWinner(board,'O')):
			userMove()
			printBoard()
		else:
			print(" Sorry, O's won this time! Good job")
			break

		if not(isWinner(board,'X')):
			move=compMove()
			insertLetter('O',move)
			printBoard()
		else:
			print(" Congratulations!, X's won this time! Good job")
			break

	if isBoardFull(board):
		print('Tie game!')


	

main()