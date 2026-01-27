class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        """Backtracking with pruning to partition into four equal sides.

        Intuition:
            The total length must be divisible by 4. Try placing each
            matchstick into one of 4 sides, pruning when a side exceeds
            the target or when duplicate side lengths are encountered.

        Approach:
            Sort matchsticks in descending order for earlier pruning. Use
            DFS to try assigning each matchstick to one of the four sides.
            Skip duplicate side lengths to avoid redundant searches.

        Complexity:
            Time: O(4^n) worst case, much better with pruning
            Space: O(n) recursion depth
        """

        def dfs(index: int) -> bool:
            if index == len(matchsticks):
                return True
            for i in range(4):
                if i > 0 and sides[i - 1] == sides[i]:
                    continue
                sides[i] += matchsticks[index]
                if sides[i] <= target and dfs(index + 1):
                    return True
                sides[i] -= matchsticks[index]
            return False

        target, remainder = divmod(sum(matchsticks), 4)
        if remainder or target < max(matchsticks):
            return False
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        return dfs(0)
