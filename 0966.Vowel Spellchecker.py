class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        """Three-tier lookup: exact match, case-insensitive, vowel-insensitive.

        Intuition:
            Check queries against the wordlist with increasing flexibility:
            first exact match, then case-insensitive match, then vowel-insensitive
            match where all vowels are treated as wildcards.

        Approach:
            1. Build an exact-match set from wordlist.
            2. Build a case-insensitive map (first occurrence wins).
            3. Build a vowel-insensitive map with vowels replaced by '*'.
            4. For each query, try exact, then lowercase, then vowel pattern.

        Complexity:
            Time: O((n + q) * m) — building maps and querying, m = word length
            Space: O(n * m) — storing maps and set
        """

        def vowel_pattern(word: str) -> str:
            return "".join("*" if char in "aeiou" else char for char in word)

        exact_set = set(wordlist)
        lowercase_map: dict[str, str] = {}
        pattern_map: dict[str, str] = {}
        for word in wordlist:
            lowered = word.lower()
            lowercase_map.setdefault(lowered, word)
            pattern_map.setdefault(vowel_pattern(lowered), word)

        result = []
        for query in queries:
            if query in exact_set:
                result.append(query)
                continue
            lowered_query = query.lower()
            if lowered_query in lowercase_map:
                result.append(lowercase_map[lowered_query])
                continue
            query_pattern = vowel_pattern(lowered_query)
            if query_pattern in pattern_map:
                result.append(pattern_map[query_pattern])
                continue
            result.append("")
        return result
