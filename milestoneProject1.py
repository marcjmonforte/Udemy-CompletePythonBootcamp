# =================================
# MILESTONE PROJECT #1: Tic Tac Toe
# =================================

# ================================
# STEP 1: Construct the gameboard.
# ================================

from IPython.display import clear_output		# To immediately clear all output.

def game_board(board):

	clear_output()

	print '   T  I  C  T  A  C  T  O  E   '
	print '==============================='
	print '-------------------------------'
	print '|' + '1' +'        |' + '2' +'        |' + '3' +'        |'
	print '|    ' + board[1] + '    |    ' + board[2] + '    |    ' + board[3] + '    |'
	print '|         |         |         |'
	print '-------------------------------'
	print '|' + '4' +'        |' + '5' +'        |' + '6' +'        |'
	print '|    ' + board[4] + '    |    ' + board[5] + '    |    ' + board[6] + '    |'
	print '|         |         |         |'
	print '-------------------------------'
	print '|' + '7' +'        |' + '8' +'        |' + '9' +'        |'
	print '|    ' + board[7] + '    |    ' + board[8] + '    |    ' + board[9] + '    |'
	print '|         |         |         |'
	print '-------------------------------'
	print '==============================='

board = ['nothing',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# ==========================
# STEP 2: Take player input.
# ==========================

def player_input():
	marker = ''
	while not (marker == 'O' or marker == 'X'):
		marker = raw_input('Player 1: Do you want to be X or O?').upper()

	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')

# =======================================
# STEP 3: Place their input on the board.
# =======================================

def place_marker (board, marker, position):
	board[position] = marker

# ========================================================
# STEP 4: Check if the game is won,tied, lost, or ongoing.
# ========================================================

def win_check(board,marker):
	return ((board[1] == marker and board[2] == marker and board[3] == marker) or
	(board[4] == marker and board[5] == marker and board[6] == marker) or
	(board[7] == marker and board[8] == marker and board[9] == marker) or
	(board[1] == marker and board[4] == marker and board[7] == marker) or
	(board[2] == marker and board[5] == marker and board[8] == marker) or
	(board[3] == marker and board[6] == marker and board[9] == marker) or
	(board[1] == marker and board[5] == marker and board[9] == marker) or
	(board[7] == marker and board[5] == marker and board[3] == marker))

# ===========================================================
# STEP 5: Repeat c and d until the game has been won or tied.
# ===========================================================

import random
def choose_first():
	if random.randint(0,1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'

# =========================================================
# STEP 6: Figure out if space on board is freely available.
# =========================================================

def space_check(board,position):
	return board[position] == ' '

# ===============================
# STEP 7: Check if board is full.
# ===============================

def full_board_check(board):
	for i in xrange (1,10):
		if space_check(board,i):
			return False
	return True

# =====================================================================================================
# STEP 8: Ask player where they want to go, and then use step 6's function to see if it's a valid move.
# =====================================================================================================

def player_choice(board):
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
		position = raw_input('Choose your next position: (1-9)')

	return int(position)

# ==================================
# STEP 9: Do you want to play again?
# ==================================

def replay():
	return raw_input('Do you want to play again? Enter "Yes" or "No"').lower().startswith('y')

# ======================
# STEP 10: Run the game!
# ======================

print 'Welcome to Tic Tac Toe'

while True:

    theBoard = [' '] * 10
    p1_marker, p2_marker = player_input()
    turn = choose_first()
    print turn + ' will go first!'

    game_on = True

    while game_on:

        if turn == 'Player 1':
            game_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,p1_marker,position)

            if win_check(theBoard,p1_marker):
                game_board(theBoard)
                print 'You win!'
                game_on = False

            else:
                if full_board_check(theBoard):
                    game_board(theBoard)
                    print 'Draw!'
                    break
                else:
                    turn = 'Player 2'

        else:
            game_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,p2_marker,position)

            if win_check(theBoard,p2_marker):
                game_board(theBoard)
                print 'You win!'
                game_on = False

            else:
                if full_board_check(theBoard):
                    game_board(theBoard)
                    print 'Draw!'
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break