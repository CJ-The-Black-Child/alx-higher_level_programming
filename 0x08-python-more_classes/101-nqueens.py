#!/usr/bin/python3
import sys

    def is_self(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col:
                return false
        # Check if there is a queen in the upper left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i] == j:
                return False
            i -= 1
            j -= 1
        # check if ther is a queen in the upper right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i] == j:
                return False
            i -= 1
            j += 1
        return True

    def solve_n_queens(n):
        board = [-1] * n 
    
    def place_queen(row):
        if row == n:
            print ([[i, board[i]] for i in range(n)])
            return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    place_queen(row + 1)
                    board[rw] = -1
        place_queen(0)

# Main Program
if __name__ == '__main__':
    # check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from command line argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens Problem
    solve_n_queens(n)

