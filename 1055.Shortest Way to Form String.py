class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """Find minimum subsequences of source to form target.

        Intuition:
            Greedily match as many target characters as possible in each pass
            through source.

        Approach:
            For each pass, use two pointers to advance through source and target.
            If no progress is made in a pass, return -1.

        Complexity:
            Time: O(m * n) where m = len(source), n = len(target)
            Space: O(1)
        """

        def match_pass(source_idx: int, target_idx: int) -> int:
            while source_idx < source_len and target_idx < target_len:
                if source[source_idx] == target[target_idx]:
                    target_idx += 1
                source_idx += 1
            return target_idx

        source_len, target_len = len(source), len(target)
        subsequence_count = 0
        target_idx = 0
        while target_idx < target_len:
            new_target_idx = match_pass(0, target_idx)
            if new_target_idx == target_idx:
                return -1
            target_idx = new_target_idx
            subsequence_count += 1
        return subsequence_count
