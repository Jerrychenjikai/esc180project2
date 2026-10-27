"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 19, 2026
"""

'''
1. no global variables
2. d_y, d_x represent direction of sequences, and both could only take on 0 or 1
3. coordinate (y, x) means board[y][x]
4. open sequence: a stone can be put on both ends
   closed sequence: no stone could be put on either end
   semi_open: not open nor closed'''

def is_empty(board):
    '''This function returns True iff there are no stones on the board board'''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board [i][j] != " ":
                return False
    return True
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    '''This function analyses the sequence of length length that ends at location (y_end,
x_end). The function returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence
if semi-open, and "CLOSED" if the sequence is closed.
Assume that the sequence is complete (i.e., you are not just given a subsequence) and valid, and
contains stones of only one colour.'''
    pass
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''This function analyses the row (let’s call it R) of squares that starts at the location
(y_start,x_start) and goes in the direction (d_y,d_x). Note that this use of the word
row is different from “a row in a table”. Here the word row means a sequence of squares, which
are adjacent either horizontally, or vertically, or diagonally. The function returns a tuple whose
first element is the number of open sequences of colour col of length length in the row R 
and whose second element is the number of semi-open sequences of colour col of length
length in the row R
Assume that (y_start,x_start) is located on the edge of the board. Only complete
sequences count. For example, column 1 in Fig. 1 is considered to contain one open row of
length 3, and no other rows.'''
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    '''This function analyses the board board. The function returns a tuple, whose first element is the
number of open sequences of colour col of length length on the entire board, and whose
second element is the number of semi-open sequences of colour col of length length on the
entire board.
Only complete sequences count. For example, Fig. 1 is considered to contain one open row of
length 3, and no other rows.
Assume length is an integer greater or equal to 2.'''
    open_seq_count, semi_open_seq_count = 0, 0
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    '''This function uses the function score() (provided) to find the optimal move for black. It finds
the location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes
the score of the board as calculated by score(). The function returns a tuple (y, x) such
that putting a black stone in coordinates (y, x) maximizes the potential score (if there are
several such tuples, you can return any one of them). After the function returns, the contents of
board must remain the same.'''
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])
    
def is_win(board):
    '''This function determines the current status of the game, and returns one of ["White won",
"Black won", "Draw", "Continue playing"], depending on the current status on
the board. The only situation where "Draw" is returned is when board is full.'''
    pass

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

if __name__ == '__main__':
    play_gomoku(8)
    
