class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Optimized greedy bit manipulation approach with early stopping

        Intuition:
        We can always include all '0's in our subsequence as they don't increase the value.
        For '1's, we need to be selective to keep the binary value under k.
        Once the power of 2 exceeds k, we can stop processing and just count remaining '0's.

        Approach:
        1. Process the string from right to left (least significant bit first)
        2. Always include '0's as they don't affect the value
        3. For '1's, only include them if adding at the current position keeps value ≤ k
        4. Once the bit position exceeds k, stop and just count remaining '0's
        5. Track both the length of subsequence and its binary value

        Complexity:
        Time: O(n) where n is the length of string s
        Space: O(1) constant extra space
        """
        count = 0   # Number of characters in the valid subsequence
        value = 0   # Current value of the binary subsequence
        power = 1   # Current power of 2 (for binary digit weight)

        # Traverse the string from right to left
        for char in reversed(s):
            if char == '0':
                count += 1  # Always safe to include 0
            # Only include '1' if adding it keeps value ≤ k
            elif power <= k and value + power <= k:
                value += power
                count += 1
            # else, skip this '1' as it would exceed k

            power <<= 1  # Move to the next bit position (multiply power by 2)
            if power > k:  # Further '1' bits would be too big
                break

        # Count all the '0's we skipped before and any '1's we could take
        # This is an optimization: once power > k, we can take all remaining '0's
        remaining_chars = len(s) - count
        if remaining_chars > 0:
            count += s[:remaining_chars].count('0')

        return count
