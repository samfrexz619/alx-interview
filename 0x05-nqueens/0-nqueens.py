#!/usr/bin/python3
"""
   Description: The N queens puzzle is the challenge of placing N non-attacking
                queens on an N×N chessboard. Write a program that solves the N
                queens problem.
"""


import sys


def is_safe(board, row, col, n):
    ''' '''
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check if there is a queen in the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    if col == n:
        # All queens are placed, print the solution
        print_solution(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0  # backtrack


def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def nqueens_solver(n):
    # Initialize the chessboard with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]

    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Parse the command-line argument as an integer
        n = int(sys.argv[1])

        # Check if N is greater than or equal to 4
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        nqueens_solver(n)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
