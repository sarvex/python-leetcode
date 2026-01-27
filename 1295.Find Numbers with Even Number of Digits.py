class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """Count numbers with an even number of digits.

        Intuition:
            Convert each number to a string and check if its length is even.

        Approach:
            Sum a boolean expression checking whether the string length of each
            number is even.

        Complexity:
            Time: O(n * d) where d is the average number of digits
            Space: O(1)
        """
        return sum(len(str(value)) % 2 == 0 for value in nums)
