class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        """Backtracking with operator insertion between digits.

        Intuition:
            Try inserting +, -, or * between every possible split of the digit
            string. Multiplication requires tracking the previous operand to
            undo addition/subtraction and apply correct precedence.

        Approach:
            1. Use recursive backtracking to split the string at every position.
            2. Track the previous operand and running total for each branch.
            3. Handle leading zeros by breaking early when a segment starts with '0'.
            4. For multiplication, adjust the running total by undoing the previous
               operand and applying prev * next_val instead.

        Complexity:
            Time: O(4^n) where n is the length of num
            Space: O(n) for recursion depth
        """
        results: list[str] = []

        def search(start: int, previous: int, current: int, path: str) -> None:
            if start == len(num):
                if current == target:
                    results.append(path)
                return
            for i in range(start, len(num)):
                if i != start and num[start] == "0":
                    break
                next_val = int(num[start : i + 1])
                if start == 0:
                    search(i + 1, next_val, next_val, path + str(next_val))
                else:
                    search(
                        i + 1, next_val, current + next_val, path + "+" + str(next_val)
                    )
                    search(
                        i + 1, -next_val, current - next_val, path + "-" + str(next_val)
                    )
                    search(
                        i + 1,
                        previous * next_val,
                        current - previous + previous * next_val,
                        path + "*" + str(next_val),
                    )

        search(0, 0, 0, "")
        return results
