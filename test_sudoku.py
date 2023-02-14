import pytest
from sudoku import make_move, num_has_row_copy
from sudoku_utils import translate_move, SudokuError


def test_number_with_a_row_copy_is_caught():
    faulty_grid = [
    [' ', '6', ' ', '8', ' ', ' ', '5', ' ', '6'],
    [' ', ' ', '5', ' ', ' ', ' ', '3', '6', '7'],
    ['3', '7', ' ', ' ', '6', '5', '8', ' ', '9'],
    ['6', ' ', '9', ' ', ' ', '2', '1', ' ', ' '],
    [' ', ' ', '1', '4', '8', '9', '2', ' ', '4'],
    [' ', ' ', ' ', '3', ' ', '6', '9', ' ', ' '],
    [' ', '5', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    [' ', '1', ' ', '5', '4', '7', ' ', ' ', '3'],
    [' ', '9', '6', ' ', '3', '8', ' ', ' ', '1'],
]

    assert num_has_row_copy((0, 1), faulty_grid)
    assert num_has_row_copy((0, 8), faulty_grid)
    assert num_has_row_copy((4, 3), faulty_grid)
    assert num_has_row_copy((4, 8), faulty_grid)


@pytest.mark.parametrize(
    'coordinate_moves, actual_moves',
    [
        ('2A1', ((0, 0), 2)),
        ('21a', ((0, 0), 2)),
        ('7i3', ((8, 2), 7)),
        ('6E8', ((4, 7), 6)),
        ('68e', ((4, 7), 6)),
    ],
)
def test_coordinates_are_translated_into_moves(coordinate_moves, actual_moves):
    assert actual_moves == translate_move(coordinate_moves)


def test_coordinates_that_are_longer_or_shorter_than_expected_are_caught():
    expected_message = 'Coordinate is invalid.\nThe legal format is <number><row number><column letter> or <number><column letter><row number>'
    with pytest.raises(SudokuError, match=expected_message):
        translate_move('1I89')
        translate_move('21a4')
        translate_move('1a4')


def test_invalid_sudoku_number_in_coordinate_is_caught():
    with pytest.raises(SudokuError, match='Only numbers from 1 to 8 can be placed into the grid.'):
        translate_move('0A1')
        translate_move('#E8')


def test_invalid_row_in_coordinate_is_caught():
    with pytest.raises(SudokuError, match='Only row letters from A to I are allowed.'):
        translate_move('2J3')
        translate_move('89R')


def test_invalid_column_in_coordinate_is_caught():
    with pytest.raises(SudokuError, match='Only column numbers from 1 to 9 are allowed.'):
        translate_move('3A0')
        translate_move('80I')

