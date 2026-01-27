class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse each word in the string while preserving word order.

        Intuition:
            Split the string by spaces, reverse each individual word, and
            rejoin them with spaces.

        Approach:
            1. Split the string by spaces.
            2. Reverse each word using slicing.
            3. Join the reversed words back with spaces.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        return " ".join([word[::-1] for word in s.split(" ")])
