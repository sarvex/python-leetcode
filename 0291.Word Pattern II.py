class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        """Backtracking with bijective mapping between pattern chars and substrings.

        Intuition:
            Try every possible substring for each pattern character, maintaining
            a bijective mapping. Backtrack when conflicts arise.

        Approach:
            1. Use DFS with two pointers: one for pattern, one for the string.
            2. For each pattern character, try all possible substrings starting
               at the current string position.
            3. If the character already maps to a substring, only proceed if it matches.
            4. Otherwise, assign the mapping and recurse; backtrack on failure.

        Complexity:
            Time: O(n^m) where m is pattern length and n is string length
            Space: O(m + n)
        """
        pattern_len, string_len = len(pattern), len(s)
        char_to_substring: dict[str, str] = {}
        used_substrings: set[str] = set()

        def dfs(pattern_idx: int, string_idx: int) -> bool:
            if pattern_idx == pattern_len and string_idx == string_len:
                return True
            if (
                pattern_idx == pattern_len
                or string_idx == string_len
                or string_len - string_idx < pattern_len - pattern_idx
            ):
                return False
            for k in range(string_idx, string_len):
                substring = s[string_idx : k + 1]
                if char_to_substring.get(pattern[pattern_idx]) == substring:
                    if dfs(pattern_idx + 1, k + 1):
                        return True
                if (
                    pattern[pattern_idx] not in char_to_substring
                    and substring not in used_substrings
                ):
                    char_to_substring[pattern[pattern_idx]] = substring
                    used_substrings.add(substring)
                    if dfs(pattern_idx + 1, k + 1):
                        return True
                    char_to_substring.pop(pattern[pattern_idx])
                    used_substrings.remove(substring)
            return False

        return dfs(0, 0)
