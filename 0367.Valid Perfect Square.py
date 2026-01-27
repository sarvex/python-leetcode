from bisect import bisect_left


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """Check if a number is a perfect square using binary search.

        Intuition:
            A perfect square has an integer square root. Binary search over
            the range [1, num] to find a value whose square equals num.

        Approach:
            Use bisect_left with a key function that computes x^2 to find
            the insertion point for num in the squared sequence. If the value
            at that position squares to num, it is a perfect square.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        root = bisect_left(range(1, num + 1), num, key=lambda x: x * x) + 1
        return root * root == num
