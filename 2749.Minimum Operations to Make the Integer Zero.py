class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        Greedy bit-count bound with linear search

        Intuition:
        We need the smallest k such that num1 - k*num2 can be written as the sum of exactly k powers of two. This requires two conditions: non-negativity and at least as many set bits as k.

        Approach:
        Iterate k from 1 upward. Let x = num1 - k*num2. If x < k, it's impossible for any larger k, so return -1. If the number of set bits in x (x.bit_count()) is <= k, then we can represent x as a sum of k powers of two by splitting bits as needed, so return k.

        Complexity:
        Time: O(answer), where answer is the returned k.
        Space: O(1)
        """
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1
