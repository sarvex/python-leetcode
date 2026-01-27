class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """Count strobogrammatic numbers within a range using recursive generation.

        Intuition:
            Generate all strobogrammatic numbers of each valid length and count
            those falling within the given range.

        Approach:
            Reuse the recursive strobogrammatic number builder for each length
            from len(low) to len(high). For each generated number, check if its
            integer value falls within [low, high]. Leading zeros are handled
            by the recursive construction (0-padding only on inner layers).

        Complexity:
            Time: O(5^(n/2) * m) where n is max length and m is length range
            Space: O(5^(n/2)) for generated numbers
        """

        def dfs(length: int) -> list[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            results = []
            for inner in dfs(length - 2):
                for left, right in ("11", "88", "69", "96"):
                    results.append(left + inner + right)
                if length != target_length:
                    results.append("0" + inner + "0")
            return results

        min_len, max_len = len(low), len(high)
        low_val, high_val = int(low), int(high)
        count = 0
        for target_length in range(min_len, max_len + 1):
            for strobogrammatic in dfs(target_length):
                if low_val <= int(strobogrammatic) <= high_val:
                    count += 1
        return count
