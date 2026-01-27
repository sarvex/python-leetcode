class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        """Recursive construction of strobogrammatic numbers by building from center.

        Intuition:
            Build strobogrammatic numbers by recursively constructing the inner
            part and wrapping with valid strobogrammatic digit pairs.

        Approach:
            Base cases: length 0 returns [''], length 1 returns ['0','1','8'].
            For larger lengths, recursively get results for length-2, then wrap
            each with valid pairs (1,1), (8,8), (6,9), (9,6). Add (0,0) only
            for inner layers (not the outermost).

        Complexity:
            Time: O(5^(n/2)) number of strobogrammatic numbers
            Space: O(5^(n/2)) to store results
        """

        def dfs(length: int) -> list[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            results = []
            for inner in dfs(length - 2):
                for left, right in ("11", "88", "69", "96"):
                    results.append(left + inner + right)
                if length != n:
                    results.append("0" + inner + "0")
            return results

        return dfs(n)
