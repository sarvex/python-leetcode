class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        """Greedy selection of max subsequences and merging for largest number.

        Intuition:
            Split k digits between the two arrays in all possible ways, pick
            the maximum subsequence from each, then merge them to form the
            largest possible number.

        Approach:
            1. For each split (x from nums1, k-x from nums2), extract the
               maximum subsequence of the given length using a monotonic stack.
            2. Merge the two subsequences by always picking the lexicographically
               larger remaining sequence.
            3. Track the overall maximum across all splits.

        Complexity:
            Time: O(k * (m + n)) where m and n are lengths of nums1 and nums2
            Space: O(k) for subsequences and merged result
        """

        def max_subsequence(nums: list[int], length: int) -> list[int]:
            size = len(nums)
            stack = [0] * length
            top = -1
            remaining = size - length
            for val in nums:
                while top >= 0 and stack[top] < val and remaining > 0:
                    top -= 1
                    remaining -= 1
                if top + 1 < length:
                    top += 1
                    stack[top] = val
                else:
                    remaining -= 1
            return stack

        def is_greater(seq1: list[int], seq2: list[int], idx1: int, idx2: int) -> bool:
            if idx1 >= len(seq1):
                return False
            if idx2 >= len(seq2):
                return True
            if seq1[idx1] > seq2[idx2]:
                return True
            if seq1[idx1] < seq2[idx2]:
                return False
            return is_greater(seq1, seq2, idx1 + 1, idx2 + 1)

        def merge(seq1: list[int], seq2: list[int]) -> list[int]:
            total = len(seq1) + len(seq2)
            idx1 = idx2 = 0
            merged = [0] * total
            for pos in range(total):
                if is_greater(seq1, seq2, idx1, idx2):
                    merged[pos] = seq1[idx1]
                    idx1 += 1
                else:
                    merged[pos] = seq2[idx2]
                    idx2 += 1
            return merged

        len1, len2 = len(nums1), len(nums2)
        lower, upper = max(0, k - len2), min(k, len1)
        result = [0] * k
        for split in range(lower, upper + 1):
            subseq1 = max_subsequence(nums1, split)
            subseq2 = max_subsequence(nums2, k - split)
            candidate = merge(subseq1, subseq2)
            if result < candidate:
                result = candidate
        return result
