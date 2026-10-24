
# print_grid function borrowed from: https://stackoverflow.com/questions/67441895/how-to-print-sudoku-grid-more-efficiently
def print_grid(board):
    print("-------------------------")
    for row_num, row in enumerate(board):
        print("|", end=" ")
        for col_num, item in enumerate(row):
            print(item if item != 0 else '-', end=" ")
            if (col_num + 1) % 3 == 0:
                print("|", end=" ")
        print()
    
        if(row_num + 1) % 3 == 0:
            print("-------------------------")
