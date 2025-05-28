from itertools import chain


def convert(s: str, num_rows: int) -> str:
    """
    Convert string to zigzag pattern and read line by line.
    
    Intuition:
    - The zigzag pattern can be thought of as moving down and then diagonally up repeatedly.
    - We can simulate this by tracking the current row and direction.
    
    Approach:
    1. If num_rows is 1 or >= len(s), return the string as is.
    2. Create a list of strings, one for each row.
    3. Track the current row and direction (down or up).
    4. For each character, append it to the current row's string.
    5. Change direction when reaching the top or bottom row.
    6. Finally, join all row strings.
    
    Complexity:
    - Time: O(n), where n is the length of the input string.
    - Space: O(n), to store the zigzag pattern.
    """
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    rows = [[] for _ in range(num_rows)]
    current_row = 0
    direction = 1  # 1 for down, -1 for up
    
    for char in s:
        rows[current_row].append(char)
        if current_row == 0:
            direction = 1
        elif current_row == num_rows - 1:
            direction = -1
        current_row += direction
    
    return ''.join(chain(*rows))


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return convert(s, numRows)
