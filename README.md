# Sudoku

A simulation of a standard game of Sudoku with a `9 X 9` grid, with `3 X 3` sub-grids.
\
The goal is to fill each sub-grid with numbers 1-9 such that no number repeats.
\
Likewise, no number should be repeated in its own row or column.
\
\
A sample grid in the game is represented here, with some cells filled and some empty.

```sh
┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓
┃   │ 6 │   ┃ 8 │   │   ┃ 5 │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │ 5 ┃   │   │   ┃ 3 │ 6 │ 7 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 3 │ 7 │   ┃   │ 6 │ 5 ┃ 8 │   │ 9 ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃ 6 │   │ 9 ┃   │   │ 2 ┃ 1 │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │ 1 ┃ 4 │ 8 │ 9 ┃ 2 │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃ 3 │   │ 6 ┃ 9 │   │   ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃   │ 5 │   ┃   │   │   ┃ 4 │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │ 1 │   ┃ 5 │ 4 │ 7 ┃   │   │ 3 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │ 9 │ 6 ┃   │ 3 │ 8 ┃   │   │ 1 ┃
┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛
```
