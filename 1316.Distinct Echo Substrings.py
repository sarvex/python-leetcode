class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """Count distinct substrings that can be written as concatenation of two equal parts.

        Intuition:
            A substring is an echo if its first half equals its second half.
            Use rolling hash to compare halves efficiently.

        Approach:
            Precompute polynomial rolling hash. For every even-length substring,
            compare hashes of the two halves and collect unique hashes in a set.

        Complexity:
            Time: O(n^2)
            Space: O(n^2) for the hash set in worst case
        """
        length = len(text)
        base = 131
        mod = 10**9 + 7
        hash_prefix = [0] * (length + 10)
        power = [1] * (length + 10)
        for i, char in enumerate(text):
            token = ord(char) - ord("a") + 1
            hash_prefix[i + 1] = (hash_prefix[i] * base + token) % mod
            power[i + 1] = (power[i] * base) % mod

        def get_hash(left: int, right: int) -> int:
            return (
                hash_prefix[right] - hash_prefix[left - 1] * power[right - left + 1]
            ) % mod

        seen: set[int] = set()
        for i in range(length - 1):
            for j in range(i + 1, length, 2):
                mid = (i + j) >> 1
                first_half = get_hash(i + 1, mid + 1)
                second_half = get_hash(mid + 2, j + 1)
                if first_half == second_half:
                    seen.add(first_half)
        return len(seen)
