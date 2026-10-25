"""
// project: 3x3 board with 9 boards total, that is well sudoku.
// initated: 10/21/2026
//Dev: FireRose


// What we working with:
/*
- integers: 1-9
- Around 9 (3x3 boards)
*/

// Rules for Sudoku:
/*
1) For each number, we have to make sue that there is no dupes within:
    a) The same row 
    b) The same column
    c) And the 3x3 board itself
    *NOTE: DIAGONALS DO NOT MATTER*
2. WE have to put some numbers in the board!
    a) Range: 17 <= n <= 30
    b) make sure the number follow the same logic as Rule #1 to have a proper board initalized with n-th integers
*/

// The board itself
/*
- An array of 3x3 boards with some proper integers initalized
    - Each 3x3 board can have at least 1-5 integers already in position
    - This means we have to check the given integers positions to make sure it is supposed to be there!
- Use ASCII art to have a nice looking board design + show numbers too!

*/

// Checking board to see if they win or lose a try
/*
- If all the numbers are in their UNIQUE position, then the user wins!
    - If there is a valid number there, don't do anything to that.
- If the user runs out of tries, they a try
    - If all tries given reach 0, end the game and say they lost

*/
// Player losing: The player is given 5 tries to solve the entire soduku puzzle and if we reach 0, they have lost!
// Player winning: The entire board itself is filled with the proper numbers 


TODOS:
1) Create an initalizer of random int (1-9) to put in each valid position
2) Have a checker to see if player has won game
3) Debug
"""

import ASCII_ART


def check_row_col_position(row: int, col: int) -> bool:
    if (row < 0 or row > 8) and (col < 0 or col > 8):
        return False
    return True

def check_user_number_input(number: int) -> bool:
    if number <= 0 or number > 9:
        return False
    return True

def initalize_board() -> list[list[str]]:
    # initalize with '-' to indicate empty space:
    board = [["0" for _ in range(9)] for _ in range(9)] # initalizes the sudoku board that consist of 9x9 matrix over all
    return board

# note: board --> board[i][j]

def check_sudoku_board_row(board, row, col, number) -> bool:
    for j in range(9):
        if board[row][j] == number and j != col:
            return False # Invalid move since we had found an element before we reach a col
    return True # Valid for the row

def check_sudoku_board_col(board, row, col, number) -> bool:
    for i in range(9):
        if board[i][col] == number and i != col:
            return False # Invalid move since we had found elemnent from one of the columns
    return True # Valid for the column



def check_single_board_check(board, row, col, number) -> bool:
    # Group specified indices since we are 9x9 board
    flag = False # boolean var to hold any of the cases and return at the end of function
    if (row >= 0 and col >= 0) and (row <= 2 and col <= 2):
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == number and (i != row and j != col):
                    continue
        flag = True # 3x3 case is true!
    elif (row > 2 and col > 2) and (row <= 5 and col <= 5):
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] == number and (i != row and j != col):
                    continue
        flag = True # 3x3 case is true!
    elif (row > 5 and col > 5) and (row <= 8 and col <= 8):
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] == number and (i != row and j != col):
                    continue
        flag = True
    return flag


def check_sudoku_board(board, row, col, number) -> bool:
    row_check = check_sudoku_board_row(board, row, col, number)
    col_check = check_sudoku_board_col(board, row, col, number)
    single_board_check = check_single_board_check(board, row, col, number)
    if row_check and col_check and single_board_check:
        return True # Player's number is valid!
    return False

# starting game
def start_game(name: str) -> bool:
    board = initalize_board()

    # TEST:
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    ASCII_ART.print_grid(board)
    tries = 5 # player has only 5 tries left to solve Sudoku Puzzle
    while(True):
        number = int(input("Choose a number between (1-9): "))
        if check_user_number_input(number):
            row = int(input("What row will you like to pick?(0-8): "))
            col = int(input("What column will you like to pick?(0-8): "))
            if not check_row_col_position(row, col):
                continue # if user puts an invalid position 
            if not check_sudoku_board(board, row, col, number):
                print("WRONG!")
                ASCII_ART.print_grid(board)
                tries -= 1 # user got the sudoku puzzle wrong!
                continue
            else:
                board[row][col] = str(number) # place number
                ASCII_ART.print_grid(board)
            
        else:
            print("Invalid number!") 
            continue

        
        


def main():
    print("Hello! Welcome to Sudoku! Enter your name: ")
    name = input()
    output = f"Congrats {name}!! You have won!" if start_game(name) else f"{name} has LOST!"
    print(output)



if __name__ == "__main__":
    # board = [
    # [5, 3, 0, 0, 7, 0, 0, 0, 0],
    # [6, 0, 0, 1, 9, 5, 0, 0, 0],
    # [0, 9, 8, 0, 0, 0, 0, 6, 0],
    # [8, 0, 0, 0, 6, 0, 0, 0, 3],
    # [4, 0, 0, 8, 0, 3, 0, 0, 1],
    # [7, 0, 0, 0, 2, 0, 0, 0, 6],
    # [0, 6, 0, 0, 0, 0, 2, 8, 0],
    # [0, 0, 0, 4, 1, 9, 0, 0, 5],
    # [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]

    # ASCII_ART.print_grid(board)
    main()