class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Split and Join Approach

        Intuition:
        The problem requires reversing the order of words in a string while removing extra spaces.
        Initial thought is to split the string into words and reverse their order.

        Approach:
        1. Split the string by spaces and filter out empty strings
        2. Reverse the list of words
        3. Join the words back with a single space

        Complexity:
        Time: O(n) where n is the length of the input string
        Space: O(n) for storing the words list
        """
        # Split by spaces, filter out empty strings, reverse the list, and join with spaces
        return ' '.join(reversed([word for word in s.split() if word]))

    def reverseWords_two_pointer(self, s: str) -> str:
        """
        Two-Pointer Approach

        Intuition:
        We can manually extract each word using two pointers to avoid extra space from splitting.

        Approach:
        1. Iterate through the string and extract each word using two pointers
        2. Add each word to a list
        3. Reverse the list and join with spaces

        Complexity:
        Time: O(n) where n is the length of the input string
        Space: O(n) for storing the words list
        """
        words = []
        i, n = 0, len(s)

        while i < n:
            # Skip spaces
            while i < n and s[i] == " ":
                i += 1

            if i < n:
                # Find word end
                j = i
                while j < n and s[j] != " ":
                    j += 1

                # Add word to list
                words.append(s[i:j])
                i = j

        # Join reversed words list
        return ' '.join(reversed(words))
