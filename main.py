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
- Use ASCII art to have a nice looking board design + show numbers too!

*/

// Checking board to see if they win or lose a try
/*
- If all the numbers are in their UNIQUE position, then the user wins!
- If the user runs out of tries, they a try
    - If all tries given reach 0, end the game and say they lost

*/


// Player losing: The player is given 5 tries to solve the entire soduku puzzle and if we reach 0, they have lost!
// Player winning: The entire board itself is filled with the proper numbers 

"""

import ASCII_ART

def check_user_number_input(number: int) -> bool:
    if number <= 0 or number > 9:
        return False
    return True


def start_game(name: str) -> bool:
    while(True):
        number = int(input("Choose a number between (1-9): "))
        if check_user_number_input(number):
            print("working!")
                

        
        


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

    ASCII_ART.print_grid(board)
    main()