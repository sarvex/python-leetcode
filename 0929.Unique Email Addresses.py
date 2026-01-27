class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """String normalization with dot removal and plus truncation.

        Intuition:
            Normalize each email by removing dots from the local name and
            ignoring everything after '+', then count distinct addresses.

        Approach:
            1. Split each email into local and domain parts.
            2. Remove all dots from the local name.
            3. Truncate the local name at the first '+' if present.
            4. Recombine and add to a set for deduplication.

        Complexity:
            Time: O(n * k) where k is average email length
            Space: O(n * k)
        """
        unique: set[str] = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            if (plus_idx := local.find("+")) != -1:
                local = local[:plus_idx]
            unique.add(local + "@" + domain)
        return len(unique)
