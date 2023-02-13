# Sudoku

A simulation of a standard game of Sudoku with a `9 X 9` grid, with `3 X 3` sub-grids.
\
The goal is to fill each sub-grid with numbers 1-9 such that no number repeats.
\
Likewise, no number should be repeated in its own row or column.
And no number should be repeated in its sub-grid too.
\
\
A sample grid in the game is represented here, with some cells filled and some empty.

```sh
    1   2   3   4   5   6   7   8   9
  ┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓
A ┃   │ 6 │   ┃ 8 │   │   ┃ 5 │   │   ┃ A
  ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
B ┃   │   │ 5 ┃   │   │   ┃ 3 │ 6 │ 7 ┃ B
  ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
C ┃ 3 │ 7 │   ┃   │ 6 │ 5 ┃ 8 │   │ 9 ┃ C
  ┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
D ┃ 6 │   │ 9 ┃   │   │ 2 ┃ 1 │   │   ┃ D
  ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
E ┃   │   │ 1 ┃ 4 │ 8 │ 9 ┃ 2 │   │   ┃ E
  ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
F ┃   │   │   ┃ 3 │   │ 6 ┃ 9 │   │   ┃ F
  ┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
G ┃   │ 5 │   ┃   │   │   ┃ 4 │   │   ┃ G
  ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
H ┃   │ 1 │   ┃ 5 │ 4 │ 7 ┃   │   │ 3 ┃ H
  ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
I ┃   │ 9 │ 6 ┃   │ 3 │ 8 ┃   │   │ 1 ┃ I
  ┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛
    1   2   3   4   5   6   7   8   9
```
