class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        """Find longest cycle in array index chains using visited tracking.

        Intuition:
            Each index leads to a cycle since values are a permutation.
            Once we visit all elements of a cycle, we never need to revisit them.

        Approach:
            1. Maintain a visited array.
            2. For each unvisited index, follow the chain until we return to
               the start, counting the cycle length.
            3. Track the maximum cycle length.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(nums)
        visited = [False] * length
        result = 0
        for i in range(length):
            if visited[i]:
                continue
            current, cycle_length = nums[i], 1
            visited[current] = True
            while nums[current] != nums[i]:
                current = nums[current]
                cycle_length += 1
                visited[current] = True
            result = max(result, cycle_length)
        return result
