class Solution:
    def splitLoopedString(self, strs: list[str]) -> str:
        """Find lexicographically largest string by splitting a concatenated loop.

        Intuition:
            Each string can appear forwards or reversed. For each possible split
            point, we try both orientations of the split string and pick the
            lexicographically largest result.

        Approach:
            1. Pre-orient each string to its lexicographically larger form.
            2. For each string, try every split point within it.
            3. For each split, form the full loop string in both orientations.
            4. Track the overall maximum.

        Complexity:
            Time: O(n * m) where n is number of strings and m is total characters
            Space: O(m)
        """
        strs = [s[::-1] if s[::-1] > s else s for s in strs]
        answer = "".join(strs)
        for i, current in enumerate(strs):
            tail = "".join(strs[i + 1 :]) + "".join(strs[:i])
            for j in range(len(current)):
                prefix = current[j:]
                suffix = current[:j]
                answer = max(answer, prefix + tail + suffix)
                answer = max(answer, suffix[::-1] + tail + prefix[::-1])
        return answer
