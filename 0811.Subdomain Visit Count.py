from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        """Count visits for all subdomains using a counter.

        Intuition:
            Each domain entry contributes its count to itself and all parent
            subdomains. Split at each '.' to generate all subdomains.

        Approach:
            1. For each entry, parse the visit count.
            2. Add the count to every subdomain (split at spaces and dots).
            3. Format and return results.

        Complexity:
            Time: O(n * d) where n = number of entries, d = max domain depth
            Space: O(n * d)
        """
        visit_counts: Counter[str] = Counter()
        for entry in cpdomains:
            count = int(entry[: entry.index(" ")])
            for i, char in enumerate(entry):
                if char in " .":
                    visit_counts[entry[i + 1 :]] += count
        return [f"{count} {domain}" for domain, count in visit_counts.items()]
