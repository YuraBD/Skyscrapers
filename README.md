Skyscrapers is a building placing puzzle based on an NxN grid with some clues along its sides. The object is to place a skyscraper in each square, with a height between 1 and N, so that no two skyscrapers in a row or column have the same number of floors. In addition, the number of visible skyscrapers, as viewed from the direction of each clue, is equal to the value of the clue. Higher skyscrapers block the view of lower skyscrapers located behind them.

In module **skyscrapers.py** are functions which check the status of skyscraper game board.
Return True if the board status is compliant with the rules, False otherwise.

This module has 7 functions:

1) **read_input**
Read game board file from path.
Return list of str.

2) **left_to_right_check**
Check row-wise visibility from left to right.
Return True if number of building from the left-most hint is visible looking to the right,
wFalse otherwise.

input_line - representing board row.
pivot - number on the left-most hint of the input_line.

3) **check_not_finished_board**
Check if skyscraper board is not finished, i.e., '?' present on the game board.
Return True if finished, False otherwise.

4) **check_uniqueness_in_rows**
Check buildings of unique height in each row.
Return True if buildings in a row have unique length, False otherwise.

5) **check_horizontal_visibility**
Check row-wise visibility (left-right and vice versa)
Return True if all horizontal hints are satisfiable,
 i.e., for line 412453* , hint is 4, and 1245 are the four buildings
  wthat could be observed from the hint looking to the right.

6) **check_columns**
Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).
Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

7) **check_skyscrapers**
Main function to check the status of skyscraper game board.
Return True if the board status is compliant with the rules,
False otherwise.