from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Check if s2 contains a permutation of s1 using sliding window.

        Intuition:
            A permutation of s1 in s2 means a substring of s2 with the same
            character frequencies as s1. We slide a window of length len(s1)
            across s2 and compare frequency counts.

        Approach:
            1. Count character frequencies of s1 and the first window of s2.
            2. Slide the window across s2, adding the new character and removing
               the outgoing character.
            3. Compare counts at each position.

        Complexity:
            Time: O(n) where n is len(s2)
            Space: O(1) since alphabet size is fixed at 26
        """
        window_size = len(s1)
        target_count = Counter(s1)
        window_count = Counter(s2[:window_size])
        if target_count == window_count:
            return True
        for i in range(window_size, len(s2)):
            window_count[s2[i]] += 1
            window_count[s2[i - window_size]] -= 1
            if target_count == window_count:
                return True
        return False
