from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Sliding window with character frequency counting

        Intuition:
        Use a sliding window approach to find the minimum substring containing all characters
        from t. Track character frequencies and maintain a valid window that contains all
        required characters before minimizing its size.

        Approach:
        1. Create frequency counters for target string and current window
        2. Use two pointers to maintain a sliding window
        3. Expand right pointer to include required characters
        4. Once all required characters are included, contract left pointer to minimize window
        5. Track the minimum valid window found

        Complexity:
        Time: O(n) where n is the length of string s
        Space: O(k) where k is the number of unique characters in strings s and t
        """
        # Edge case handling
        if not s or not t:
            return ""

        # Initialize frequency counters and window parameters
        target_freq = Counter(t)
        window_freq = Counter()
        required_chars = len(target_freq)
        formed_chars = 0

        # Initialize window pointers and result tracking
        left = 0
        min_len = float('inf')
        result_start = 0

        # Process the string with sliding window
        for right, char in enumerate(s):
            # Add current character to window
            window_freq[char] += 1

            # Check if this character satisfies one of the required characters
            if char in target_freq and window_freq[char] == target_freq[char]:
                formed_chars += 1

            # Try to minimize window by moving left pointer
            while formed_chars == required_chars:
                # Update result if current window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result_start = left

                # Remove leftmost character from window
                left_char = s[left]
                window_freq[left_char] -= 1

                # Check if removing this character breaks the window validity
                if left_char in target_freq and window_freq[left_char] < target_freq[left_char]:
                    formed_chars -= 1

                # Move left pointer
                left += 1

        # Return the minimum window substring or empty string if not found
        return s[result_start:result_start + min_len] if min_len != float('inf') else ""
