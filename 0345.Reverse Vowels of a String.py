class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Two-pointer approach to reverse only the vowels in a string.

        Intuition:
        Since we only need to reverse the vowels while keeping other characters in place,
        we can use two pointers moving from both ends of the string and swap vowels when found.

        Approach:
        1. Convert the string to a list for in-place character swapping
        2. Use two pointers: one from the start and one from the end
        3. Move the left pointer right until it points to a vowel
        4. Move the right pointer left until it points to a vowel
        5. Swap the vowels and continue until pointers meet

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(n) for the character list
        """
        vowels = frozenset('aeiouAEIOU')
        chars = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-vowels from left
            while left < right and chars[left].lower() not in vowels:
                left += 1

            # Skip non-vowels from right
            while left < right and chars[right].lower() not in vowels:
                right -= 1

            # Swap vowels and move pointers
            chars[left], chars[right] = chars[right], chars[left]
            left, right = left + 1, right - 1

        return ''.join(chars)
