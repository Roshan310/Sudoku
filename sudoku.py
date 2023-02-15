"""Simulates a game of Sudoku"""

import csv
import random
from sudoku_utils import build_puzzle_solution_pair
from typing import List, Tuple


def get_quiz_and_solution_line(filename: str) -> Tuple[str, str]:     
    """Returns a Tuple containing quiz and solution for the Sudoku game. """

    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        quiz_and_soln = [row for row in csv_reader]
        solution = random.choices(quiz_and_soln)
        grid_soln = solution[0]['solutions']
        grid_question = solution[0]['quizzes']
    
    return (grid_question, grid_soln)

# fmt: off
# blank numbers are represented as ' '
line = get_quiz_and_solution_line('pre-solved-sudokus.txt')
grid, grid_complete = build_puzzle_solution_pair(line)

# grid = [
#     [' ', '6', ' ', '8', ' ', ' ', '5', ' ', ' '],
#     [' ', ' ', '5', ' ', ' ', ' ', '3', '6', '7'],
#     ['3', '7', ' ', ' ', '6', '5', '8', ' ', '9'],
#     ['6', ' ', '9', ' ', ' ', '2', '1', ' ', ' '],
#     [' ', ' ', '1', '4', '8', '9', '2', ' ', ' '],
#     [' ', ' ', ' ', '3', ' ', '6', '9', ' ', ' '],
#     [' ', '5', ' ', ' ', ' ', ' ', '4', ' ', ' '],
#     [' ', '1', ' ', '5', '4', '7', ' ', ' ', '3'],
#     [' ', '9', '6', ' ', '3', '8', ' ', ' ', '1'],
# ]
# fmt: on

board_state = []


def num_has_row_copy(loc: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Returns True if the number in `loc` location in the `grid` has a duplicate in the same row as it.
    Returns False otherwise.

    The `loc` (0, 1) refers to the second number (index 1) of the first row (index 0) in the `grid`.
    """
    row, index = loc[0], loc[1]
    this_num = grid[row][index]

    # get numbers to the left and right of this number
    left_nums = grid[row][0:index]
    right_nums = grid[row][index + 1 :]

    return this_num in left_nums or this_num in right_nums


def num_has_column_copy(loc: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Returns True if the number in `loc` location in the `grid` has a duplicate in the same column as it.
    Returns False otherwise.

    The `loc` (0, 1) refers to the second number (index 1) of the first row (index 0) in the `grid`.
    """

    _row, _col = loc
    this_num = grid[_row][_col]

    #Get numbers from the current column
    column_nums = [grid[row][_col] for row in range(len(grid))]

    #Delete the number that is being checked from the column
    del column_nums[column_nums.index(this_num)]
    return this_num in column_nums


def num_has_sub_grid_copy(loc: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Returns True if the number in `loc` location in the `grid` has a duplicate in the same 3 X 3 sub-grid.
    Returns False otherwise.

    The `loc` (0, 1) refers to the second number (index 1) of the first row (index 0) in the `grid`.
    """
    row, col = loc
    this_num = grid[row][col]
    if row in (1, 4, 7):
        row -= 1
    elif row in (2, 5, 8):
        row -= 2

    if col in (1, 4, 7):
        col -= 1
    elif col in (2, 5, 8):
        col -= 2
    count = 0
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if this_num == grid[i][j]:
                count += 1

    return True if count > 1 else False


def make_move(loc: Tuple[int, int], number: int, grid: List[List[str]]) -> None:
    """Places the `number` at `loc` location in the `grid`"""
    row, col = loc

    #Check if the desired location is empty or not
    if grid[row][col] == " ":
        grid[row][col] = str(number)
        board_state.append((loc, number))
  
def undo_move(grid: List[List[str]]):
    """Undoes a move made by the player."""

    #Check if the player has made any previous move or not
    if len(board_state) < 1:
        print("You haven't made a move yet!")
        return

    #Get the last location and number the player placed the move in grid
    loc, number = board_state.pop()
    row, col = loc
    grid[row][col] = " "


def sudoku_is_solved(grid: List[List[str]]) -> bool:
    """Returns True if the sudoku has been solved.
    Returns False otherwise.
    """
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == " ":
                return False
            elif (
                num_has_row_copy((row, col), grid)
                or num_has_column_copy((row, col), grid)
                or num_has_sub_grid_copy((row, col), grid)
            ) == True:
                return False

    return True


def get_a_hint(grid: List[List[str]]):
    """Gives the player a hint, by revealing one or more numbers in the unsolved Sudoku."""
    
    row, col, number = get_loc_and_number_for_hint(grid, grid_complete)
    make_move((row, col), number, grid)


def get_sudoku_grid(grid: List[List[str]]) -> str:
    """Returns the sudoku grid, as a standard sudoku"""

    sudoku_grid = """
        1   2   3   4   5   6   7   8   9
      ╔━━━┯━━━┯━━━╦━━━┯━━━┯━━━╦━━━┯━━━┯━━━╗
    A ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ A
      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    B ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ B
      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    C ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ C
      ┣━━━┿━━━┿━━━╬━━━┿━━━┿━━━╬━━━┿━━━┿━━━┫
    D ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ D
      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    E ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ E
      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    F ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ F
      ┣━━━┿━━━┿━━━╬━━━┿━━━┿━━━╬━━━┿━━━┿━━━┫
    G ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ G
      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    H ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ H
      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    I ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ I
      ╚━━━┷━━━┷━━━╩━━━┷━━━┷━━━╩━━━┷━━━┷━━━╝
        1   2   3   4   5   6   7   8   9
    """.format(
        *[cell for row in grid for cell in row]
    )

    return sudoku_grid


def get_loc_and_number_for_hint(grid_incomplete, grid_complete):
    """Returns the location and number for the hint """

    loc_and_num = []
    quiz_and_soln = [(row1, row2) for row1, row2 in zip(grid_incomplete, grid_complete)]
    hint_soln = random.choice(quiz_and_soln)
    print(hint_soln)
    quiz, soln = hint_soln
    for row in range(9):
        if grid_complete[row] == hint_soln[1]:
            loc_and_num.append(row)
            break
    for num1, num2 in zip(quiz, soln):
        if num1 != num2:
            loc_and_num.append(soln.index(num2))
            loc_and_num.append(num2)
            break

    return loc_and_num
