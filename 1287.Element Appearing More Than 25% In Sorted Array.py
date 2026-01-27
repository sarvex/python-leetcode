class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        """Find element appearing more than 25% in a sorted array.

        Intuition:
            In a sorted array, an element appearing more than 25% of the time must
            be found at index i where arr[i] == arr[i + n/4].

        Approach:
            Iterate through the array and check if the element at position i equals
            the element at position i + n//4. The first match is the answer.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        length = len(arr)
        quarter = length >> 2
        for i, value in enumerate(arr):
            if value == arr[i + quarter]:
                return value
        return 0
