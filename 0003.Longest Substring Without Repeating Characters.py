class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Intuition:
        Use a sliding window approach with a dictionary to track character positions.

        Approach:
        1. Use a dictionary to store the most recent index of each character
        2. Maintain two pointers (left and right) to represent the current window
        3. Move the right pointer and update the max length when a duplicate is found
        4. Update the left pointer to skip past the previous occurrence of the current character

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(min(m, n)) where m is the size of the character set
        """
        char_index = {}  # Stores the most recent index of each character
        max_length = left = 0

        for right, char in enumerate(s):
            # If character is in dict and its index is within the current window
            if char in char_index and char_index[char] >= left:
                # Move left pointer to the right of the previous occurrence
                left = char_index[char] + 1

            # Update the most recent index of the character
            char_index[char] = right

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
