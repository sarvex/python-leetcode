class Solution:
    def findPermutation(self, s: str) -> list[int]:
        """Reverse segments of consecutive 'D' characters.

        Intuition:
            Start with the identity permutation. Each 'D' sequence requires
            a decreasing segment, achieved by reversing the corresponding
            portion of the identity.

        Approach:
            Initialize the result as [1, 2, ..., n+1]. Find each maximal
            run of 'D' characters and reverse the corresponding subarray
            to create the required decreasing sequence.

        Complexity:
            Time: O(n)
            Space: O(n) for the result array
        """
        length = len(s)
        result = list(range(1, length + 2))
        i = 0
        while i < length:
            j = i
            while j < length and s[j] == "D":
                j += 1
            result[i : j + 1] = result[i : j + 1][::-1]
            i = max(i + 1, j)
        return result
