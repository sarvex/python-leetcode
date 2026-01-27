from math import inf


class Solution:
    def nextClosestTime(self, time: str) -> str:
        """DFS enumeration of all valid times using available digits.

        Intuition:
            With only 4 digit positions and at most 4 unique digits, we can
            enumerate all possible valid times and find the closest one after
            the current time.

        Approach:
            1. Extract unique digits from the input time.
            2. Use DFS to build all 4-digit combinations from those digits.
            3. Filter valid times (hours < 24, minutes < 60).
            4. Find the time closest to but after the current time.
            5. If no later time exists, wrap around to the smallest valid time.

        Complexity:
            Time: O(4^4) = O(256) constant for enumerating all combinations
            Space: O(4^4) for the DFS recursion stack
        """

        def is_valid_time(candidate: str) -> bool:
            hours, minutes = int(candidate[:2]), int(candidate[2:])
            return 0 <= hours < 24 and 0 <= minutes < 60

        def dfs(current: str) -> None:
            if len(current) == 4:
                if not is_valid_time(current):
                    return
                nonlocal result, min_diff
                candidate_minutes = int(current[:2]) * 60 + int(current[2:])
                if current_minutes < candidate_minutes < current_minutes + min_diff:
                    min_diff = candidate_minutes - current_minutes
                    result = current[:2] + ":" + current[2:]
                return
            for digit in digits:
                dfs(current + digit)

        digits = {char for char in time if char != ":"}
        current_minutes = int(time[:2]) * 60 + int(time[3:])
        min_diff = inf
        result = None
        dfs("")
        if result is None:
            smallest = min(int(char) for char in digits)
            result = f"{smallest}{smallest}:{smallest}{smallest}"
        return result
