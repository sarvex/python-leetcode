class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """DFS to verify additive number property with two initial numbers.

        Intuition:
            Try all possible splits for the first two numbers, then verify
            the rest of the string follows the additive sequence.

        Approach:
            1. Enumerate all possible first and second numbers by splitting.
            2. For each pair, recursively check if the remaining string
               starts with their sum, continuing the sequence.
            3. Handle leading zeros by skipping invalid splits.

        Complexity:
            Time: O(n^3) where n is the length of num
            Space: O(n) for recursion depth
        """

        def dfs(first: int, second: int, remaining: str) -> bool:
            if not remaining:
                return True
            if first + second > 0 and remaining[0] == "0":
                return False
            for i in range(1, len(remaining) + 1):
                if first + second == int(remaining[:i]):
                    if dfs(second, first + second, remaining[i:]):
                        return True
            return False

        length = len(num)
        for i in range(1, length - 1):
            for j in range(i + 1, length):
                if i > 1 and num[0] == "0":
                    break
                if j - i > 1 and num[i] == "0":
                    continue
                if dfs(int(num[:i]), int(num[i:j]), num[j:]):
                    return True
        return False
