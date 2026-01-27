class Solution:
    def depthSumInverse(self, nestedList: list) -> int:
        """Compute inverse depth-weighted sum using DFS to find max depth.

        Intuition:
            Instead of weighting by depth from root, weight by inverse depth
            (max_depth + 1 - depth). We can compute this as
            (max_depth + 1) * total_sum - depth_weighted_sum.

        Approach:
            Perform DFS to simultaneously compute the total sum, the
            depth-weighted sum, and the maximum depth. The inverse weighted
            sum is then (max_depth + 1) * total_sum - depth_weighted_sum.

        Complexity:
            Time: O(n) where n is the total number of integers
            Space: O(d) where d is the maximum nesting depth
        """

        def dfs(element: object, depth: int) -> None:
            nonlocal max_depth, total_sum, weighted_sum
            max_depth = max(max_depth, depth)
            if element.isInteger():
                total_sum += element.getInteger()
                weighted_sum += element.getInteger() * depth
            else:
                for child in element.getList():
                    dfs(child, depth + 1)

        max_depth = total_sum = weighted_sum = 0
        for element in nestedList:
            dfs(element, 1)
        return (max_depth + 1) * total_sum - weighted_sum
