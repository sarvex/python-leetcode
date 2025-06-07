from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def clearStars(self, s: str) -> str:
        """Stack-based approach for removing characters based on star operations.

        Intuition:
        When we encounter a '*', we need to remove the lexicographically smallest character
        that appeared before it. We can use a stack-like structure to track characters.

        Approach:
        1. Use a dictionary to track positions of each character
        2. Mark positions to remove when encountering '*'
        3. Remove the lexicographically smallest character when processing a '*'
        4. Construct final string from non-removed characters

        Complexity:
        Time: O(n), where n is the length of string s
        Space: O(n) for storing character positions and removal status
        """
        char_positions = defaultdict(list)  # Maps characters to their positions
        n = len(s)
        to_remove = [False] * n

        for i, char in enumerate(s):
            if char == '*':
                to_remove[i] = True  # Mark '*' for removal

                # Find lexicographically smallest character to remove
                for c in ascii_lowercase:
                    if char_positions[c]:  # If this character exists in our tracking
                        to_remove[char_positions[c].pop()] = True  # Mark for removal
                        break
            else:
                char_positions[char].append(i)  # Track position of this character

        # Construct result string from non-removed characters
        return ''.join(s[i] for i in range(n) if not to_remove[i])
