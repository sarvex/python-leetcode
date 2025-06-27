from collections import deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        BFS with pruning: Find the longest subsequence that appears exactly k times.

        Intuition:
        Use BFS to explore all possible subsequences, starting from the shortest ones.
        Only consider characters that appear at least k times in the original string.

        Approach:
        1. Count frequency of each character and keep only those appearing ≥ k times
        2. Use BFS to generate candidate subsequences in decreasing lexicographical order
        3. For each candidate, check if it appears exactly k times as a subsequence
        4. Return the longest valid subsequence found

        Complexity:
        Time: O(n * 26^l) where n is the length of s and l is the length of the answer
        Space: O(26^l) for the queue
        """
        # Count character frequencies
        char_freq = [0] * 26
        for ch in s:
            char_freq[ord(ch) - ord('a')] += 1

        # Filter valid characters (appearing at least k times)
        valid_chars = [chr(i + ord('a')) for i, freq in enumerate(char_freq) if freq >= k]

        def is_valid_subsequence(subsequence: str) -> bool:
            """Check if subsequence appears exactly k times in s."""
            i = count = 0
            for ch in s:
                if subsequence[i] == ch:
                    i += 1
                    if i == len(subsequence):
                        count += 1
                        if count == k:
                            return True
                        i = 0
            return False

        # BFS to find the longest valid subsequence
        result = ""
        queue = deque([""])

        while queue:
            current = queue.popleft()
            for ch in valid_chars:
                new_subsequence = current + ch
                if is_valid_subsequence(new_subsequence):
                    result = new_subsequence  # Update result with the new valid subsequence
                    queue.append(new_subsequence)  # Continue BFS with this subsequence

        return result
