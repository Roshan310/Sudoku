"""Simulates a game of Sudoku"""

from typing import List, Tuple

# fmt: off
# blank numbers are represented as '.'
grid = [
    '.6.8..5.6',
    '..5...367',
    '37..658.9',
    '6.9..21..',
    '..14892.4',
    '...3.69..',
    '.5....4..',
    '.1.547..3',
    '.96.38..1',
]
# fmt: on


def num_has_row_copy(loc: Tuple[int, int], grid: List[str]) -> bool:
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


def num_has_column_copy(loc: Tuple[int, int], grid: List[str]) -> bool:
    """Returns True if the number in `loc` location in the `grid` has a duplicate in the same column as it.
    Returns False otherwise.

    The `loc` (0, 1) refers to the second number (index 1) of the first row (index 0) in the `grid`.
    """
    return True  # TODO


def num_has_cell_copy(loc: Tuple[int, int], grid: List[str]) -> bool:
    """Returns True if the number in `loc` location in the `grid` has a duplicate in the same cell.
    Returns False otherwise.

    The `loc` (0, 1) refers to the second number (index 1) of the first row (index 0) in the `grid`.
    """
    return True  # TODO


def undo_move():
    """Undoes a move made by the player."""
    # TODO

def sudoku_is_solved() -> bool:
    """Returns True if the sudoku has been solved. 
    Returns False otherwise.
    """
    return True # TODO

def get_a_hint(grid: List[str]):
    """Gives the player a hint, by revealing one or more numbers in the unsolved Sudoku."""
    # TODO

def get_sudoku_grid(grid: List[str]) -> str:
    """Returns the sudoku grid, as a standard sudoku"""

    sudoku_grid = """
    ╔━━━┯━━━┯━━━╦━━━┯━━━┯━━━╦━━━┯━━━┯━━━╗
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┣━━━┿━━━┿━━━╬━━━┿━━━┿━━━╬━━━┿━━━┿━━━┫
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┣━━━┿━━━┿━━━╬━━━┿━━━┿━━━╬━━━┿━━━┿━━━┫
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
    ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
    ╚━━━┷━━━┷━━━╩━━━┷━━━┷━━━╩━━━┷━━━┷━━━╝
    """.format(
        *[cell for row in grid for cell in row]
    )

    return sudoku_grid
