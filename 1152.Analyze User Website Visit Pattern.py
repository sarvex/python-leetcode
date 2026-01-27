from collections import Counter, defaultdict


class Solution:
    def mostVisitedPattern(
        self, username: list[str], timestamp: list[int], website: list[str]
    ) -> list[str]:
        """Find the most visited 3-sequence website pattern.

        Intuition:
            Group visits by user sorted by time, then enumerate all 3-site
            subsequences per user and count distinct patterns across users.

        Approach:
            Sort visits by timestamp, group sites per user. For each user,
            generate all unique 3-site combinations. Count pattern frequencies
            and return the lexicographically smallest most frequent pattern.

        Complexity:
            Time: O(n^3) where n is the max visits per user
            Space: O(n^3) for storing patterns
        """
        user_sites: dict[str, list[str]] = defaultdict(list)
        for user, _, site in sorted(
            zip(username, timestamp, website), key=lambda x: x[1]
        ):
            user_sites[user].append(site)

        pattern_count: Counter[tuple[str, ...]] = Counter()
        for sites in user_sites.values():
            length = len(sites)
            unique_patterns: set[tuple[str, ...]] = set()
            if length > 2:
                for i in range(length - 2):
                    for j in range(i + 1, length - 1):
                        for k in range(j + 1, length):
                            unique_patterns.add((sites[i], sites[j], sites[k]))
            for pattern in unique_patterns:
                pattern_count[pattern] += 1
        return list(sorted(pattern_count.items(), key=lambda x: (-x[1], x[0]))[0][0])
