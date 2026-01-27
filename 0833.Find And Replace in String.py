class Solution:
    def findReplaceString(
        self, s: str, indices: list[int], sources: list[str], targets: list[str]
    ) -> str:
        """Replace substrings at given indices if source matches.

        Intuition:
            Mark which indices have valid replacements, then build the result
            string by either inserting the target or keeping the original.

        Approach:
            1. For each replacement, check if s starts with the source at the index.
            2. Store valid replacement indices in an array.
            3. Walk through s, applying replacements or copying characters.

        Complexity:
            Time: O(n + sum(len(source)))
            Space: O(n)
        """
        length = len(s)
        replacement_map = [-1] * length
        for k, (idx, source) in enumerate(zip(indices, sources)):
            if s.startswith(source, idx):
                replacement_map[idx] = k
        result: list[str] = []
        i = 0
        while i < length:
            if ~replacement_map[i]:
                result.append(targets[replacement_map[i]])
                i += len(sources[replacement_map[i]])
            else:
                result.append(s[i])
                i += 1
        return "".join(result)
