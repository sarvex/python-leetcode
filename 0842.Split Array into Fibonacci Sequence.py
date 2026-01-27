class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        """Backtracking to find a valid Fibonacci-like split of the string.

        Intuition:
            Try all possible first two numbers, then greedily check if the
            remaining string follows the Fibonacci property.

        Approach:
            1. Use DFS to try splitting the string at each position.
            2. Prune: no leading zeros, values must fit in 32-bit int.
            3. Once two numbers are chosen, the next must equal their sum.
            4. Return the sequence if it has more than 2 elements.

        Complexity:
            Time: O(n^2) with pruning
            Space: O(n)
        """

        def dfs(start: int) -> bool:
            if start == length:
                return len(sequence) > 2
            current_value = 0
            for end in range(start, length):
                if end > start and num[start] == "0":
                    break
                current_value = current_value * 10 + int(num[end])
                if current_value > 2**31 - 1 or (
                    len(sequence) > 2 and current_value > sequence[-2] + sequence[-1]
                ):
                    break
                if len(sequence) < 2 or sequence[-2] + sequence[-1] == current_value:
                    sequence.append(current_value)
                    if dfs(end + 1):
                        return True
                    sequence.pop()
            return False

        length = len(num)
        sequence: list[int] = []
        dfs(0)
        return sequence
