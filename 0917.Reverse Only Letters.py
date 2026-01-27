class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """Two-pointer approach skipping non-letter characters.

        Intuition:
            Use two pointers from both ends, skipping non-alphabetic
            characters, and swap only the letters.

        Approach:
            1. Convert string to list for in-place modification.
            2. Move left pointer forward past non-letters.
            3. Move right pointer backward past non-letters.
            4. Swap letters at both pointers and advance.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and not chars[left].isalpha():
                left += 1
            while left < right and not chars[right].isalpha():
                right -= 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left, right = left + 1, right - 1
        return "".join(chars)
