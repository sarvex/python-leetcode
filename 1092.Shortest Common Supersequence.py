class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """Build shortest common supersequence via LCS backtracking.

        Intuition:
            The shortest common supersequence must contain the LCS of both strings,
            with remaining characters interleaved. By computing the LCS table first,
            we can reconstruct the supersequence by backtracking through the DP table.

        Approach:
            Compute the LCS length table using standard DP. Then backtrack from
            (m, n) to (0, 0), appending characters from str1 or str2 depending on
            which direction gives the optimal path, and appending shared characters
            once when they match.

        Complexity:
            Time: O(m * n) where m and n are lengths of str1 and str2
            Space: O(m * n) for the DP table
        """
        row_count, col_count = len(str1), len(str2)
        lcs = [[0] * (col_count + 1) for _ in range(row_count + 1)]
        for i in range(1, row_count + 1):
            for j in range(1, col_count + 1):
                if str1[i - 1] == str2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
        result: list[str] = []
        i, j = row_count, col_count
        while i or j:
            if i == 0:
                j -= 1
                result.append(str2[j])
            elif j == 0:
                i -= 1
                result.append(str1[i])
            else:
                if lcs[i][j] == lcs[i - 1][j]:
                    i -= 1
                    result.append(str1[i])
                elif lcs[i][j] == lcs[i][j - 1]:
                    j -= 1
                    result.append(str2[j])
                else:
                    i, j = i - 1, j - 1
                    result.append(str1[i])
        return "".join(result[::-1])
