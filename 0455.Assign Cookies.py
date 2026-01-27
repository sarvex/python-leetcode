class Solution:
    def findContentChildren(self, greed: list[int], sizes: list[int]) -> int:
        """Greedy assignment of smallest sufficient cookies to least greedy children.

        Intuition:
            Sort both children by greed and cookies by size. Greedily assign
            the smallest cookie that satisfies each child.

        Approach:
            1. Sort greed factors and cookie sizes.
            2. Use two pointers: for each child, advance the cookie pointer
               until a sufficiently large cookie is found.
            3. If no cookie can satisfy the child, return the count so far.

        Complexity:
            Time: O(n log n + m log m) for sorting both arrays.
            Space: O(1) excluding the sort space.
        """
        greed.sort()
        sizes.sort()
        cookie_idx = 0
        for child_idx, child_greed in enumerate(greed):
            while cookie_idx < len(sizes) and sizes[cookie_idx] < greed[child_idx]:
                cookie_idx += 1
            if cookie_idx >= len(sizes):
                return child_idx
            cookie_idx += 1
        return len(greed)
