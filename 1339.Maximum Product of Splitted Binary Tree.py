import sys

sys.setrecursionlimit(100000)


class Solution:
    def maxProduct(self, root) -> int:
        sums = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sums.append(s)
            return s

        total = dfs(root)
        return max(s * (total - s) for s in sums) % 1000000007
