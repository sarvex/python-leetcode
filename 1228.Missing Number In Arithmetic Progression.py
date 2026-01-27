class Solution:
    def missingNumber(self, arr: list[int]) -> int:
        """Missing number in arithmetic progression.

        Intuition:
            In a complete arithmetic progression of length n+1, the sum equals
            (first + last) * (n+1) / 2. The missing value is this expected
            sum minus the actual sum.

        Approach:
            Compute the expected sum using the first and last elements with
            the original length (len + 1), then subtract the current sum.

        Complexity:
            Time: O(n) where n is the length of the array
            Space: O(1)
        """
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)
