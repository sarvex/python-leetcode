from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        """Find the minimum substring length to replace for a balanced string.

        Intuition:
            A string of length n with characters Q, W, E, R is balanced when
            each appears n/4 times. We need to find the smallest window whose
            removal leaves all remaining character counts at most n/4.

        Approach:
            Use a sliding window. Shrink the left boundary while the characters
            outside the window all have counts <= n/4. Track the minimum window
            size that satisfies this condition.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        frequency = Counter(s)
        length = len(s)
        target = length // 4
        if all(v <= target for v in frequency.values()):
            return 0
        result = length
        left = 0
        for right, char in enumerate(s):
            frequency[char] -= 1
            while left <= right and all(v <= target for v in frequency.values()):
                result = min(result, right - left + 1)
                frequency[s[left]] += 1
                left += 1
        return result
