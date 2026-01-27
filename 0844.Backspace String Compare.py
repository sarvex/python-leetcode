class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """O(1) space comparison using reverse traversal with skip counters.

        Intuition:
            Process both strings from the end, using counters to track
            backspaces. Compare characters only when both pointers are at
            non-deleted positions.

        Approach:
            1. Start from the end of both strings.
            2. Skip characters that are '#' or have pending backspaces.
            3. Compare the current characters at both pointers.
            4. If they differ or one string is exhausted early, return False.

        Complexity:
            Time: O(n + m)
            Space: O(1)
        """
        s_idx, t_idx = len(s) - 1, len(t) - 1
        s_skip = t_skip = 0
        while s_idx >= 0 or t_idx >= 0:
            while s_idx >= 0:
                if s[s_idx] == "#":
                    s_skip += 1
                    s_idx -= 1
                elif s_skip:
                    s_skip -= 1
                    s_idx -= 1
                else:
                    break
            while t_idx >= 0:
                if t[t_idx] == "#":
                    t_skip += 1
                    t_idx -= 1
                elif t_skip:
                    t_skip -= 1
                    t_idx -= 1
                else:
                    break
            if s_idx >= 0 and t_idx >= 0:
                if s[s_idx] != t[t_idx]:
                    return False
            elif s_idx >= 0 or t_idx >= 0:
                return False
            s_idx, t_idx = s_idx - 1, t_idx - 1
        return True
