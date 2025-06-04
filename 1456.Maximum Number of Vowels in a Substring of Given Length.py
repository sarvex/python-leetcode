class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Sliding window approach to find maximum number of vowels in a substring of length k.

        Intuition:
            Use a sliding window of fixed size k and count vowels in it. As we slide the window,
            we add a new character and remove the oldest one, updating the vowel count accordingly.

        Approach:
            1. Define a set of vowels for O(1) lookups
            2. Initialize the count of vowels in the first window of size k
            3. Slide the window through the string, updating the vowel count:
               - Add 1 if the new character is a vowel
               - Subtract 1 if the character leaving the window is a vowel
            4. Track the maximum vowel count seen so far

        Complexity:
            Time: O(n) where n is the length of the string
            Space: O(1) as we only use a fixed-size set and a few variables
        """
        vowels = frozenset("aeiou")
        result = current = sum(s[i] in vowels for i in range(k))

        for i in range(k, len(s)):
            current += (s[i] in vowels) - (s[i - k] in vowels)
            result = max(result, current)

            if result == k:
                break

        return result
