class Solution:
    def depthSum(self, nestedList: list["NestedInteger"]) -> int:
        """Recursive DFS weighting each integer by its nesting depth.

        Intuition:
            Each integer should be multiplied by its depth level. Recursively
            traverse the nested structure, incrementing depth at each level.

        Approach:
            1. Iterate over each element in the nested list.
            2. If it is an integer, add value * depth to the running sum.
            3. If it is a list, recurse with depth + 1.

        Complexity:
            Time: O(n) where n is the total number of nested elements
            Space: O(d) where d is the maximum nesting depth
        """

        def dfs(nested_list: list["NestedInteger"], depth: int) -> int:
            depth_sum = 0
            for item in nested_list:
                if item.isInteger():
                    depth_sum += item.getInteger() * depth
                else:
                    depth_sum += dfs(item.getList(), depth + 1)
            return depth_sum

        return dfs(nestedList, 1)
