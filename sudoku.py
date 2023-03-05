"""Simulates a game of Sudoku"""
from colorama import Fore, Back
import csv
import random
import ui
from rich import print as rprint
from sudoku_utils import build_puzzle_solution_pair, translate_move, SudokuError
import sys
from textwrap import dedent
from typing import List, Tuple
from pathlib import Path

board_state: List[Tuple[Tuple[int, int], int]] = []


def main():
    ui.show_game_instructions()
    print(Fore.CYAN)
    print(Back.BLUE)

    try:
        if prompt_to_continue() == 'q':
            sys.exit('Goodbye!')
    except (KeyboardInterrupt, EOFError):
        sys.exit('Goodbye!')
    ui.clear_screen()

    presolved_puzzles = Path('puzzle-dataset', 'pre-solved-sudokus.txt')
    print(presolved_puzzles)
    line = get_quiz_and_solution_line(str(presolved_puzzles))
    grid, solution = build_puzzle_solution_pair(line)
    rprint(ui.vertical_split(ui.get_sudoku_grid(grid), ui.explain_coordinate_system()))

    try:
        if prompt_to_continue() == 'q':
            sys.exit('Goodbye!')
        ui.clear_screen()
    except (KeyboardInterrupt, EOFError):
        sys.exit('Goodbye!')

    rprint(ui.vertical_split(ui.get_sudoku_grid(grid), ui.get_game_keys()))

    game_key_func = {
        'u': 'undo_move(grid)',
        'h': 'get_a_hint(grid, solution)',
    }

    while True:
        try:
            prompt = input('Enter move, or other game key (q to quit)\n> ').strip().lower()
        except (KeyboardInterrupt, EOFError):
            sys.exit('Goodbye!')

        if prompt in (tuple(ui.GAME_KEYS.values())):  # a game key was entered
            eval(game_key_func[f'{prompt}'])
        else:
            if prompt == 'q':
                sys.exit('Goodbye!')
            try:
                location, number = translate_move(prompt)
                make_move(location, number, grid)
            except SudokuError as e:
                ui.clear_screen()
                rprint(ui.vertical_split(ui.get_sudoku_grid(grid), ui.get_game_keys()))
                rprint(f'[bold red]{e.error_message}')
                continue
        ui.clear_screen()
        rprint(ui.vertical_split(ui.get_sudoku_grid(grid), ui.get_game_keys()))


def prompt_to_continue() -> str:
    """Returns the input that the user entered when prompted to continue.

    The user is re-prompted if they enter an invalid choice.
    """
    while True:
        prompt = input('Enter y to continue, q to quit\n> ').strip().lower()
        if prompt in ('y', 'q'):
            break
        else:
            print('Unknown choice. Try again!')
    return prompt


def get_quiz_and_solution_line(filename: str) -> Tuple[str, str]:
    """Returns a Tuple containing quiz and solution for the Sudoku game."""

    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        quiz_and_soln = [row for row in csv_reader]
        solution = random.choice(quiz_and_soln)
        grid_soln = solution['solutions']
        grid_question = solution['quizzes']

    return (grid_question, grid_soln)


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
    # unpacks the row and col from the `loc` tuple
    _row, _col = loc
    this_num = grid[_row][_col]

    # Get numbers from the current column
    column_nums = [grid[row][_col] for row in range(len(grid))]

    # Delete the number that is being checked from the column
    del column_nums[column_nums.index(this_num)]

    # returns True if the number is in the column else returns False
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

    # Check if the desired location is empty or not
    if grid[row][col] == " ":
        grid[row][col] = str(number)

        # Add the current location and number to the board_state list after each move.
        # This makes it easier to undo the last move later on.
        board_state.append((loc, number))
    else:
        print("There's a number already in that position!!")


def undo_move(grid: List[List[str]]):
    """Undoes a move made by the player."""

    # Check if the player has made any previous move or not
    if len(board_state) < 1:
        print("You haven't made a move yet!")
        return

    # Get the last location and number from the board_state list.
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


def get_a_hint(grid_incomplete: List[List[str]], grid_complete: List[List[str]]) -> None:
    """Gives the player a hint, by revealing one or more numbers in the unsolved Sudoku."""

    row, col, number = get_loc_and_number_for_hint(grid_incomplete, grid_complete)
    make_move((row, col), number, grid_incomplete)


def get_loc_and_number_for_hint(grid_incomplete, grid_complete):
    """Returns the location and number for the hint"""

    loc_and_num = []
    quiz_and_soln = [(row1, row2) for row1, row2 in zip(grid_incomplete, grid_complete)]
    hint_soln = random.choice(quiz_and_soln)
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


if __name__ == '__main__':
    main()
