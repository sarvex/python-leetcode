from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        """Greedy placement of most frequent characters at even then odd indices.

        Intuition:
            If the most frequent character appears more than (n+1)/2 times, it's
            impossible. Otherwise, placing characters by frequency into alternating
            positions ensures no two adjacent characters are the same.

        Approach:
            1. Count character frequencies
            2. If max frequency exceeds (n+1)//2, return empty string
            3. Place characters by descending frequency at even indices first,
               then wrap to odd indices

        Complexity:
            Time: O(n + k log k) where n is string length and k is alphabet size
            Space: O(n) for the result array
        """
        length = len(s)
        freq = Counter(s)
        max_freq = max(freq.values())
        if max_freq > (length + 1) // 2:
            return ""
        index = 0
        result: list[str] = [""] * length
        for char, count in freq.most_common():
            while count:
                result[index] = char
                count -= 1
                index += 2
                if index >= length:
                    index = 1
        return "".join(result)
