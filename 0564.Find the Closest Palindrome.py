class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """Find the closest palindrome by generating candidates from mirrored halves.

        Intuition:
            The closest palindrome is formed by mirroring the left half of the
            number. We also need to consider edge cases like 10...0 - 1 and
            10...0 + 1, plus variations of the left half +/- 1.

        Approach:
            1. Generate candidate palindromes: 10^(len-1) - 1, 10^len + 1,
               and mirrors of left_half - 1, left_half, left_half + 1.
            2. Remove the original number from candidates.
            3. Return the candidate with the smallest absolute difference,
               breaking ties by choosing the smaller value.

        Complexity:
            Time: O(d) where d is the number of digits
            Space: O(d)
        """
        value = int(n)
        length = len(n)
        candidates = {10 ** (length - 1) - 1, 10**length + 1}
        left_half = int(n[: (length + 1) >> 1])
        for half in range(left_half - 1, left_half + 2):
            reversed_half = half if length % 2 == 0 else half // 10
            mirrored = half
            while reversed_half:
                mirrored = mirrored * 10 + reversed_half % 10
                reversed_half //= 10
            candidates.add(mirrored)
        candidates.discard(value)

        answer = -1
        for candidate in candidates:
            if (
                answer == -1
                or abs(candidate - value) < abs(answer - value)
                or (
                    abs(candidate - value) == abs(answer - value) and candidate < answer
                )
            ):
                answer = candidate
        return str(answer)
