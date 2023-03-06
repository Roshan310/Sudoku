"""Utility functions for the user interface of the game"""

from rich.table import Table, box
from rich import print as rprint
from typing import List
from textwrap import dedent
import os


GAME_KEYS = {'undo': 'u', 'hint': 'h'}


def clear_screen() -> None:
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_sudoku_and_keys(grid: List[List[str]]) -> Table:
    """Returns the sudoku grid and the list of possible game keys to enter, side-by-side."""
    return split_left_right(get_sudoku_grid(grid), get_game_keys(), outer_edge=False)


def get_info(message: str = "") -> Table:
    """Returns the `info` section of the game UI.
    This section is reserved for errors, and other useful texts.
    """
    return split_left_right('info', message, outer_edge=False)


def get_game_keys() -> Table:
    """Shows possible keys that the user can press in the game."""
    keys = Table(show_header=False, show_lines=False, title='game keys:', show_edge=False)
    keys.add_column()
    keys.add_row()  # for additional vertical spacing
    keys.add_row('\n'.join(f'{v}: {k} ' for k, v in GAME_KEYS.items()))
    return keys


def split_left_right(left_element, right_element, outer_edge=True) -> Table:
    """Returns a rich table with the `left_element` on the left of the table,
    and the `right_element` on the right of the table.
    """
    UI = Table(show_header=False, show_edge=outer_edge, box=box.ROUNDED)
    UI.add_column(no_wrap=True)
    UI.add_column(no_wrap=True)
    UI.add_row(left_element, right_element)
    return UI


def split_up_down(top_element, bottom_element, outer_edge=True) -> Table:
    """Returns a rich table with the `top_element` at the top of the table,
    and the `bottom_element` at the bottom of the table.
    """
    UI = Table(show_header=False, show_edge=outer_edge, box=box.ROUNDED)
    UI.add_column(no_wrap=True)
    UI.add_row(top_element, end_section=True)
    UI.add_row(bottom_element, end_section=True)
    return UI


def explain_coordinate_system() -> str:
    explanation = dedent(
        """You place numbers by typing: 
1) The number you want to place,
2) Where in the grid to place.

9A3 places 9 in location A3 of the grid.
Entering 9a3 or 93a or 93A does the same thing.

Incorrect numbers, or locations are rejected."""
    )

    return explanation


def get_sudoku_grid(grid: List[List[str]]) -> str:
    """Returns the sudoku grid, as a standard sudoku"""

    sudoku_grid = dedent(
        """    1   2   3   4   5   6   7   8   9
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
    1   2   3   4   5   6   7   8   9"""
    ).format(*[cell for row in grid for cell in row])

    return sudoku_grid


def show_game_instructions() -> None:
    """Prints the game's instructions"""
    banner = dedent(
        """    
    ███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗
    ██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║
    ███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║
    ╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║
    ███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝
    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
    """
    )
    instructions_text = dedent(
        """
    The game consists of a large 9 X 9 grid of cells,
    with smaller 3 X 3 sub-grids.

    You win if you fill in the cells with numbers 1 to 9,
    such that:

    + No number is repeated in a sub-grid
    + No number is repeated in its own row
    + No number repeats in its own column
    """
    )
    instructions = Table(show_header=False, show_lines=False)
    instructions.add_column()
    instructions.add_row(instructions_text)
    print(banner)
    rprint(instructions)
