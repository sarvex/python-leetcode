class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """Count vowels permutation using dynamic programming.

        Intuition:
            Each vowel can only be followed by specific vowels based on the
            rules. Track counts for each vowel position and transition.

        Approach:
            Use DP where f[i] represents count of strings ending with vowel i
            (a=0, e=1, i=2, o=3, u=4). Apply transition rules each step.

        Complexity:
            Time: O(n)
            Space: O(1) since we only track 5 vowel counts
        """
        MOD = 10**9 + 7
        counts = [1] * 5
        for _ in range(n - 1):
            new_counts = [0] * 5
            new_counts[0] = (counts[1] + counts[2] + counts[4]) % MOD
            new_counts[1] = (counts[0] + counts[2]) % MOD
            new_counts[2] = (counts[1] + counts[3]) % MOD
            new_counts[3] = counts[2]
            new_counts[4] = (counts[2] + counts[3]) % MOD
            counts = new_counts
        return sum(counts) % MOD
