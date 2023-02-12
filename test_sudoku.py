import pytest
from sudoku import num_has_row_copy

def test_number_with_a_row_copy_is_caught():
    faulty_grid = [
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

    assert num_has_row_copy((0,1), faulty_grid)
    assert num_has_row_copy((0,8), faulty_grid)
    assert num_has_row_copy((4,3), faulty_grid)
    assert num_has_row_copy((4,8), faulty_grid)
