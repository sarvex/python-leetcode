class Solution:
    def confusingNumberII(self, n: int) -> int:
        """Count confusing numbers in [1, n].

        Intuition:
            Only digits 0, 1, 6, 8, 9 can appear. Use digit DFS to enumerate
            valid numbers and check if rotation differs.

        Approach:
            DFS through digit positions building numbers from valid digits only.
            For each complete number, check if its 180-degree rotation differs.

        Complexity:
            Time: O(5^d * d) where d = number of digits in n
            Space: O(d) for recursion depth
        """
        rotation_map = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]

        def is_confusing(number: int) -> bool:
            rotated, remaining = 0, number
            while remaining:
                remaining, digit = divmod(remaining, 10)
                rotated = rotated * 10 + rotation_map[digit]
            return number != rotated

        def dfs(pos: int, tight: bool, current: int) -> int:
            if pos >= len(digits):
                return int(is_confusing(current))
            upper = int(digits[pos]) if tight else 9
            count = 0
            for digit in range(upper + 1):
                if rotation_map[digit] != -1:
                    count += dfs(
                        pos + 1, tight and digit == upper, current * 10 + digit
                    )
            return count

        digits = str(n)
        return dfs(0, True, 0)
