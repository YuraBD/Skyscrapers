'''
This module checks a board of skyscrapers game
 and returns True if it is correct and False if isn't

Github: https://github.com/YuraBD/Skyscrapers

This module has 7 functions:

1) read_input
Read game board file from path.
Return list of str.

2) left_to_right_check
Check row-wise visibility from left to right.
Return True if number of building from the left-most hint is visible looking to the right,
False otherwise.

input_line - representing board row.
pivot - number on the left-most hint of the input_line.
>>> left_to_right_check("412453*", 4)
True
>>> left_to_right_check("452453*", 4)
False

3) check_not_finished_board
Check if skyscraper board is not finished, i.e., '?' present on the game board.
Return True if finished, False otherwise.
>>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
                              '*?????5', '*?????*', '*?????*', '*2*1***'])
False
>>> check_not_finished_board(['***21**', '412453*', '423145*',\
                              '*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_not_finished_board(['***21**', '412453*', '423145*',\
                              '*5?3215', '*35214*', '*41532*', '*2*1***'])
False

4) check_uniqueness_in_rows
Check buildings of unique height in each row.
Return True if buildings in a row have unique length, False otherwise.
>>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
                              '*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
                              '*543215', '*35214*', '*41532*', '*2*1***'])
False
>>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
                              '*553215', '*35214*', '*41532*', '*2*1***'])
False

5) check_horizontal_visibility
Check row-wise visibility (left-right and vice versa)
Return True if all horizontal hints are satisfiable,
 i.e., for line 412453* , hint is 4, and 1245 are the four buildings
  wthat could be observed from the hint looking to the right.
>>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
                                 '*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
                                 '*543215', '*35214*', '*41532*', '*2*1***'])
False
>>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
                                 '*543215', '*35214*', '*41532*', '*2*1***'])
False

6) check_columns
Check column-wise compliance of the board for uniqueness (buildings of unique height)
 and visibility (top-bottom and vice versa).
Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.
>>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
False
>>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
False

7) check_skyscrapers
Main function to check the status of skyscraper game board.
Return True if the board status is compliant with the rules,
False otherwise.
'''

def read_input(path: str) -> list:
    """
    Read game board file from path.
    Return list of str.
    """
    board_file = open(path, 'r', encoding='UTF-8')
    board = [line.strip() for line in board_file.readlines()]
    return board


def left_to_right_check(input_line: str, pivot: int) -> bool:
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 4)
    False
    """
    line = list(map(int ,list(input_line[1:-1])))
    max_height = line[0]
    visibility = 1
    for building in line[1:]:
        if building > max_height:
            visibility += 1
            max_height = building
    if visibility == pivot:
        return True
    return False


def check_not_finished_board(board: list) -> bool:
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
                                  '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
                                  '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
                                  '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board[1:-1]:
        if '?' in row:
            return False
    return True


def check_uniqueness_in_rows(board: list) -> bool:
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
                                  '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
                                  '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
                                  '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    c_board = board.copy()
    for row in c_board[1:-1]:
        row = row[1:-1]
        while row:
            if row.count(row[0]) != 1:
                return False
            row = row.replace(row[0], '')
    return True


def check_horizontal_visibility(board: list) -> bool:
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
                                     '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
                                     '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
                                     '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board[1:-1]:
        if row[0] == '*':
            pass
        else:
            if not left_to_right_check(row, int(row[0])):
                return False
        r_row = row[::-1]
        if r_row[0] == "*":
            pass
        else:
            if not left_to_right_check(r_row, int(r_row[0])):
                return False
    return True


def check_columns(board: list) -> bool:
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
     and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    r_board = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            row.append(board[j][i])
        r_board.append(row)
    r_board = list(map(lambda row: ''.join(row), r_board))
    if not check_horizontal_visibility(r_board):
        return False
    if not check_uniqueness_in_rows(r_board):
        return False
    return True


def check_skyscrapers(input_path: str) -> bool:
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    if not check_horizontal_visibility(board) or\
       not check_uniqueness_in_rows(board) or\
       not check_columns(board):
        return False
    return True


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
