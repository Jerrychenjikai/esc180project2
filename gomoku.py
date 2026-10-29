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
2. d_y, d_x represent direction of sequences, and both could only take on 0 or 1 or -1
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
    color = board[y_end][x_end]
    if color == "w":
        opp_color = "b"
    else:
        opp_color = "w"

    if d_y == 0 and d_x == 1: #left to right
        left_position_empty = False
        right_position_empty = False
        #check left
        if x_end - length >= 0:
            if board[y_end][x_end - length] == " ":
                left_position_empty = True
            elif board[y_end][x_end - length] == opp_color:
                left_position_empty = False

        #check right
        if x_end + 1 >= len(board[0]):
            right_position_empty = False
        elif board[y_end][x_end + 1] == opp_color:
            right_position_empty = False
        elif board[y_end][x_end + 1] == " ":
            right_position_empty = True

        if right_position_empty and left_position_empty:
            return "OPEN"
        elif not right_position_empty and not left_position_empty:
            return "CLOSED"
        else:
            return "SEMIOPEN"

    if d_y == 1 and d_x == 0: #top to bottom
        top_position_empty = False
        bottom_position_empty = False
        #check top
        if y_end - length >= 0:
            if board[y_end - length][x_end] == " ":
                top_position_empty = True
            elif board[y_end - length][x_end] == opp_color:
                top_position_empty = False

        #check bottom
        if y_end + 1 >= len(board):
            bottom_position_empty = False
        elif board[y_end + 1][x_end] == opp_color:
            bottom_position_empty = False
        elif board[y_end + 1][x_end] == " ":
            bottom_position_empty = True

        if bottom_position_empty and top_position_empty:
            return "OPEN"
        elif not bottom_position_empty and not top_position_empty:
            return "CLOSED"
        else:
            return "SEMIOPEN"

    if d_y == 1 and d_x == 1: #upper left to lower right
        upper_left_empty = False
        lower_right_empty = False
        #check upper left
        if y_end - length >= 0 and x_end - length >= 0:
            if board[y_end - length][x_end - length] == " ":
                upper_left_empty = True
            elif board[y_end - length][x_end - length] == opp_color:
                upper_left_empty = False
        #check lower right
        if y_end + 1 >= len(board) or x_end + 1 >= len(board[0]):
            lower_right_empty = False
        elif board[y_end + 1][x_end + 1] == opp_color:
            lower_right_empty = False
        elif board[y_end + 1][x_end + 1] == " ":
            lower_right_empty = True

        if upper_left_empty and lower_right_empty:
            return "OPEN"
        elif not upper_left_empty and not lower_right_empty:
            return "CLOSED"
        else:
            return "SEMIOPEN"

    if d_y == 1 and d_x == -1: #upper right to lower left
        upper_right_empty = False
        lower_left_empty = False
        #check upper right
        if y_end - length >= 0 and x_end + length < len(board[0]):
            if board[y_end - length][x_end + length] == " ":
                upper_right_empty = True
            elif board[y_end - length][x_end + length] == opp_color:
                upper_right_empty = False
        #check lower right
        if y_end + 1 >= len(board) or x_end - 1 < 0:
            lower_left_empty = False
        elif board[y_end + 1][x_end - 1] == opp_color:
            lower_left_empty = False
        elif board[y_end + 1][x_end - 1] == " ":
            lower_left_empty = True

        if upper_right_empty and lower_left_empty:
            return "OPEN"
        elif not upper_right_empty and not lower_left_empty:
            return "CLOSED"
        else:
            return "SEMIOPEN"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x, count_close = False):
   
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
    open_seq_count = 0
    semi_open_seq_count = 0
    close_seq_count = 0

    col_position = []

    y = y_start
    x = x_start

    # Collect positions of stones with the specified color
    while 0 <= y < len(board) and 0 <= x < len(board[0]):

        if board[y][x] == col:
            col_position.append([y, x])

        y += d_y
        x += d_x

    if len(col_position) == 0:
        if count_close:
            return open_seq_count, semi_open_seq_count, close_seq_count
        else:
            return open_seq_count, semi_open_seq_count

    count = 1

    # Count consecutive stones
    for i in range(1, len(col_position)):
        if (col_position[i][0] == col_position[i - 1][0] + d_y and col_position[i][1] == col_position[i - 1][1] + d_x):
            count += 1
        else:
            if count == length:
                status = is_bounded(board, col_position[i - 1][0], col_position[i - 1][1], length, d_y, d_x)
                if status == "OPEN":
                    open_seq_count += 1
                elif status == "SEMIOPEN":
                    semi_open_seq_count += 1
                else:
                    close_seq_count += 1

            count = 1

    # Check the last sequence
    if count == length:
        status = is_bounded(board, col_position[-1][0], col_position[-1][1], length, d_y, d_x)
        if status == "OPEN":
            open_seq_count += 1
        elif status == "SEMIOPEN":
            semi_open_seq_count += 1
        else:
            close_seq_count += 1

    if count_close:
        return open_seq_count, semi_open_seq_count, close_seq_count
    else:
        return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length, count_close = False):
    '''This function analyses the board board. The function returns a tuple, whose first element is the
number of open sequences of colour col of length length on the entire board, and whose
second element is the number of semi-open sequences of colour col of length length on the
entire board.
Only complete sequences count. For example, Fig. 1 is considered to contain one open row of
length 3, and no other rows.
Assume length is an integer greater or equal to 2.'''
    if length == 1:
        raise ValueError("length should be greater than 1")
    
    open_seq_count, semi_open_seq_count, close_seq_count = 0, 0, 0

    top_edge_points = [[0,0]]
    edge_points = []
    top_possible_delta = [[1,0], [1,1], [1,-1]]
    possible_delta = [[0,1], [1,1], [1,-1]]

    for i in range(1, len(board)):
        top_edge_points.append([0,i])
        edge_points.append([i,len(board)-1])
        edge_points.append([i,0])

    for i in edge_points:
        for j in possible_delta:
            a = detect_row(board, col, i[0], i[1], length, j[0], j[1], True)
            open_seq_count, semi_open_seq_count, close_seq_count += a[0], a[1], a[2]

    for i in top_edge_points:
        for j in top_possible_delta:
            a = detect_row(board, col, i[0], i[1], length, j[0], j[1], True)
            open_seq_count, semi_open_seq_count, close_seq_count += a[0], a[1], a[2]

    a = detect_row(board, col, 0, 0, length, 0, 1, True)
    open_seq_count, semi_open_seq_count, close_seq_count += a[0], a[1], a[2]

    if count_close:
        return open_seq_count, semi_open_seq_count, close_seq_count
    else:
        return open_seq_count, semi_open_seq_count
    
def search_max(board):
    '''This function uses the function score() (provided) to find the optimal move for black. It finds
the location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes
the score of the board as calculated by score(). The function returns a tuple (y, x) such
that putting a black stone in coordinates (y, x) maximizes the potential score (if there are
several such tuples, you can return any one of them). After the function returns, the contents of
board must remain the same.'''
    maxx = -99999999999999
    coord = (-1, -1)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                board[i][j] = 'b'
                a = score(board)
                if a>maxx:
                    maxx = a
                    coord = (i, j)
                board[i][j] = ' '

    return coord

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
    if sum(detect_rows(board, 'w', 5, True)) > 0 \
        or sum(detect_rows(board, 'w', 6, True)) > 0 \
        or sum(detect_rows(board, 'w', 7, True)) > 0 \
        or sum(detect_rows(board, 'w', 8, True)) > 0:
        return "White won"
    if sum(detect_rows(board, 'b', 5, True)) > 0 \
        or sum(detect_rows(board, 'b', 6, True)) > 0 \
        or sum(detect_rows(board, 'b', 7, True)) > 0 \
        or sum(detect_rows(board, 'b', 8, True)) > 0:
        return "Black won"

    for i in board:
        for j in i:
            if j == ' ':
                return "Continue playing"

    return "Draw"

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


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


if __name__ == '__main__':
    play_gomoku(8)
    
