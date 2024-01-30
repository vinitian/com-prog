# HW1 TIC-TAC-TOE (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main()

def show_board(board):
    # show current board state on screen
    # enter your code here
    n = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
      if board[i] == 'O' or board[i] == 'X':
        n[i] = board[i]
    print(f' {n[0]} | {n[1]} | {n[2]}\n---+---+---\n {n[3]} | {n[4]} | {n[5]}\n---+---+---\n {n[6]} | {n[7]} | {n[8]}')

def available(board):
    # return a list of integer numbers indicate the available positions in current board status
    x = []
    # enter your code here
    for i in range(9):
      if board[i] == '-':
        x.append(i+1)
    return x

def generate_unique_random_sequence(n, seed_value=None):
    # return a list of unique random sequence from 0 to n-1
    import random
    random.seed(seed_value)
    sequence = []
    # enter you code here
    for i in range(n):
      sequence += [random.randint(0,n-1)]
    return sequence

def get_new_board_state(board, position, player_turn):
    # return new board state after player/computer's turn
    # enter your code here, and remove the line with 'pass'
    if player_turn:
      board = board[:position-1] + 'X' + board[position:]
    else:
      board = board[:position-1] + 'O' + board[position:]
    return board

def check_win(b):
    # check whether the board status is in winning conditions
    # return 'True' if someone win, and 'False' otherwise.
    # enter your code here
    if (b[0] != '-' and b[0] == b[4] and b[0] == b[8]) or (b[2] != '-' and b[2] == b[4] and b[2] == b[6]): # diagonal win
      return True
    for i in range(9):
      if b[i] != '-' and i%3 == 0 and b[i] == b[i+1] and b[i] == b[i+2]: # horizontal win -- i = 0,3,6 // position 1,4,7
          return True
      elif b[i] != '-' and i<3 and b[i] == b[i+3] and b[i] == b[i+6]: # vertical win -- i = 0,1,2 // position 1,2,3
          return True

#
# DO NOT modify the code after this line
#
def get_computer_turn(board):
    b = available(board) # need to implement
    # [1, ..., 9] without positions played
    k = generate_unique_random_sequence(len(b)) # need to implement
    # select the first position k
    return b[k[0]]

def get_player_turn(board):
    b = available(board) # need to implement
    print("Player's turn")
    print('Enter: ' + str(b))
    x = int(input())
    while x not in b:
        print('Wrong input please enter: ' + str(b))
        x = int(input())
    return x

exec(input().strip())