class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        """Check if any element's double exists in the array.

        Intuition:
            For each element, check if its double or half has been seen before
            using a hash set for O(1) lookups.

        Approach:
            Iterate through the array, checking if 2*x or x/2 (when even)
            is already in the seen set before adding x.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        seen: set[int] = set()
        for x in arr:
            if x * 2 in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            seen.add(x)
        return False
