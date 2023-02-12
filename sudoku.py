from copy import deepcopy

# fmt: off
grid = [
    ['4','9','7',
     '3','1','2',
     '5','6','4'],

    ['','9','',
     '6','8','7',
     '','1',''],

    ['3','','5',
     '','','4',
     '','','9'],

    ['4','7','',
     '1','6','2',
     '','','9'],
]
# fmt: on

cell_nums = set()

# check for duplicate in cell
for num in grid[0]:
    if num in cell_nums:
        print(f"There is a duplicate number {num}")
    else:
        cell_nums.add(num)


# check for duplicate in row
num_to_check = "4"

current_row = grid[0][0:3]
# print(current_row)
# print(current_row) #[9, 7]
first_row = grid[1][0:3]
second_row = grid[2][0:3]

print(first_row)
print(second_row)
for num in current_row:
    if num in current_row or num in first_row or num in second_row:
        print(f"A duplicate {num} was found in ...")

# check for duplicate in column
# ['4', '9', '7'] | ['', '9', ''] | ['3', '', '5'] | ['', '7', '']
