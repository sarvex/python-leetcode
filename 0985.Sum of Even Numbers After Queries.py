class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        """Incrementally maintain even sum while applying queries.

        Intuition:
        Instead of recalculating the even sum from scratch after each query,
        adjust the running sum by subtracting the old value (if even) and
        adding the new value (if even).

        Approach:
        1. Compute initial sum of all even numbers
        2. For each query, remove old value from sum if even
        3. Apply the update and add new value to sum if even
        4. Record the current even sum after each query

        Complexity:
        Time: O(n + q) where n is array length and q is number of queries
        Space: O(q) for the result list
        """
        even_sum = sum(x for x in nums if x % 2 == 0)
        result: list[int] = []
        for value, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += value
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            result.append(even_sum)
        return result
