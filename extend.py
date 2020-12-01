import random
from random import randint

def sudoku_generator():
    puzzle = []

    for i in range(0, 9):
        col = []
        for j in range(0, 9):
            col.append(0)
        puzzle.append(col)

    for i in range(0, 11):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        val = random.randint(0, 9)
        if is_valid(val, puzzle, row, col):
            puzzle[row][col] = val

    sudoku_solver(puzzle)

    for i in range(0, 70):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle

def sudoku_solver(puzzle):
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == 0:
                for val in range(1, 10):
                    if is_valid(val, puzzle, row, col):
                        puzzle[row][col] = val
                        
                        if is_solved(puzzle):
                            return True
                        else:
                            sudoku_solver(puzzle)
                
                if not is_solved(puzzle):
                    puzzle[row][col] = 0
                    return False
    return True


def is_solved(puzzle):
    for row in puzzle:
        for cell in row:
            if cell == 0:
                return False
    return True


def is_valid(val, puzzle, row, col):
    for i in range(0, 9):
        if puzzle[row][i] == val or puzzle[i][col] == val:
            return False
    
    rows = int(row / 3) * 3
    cols = int(col / 3) * 3
    
    for i in range(rows, rows + 3):
        for j in range(cols, cols + 3):
            if puzzle[i][j] == val:
                return False
    return True
