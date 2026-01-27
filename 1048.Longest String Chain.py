class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        """Longest String Chain using DP with predecessor check.

        Intuition:
            Sort words by length so predecessors always appear before their
            successors. Then use DP to find the longest chain.

        Approach:
            Sort by length. For each word, check all previous words as
            potential predecessors (differ by exactly one character insertion).
            Use a two-pointer comparison to verify the predecessor relationship.

        Complexity:
            Time: O(n^2 * L) where L is max word length
            Space: O(n)
        """

        def is_predecessor(shorter: str, longer: str) -> bool:
            if len(longer) - len(shorter) != 1:
                return False
            si = li = mismatches = 0
            while si < len(shorter) and li < len(longer):
                if shorter[si] != longer[li]:
                    mismatches += 1
                else:
                    si += 1
                li += 1
            return mismatches < 2 and si == len(shorter)

        count = len(words)
        chain_length = [1] * (count + 1)
        words.sort(key=len)
        result = 1
        for i in range(1, count):
            for j in range(i):
                if is_predecessor(words[j], words[i]):
                    chain_length[i] = max(chain_length[i], chain_length[j] + 1)
            result = max(result, chain_length[i])
        return result
