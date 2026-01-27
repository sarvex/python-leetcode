class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        """Count unique Morse code transformations using a set.

        Intuition:
            Map each word to its Morse code representation and count distinct ones.

        Approach:
            1. Define the Morse code for each letter a-z.
            2. Transform each word by concatenating its letters' Morse codes.
            3. Use a set to count unique transformations.

        Complexity:
            Time: O(n * m) where n = number of words, m = average word length
            Space: O(n * m)
        """
        morse_codes = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        transformations = {
            "".join(morse_codes[ord(char) - ord("a")] for char in word)
            for word in words
        }
        return len(transformations)
