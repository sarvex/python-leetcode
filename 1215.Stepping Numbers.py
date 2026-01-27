from collections import deque


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list[int]:
        """Stepping numbers in a given range using BFS.

        Intuition:
            A stepping number has adjacent digits differing by exactly 1. We can
            generate them level by level starting from single digits using BFS.

        Approach:
            Start BFS from digits 1-9. For each number, append digits that differ
            by 1 from the last digit. Collect numbers within [low, high]. Handle
            zero as a special case.

        Complexity:
            Time: O(2^d) where d is the number of digits in high
            Space: O(2^d) for the BFS queue
        """
        result: list[int] = []
        if low == 0:
            result.append(0)
        queue: deque[int] = deque(range(1, 10))
        while queue:
            value = queue.popleft()
            if value > high:
                break
            if value >= low:
                result.append(value)
            last_digit = value % 10
            if last_digit:
                queue.append(value * 10 + last_digit - 1)
            if last_digit < 9:
                queue.append(value * 10 + last_digit + 1)
        return result
