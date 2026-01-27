from collections import defaultdict


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] > self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        return True


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """Union-Find to merge accounts sharing common emails.

        Intuition:
            If two accounts share an email, they belong to the same person.
            Union-Find efficiently groups accounts with shared emails.

        Approach:
            1. Map each email to the first account index that owns it.
            2. If an email is seen again, union the current and previous accounts.
            3. Group all emails by their root account.
            4. Return sorted email lists with the account name.

        Complexity:
            Time: O(n * alpha(n) + E * log(E)) where E is total emails
            Space: O(n + E) for union-find and email grouping
        """
        union_find = UnionFind(len(accounts))
        email_to_account: dict[str, int] = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_account:
                    union_find.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        groups: dict[int, set[str]] = defaultdict(set)
        for i, (_, *emails) in enumerate(accounts):
            root = union_find.find(i)
            groups[root].update(emails)
        return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
