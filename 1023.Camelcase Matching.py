class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        """Camelcase Matching with two-pointer pattern check.

        Intuition:
            A query matches the pattern if the pattern is a subsequence of the
            query and all non-matched characters in the query are lowercase.

        Approach:
            For each query, use two pointers to match against the pattern.
            Skip lowercase characters in the query that don't match. If an
            uppercase character doesn't match, return False. After exhausting
            the pattern, verify remaining query characters are all lowercase.

        Complexity:
            Time: O(q * (m + n)) where q is number of queries
            Space: O(q) for result list
        """

        def is_match(query: str, target: str) -> bool:
            query_len, target_len = len(query), len(target)
            qi = ti = 0
            while ti < target_len:
                while (
                    qi < query_len and query[qi] != target[ti] and query[qi].islower()
                ):
                    qi += 1
                if qi == query_len or query[qi] != target[ti]:
                    return False
                qi, ti = qi + 1, ti + 1
            while qi < query_len and query[qi].islower():
                qi += 1
            return qi == query_len

        return [is_match(q, pattern) for q in queries]
