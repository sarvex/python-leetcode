class Solution:
    def grayCode(self, n: int) -> list[int]:
        """Bit Manipulation Approach

        Intuition:
            The i-th Gray code can be generated from the binary representation
            of i by XOR-ing i with i >> 1.

        Approach:
            Iterate from 0 to 2^n - 1 and compute each Gray code value
            using the formula i ^ (i >> 1).

        Complexity:
            Time: O(2^n)
            Space: O(2^n)
        """
        return [i ^ (i >> 1) for i in range(1 << n)]
