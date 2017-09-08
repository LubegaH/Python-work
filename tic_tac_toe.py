#!/usr/local/bin/python
# coding: latin-1

# Played by two players
# One player is X while the other is O
# To win, one must match across a column or row or diagonal
# Game can end in a draw.

'''This program should eventually incorporate an AI as the second player
Idea is to make the AI try to defeat the the user and at evry level
'''

from __future__ import print_function
import random
import os

# method to clear screen on rerun
def clear():
	os.system('clear')
# drawBoard Method displays the board
def drawBoard(board):
	clear()
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('------------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('------------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')



# decides which letter player should be
def player_input():
	letter_chosen = ''
	while not(letter_chosen == 'X' or letter_chosen == 'O'):
		letter_chosen = raw_input('Player 1: Do you want to be X or O? ').upper()
	if letter_chosen == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

# Put marker on the board
def place_marker(board, marker, position):
	board[position] = marker

# checking for a win
def win_checker(board,mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # Across the top
	(board[4] == mark and board[5] == mark and board[6] == mark) or # Across the middle
	(board[1] == mark and board[2] == mark and board[3] == mark) or # Across the bottom
	(board[7] == mark and board[4] == mark and board[1] == mark) or # Down the left
	(board[8] == mark and board[5] == mark and board[2] == mark) or # Down the middle
	(board[9] == mark and board[6] == mark and board[3] == mark) or # Down the right
	(board[7] == mark and board[5] == mark and board[3] == mark) or # Diagonal left to right
	(board[9] == mark and board[5] == mark and board[1] == mark) # Diagonal right to left
	) 

# deciding who goes first
def first_player():
	if random.randint(0, 1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'


# check if there is a space on the board
def space_check(board, position):
	return board[position] == ' '

# check if board is full
def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True

# Method asks player to place marker in position of choice
def player_choice(board):
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
		position = raw_input('Choose your next position: (1 - 9): ')
	return int(position)

# Replay method
def replay():
	return raw_input('Do you want to play again? Enter Yes or No').lower().startswith('y')

# Putting it all together

print("This is the tic tac toe game. \n Play by putting your marker in the designed position as mapped by a keyboard Numpad")

while True:
	# Reset board
	myboard = [' '] * 10
	palyer1_marker, player2_marker = player_input()
	turn = first_player()
	print(turn + ' will go first')
	game_on = True

	while game_on:
		if turn == 'Player 1':
			# Player 1's turn

			drawBoard(myboard)
			position = player_choice(myboard)
			place_marker(myboard, palyer1_marker, position)

			# check player 1 has won
			if win_checker(myboard, palyer1_marker):
				drawBoard(myboard)
				print("Congrats, Player 1 has won the game!!!")
				game_on = False

			else:
				# Check if there is a tie
				if full_board_check(myboard):
					drawBoard(myboard)
					print("The game is a draw")
					break
				else:
					turn = 'Player 2'
		else:
			# Player 2 turn
			drawBoard(myboard)
			position = player_choice(myboard)
			place_marker(myboard, player2_marker, position)

			# Check if player 2 has won
			if win_checker(myboard, player2_marker):
				drawBoard(myboard)
				print("Congrats, Player 2 has won the game!!!")
				game_on = False

			else:
				# Check if there is a tie
				if full_board_check(myboard):
					drawBoard(myboard)
					print("The game is a draw")
					break
				else:
					turn = 'Player 1'

	# break out of main game loop if player does not want to play again
	if not replay():
		break











