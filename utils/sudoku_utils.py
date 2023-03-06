"""General utility functions for the Sudoku grid"""

from typing import Tuple, List

LEGAL_COORDINATE_LENGTH = 3
VALID_COLS = {1, 2, 3, 4, 5, 6, 7, 8, 9}
VALID_ROWS = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}


class SudokuError(Exception):
    """General exception class for the Sudoku game"""

    def __init__(self, message='Something went wrong. Please try again') -> None:
        self.error_message = message
        super().__init__(self.error_message)


def translate_move(coordinate_move: str) -> Tuple[Tuple[int, int], int]:
    """Returns a tuple that is the result of translating Sudoku coordinates into moves.

    The coordinate_move `9a8` or `9A8` or `98a` or `98A` asks to place a `9` in the intersection between
    row `A` and column `8`.

    The tuple ((0, 7), 9) will be returned, where the first tuple (0, 7) denotes row `0`, column `7`, and the last number
    denotes the `9` that will be placed in that location.
    """
    # rows that each letter corresponds to
    letter_rows = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

    if not len(coordinate_move) == LEGAL_COORDINATE_LENGTH:
        raise SudokuError(
            'Coordinate is invalid. The legal format is:\n<number><row number><column letter> or\n<number><column letter><row number>'
        )

    if not (coordinate_move[0].isdecimal() and 1 <= int(coordinate_move[0]) <= 9):
        raise SudokuError('Only numbers from 1 to 9 can be placed into the grid.')

    number = int(coordinate_move[0])

    if coordinate_move[1].isdecimal():  # the numeric column was provided first
        column = int(coordinate_move[1])

        if column not in VALID_COLS:
            raise SudokuError('Only column numbers from 1 to 9 are allowed.')

        row = str(coordinate_move[2]).upper()

        if not (row.isalpha() and row in VALID_ROWS):
            raise SudokuError('Only row letters from A to I are allowed.')

        return ((letter_rows[row], column - 1), number)

    else:  # the alphabetical row was provided first
        _row = coordinate_move[1].upper()

        if not _row in VALID_ROWS:
            raise SudokuError('Only row letters from A to I are allowed.')
        else:
            _column = coordinate_move[2]
            if not (_column.isdigit() and int(_column) in VALID_COLS):
                raise SudokuError('Only column numbers from 1 to 9 are allowed.')

            return ((letter_rows[_row], int(_column) - 1), number)


def build_puzzle_solution_pair(line: Tuple) -> Tuple[List[List[str]], List[List[str]]]:
    """Builds and returns a pair of the Sudoku puzzle and its solution, as a result of parsing the comma-separated `line`
    representations of the puzzle and the solution respectively.
    """
    puzzle_repr, solution_repr = line
    puzzle = build_grid(puzzle_repr)
    solution = build_grid(solution_repr)

    return (puzzle, solution)


def build_grid(line: str) -> List[List[str]]:
    """Builds and returns a sudoku grid, which is a result of parsing the provided `line` representation of that grid."""
    ROW_LENGTH = 9
    grid: List[List[str]] = []
    single_row = []

    for char in line:
        char = ' ' if char == '0' else char  # replace every 0 with an empty space
        single_row.append(char)
        if len(single_row) == ROW_LENGTH:  # prepare to build the next row
            grid.append(single_row)
            single_row = []
    return grid
