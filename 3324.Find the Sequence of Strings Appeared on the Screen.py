from string import ascii_lowercase
from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        """Simulate typing process to find sequence of strings that appear on screen.

        Intuition: For each character in target, we need to type all letters from 'a' until
        we reach the desired character, appending each intermediate string to our result.

        Approach: Iterate through each character in target. For each character, start from
        the last string in our result (or empty string if no previous result) and append
        each letter from 'a' to the target character, adding each intermediate string to
        our result list.

        Complexity:
            Time: O(n * 26) where n is the length of target string
            Space: O(n * avg_len) where avg_len is the average length of strings in result

        Args:
            target: The target string to be typed

        Returns:
            List of strings that appear on the screen during the typing process
        """
        result = []
        for char in target:
            current = result[-1] if result else ""
            for letter in ascii_lowercase:
                new_string = current + letter
                result.append(new_string)
                if letter == char:
                    break
        return result
