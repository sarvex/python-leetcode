class Solution:
    def peopleIndexes(self, favoriteCompanies: list[list[str]]) -> list[int]:
        """Find people whose favorite companies list is not a subset of another's.

        Intuition:
            Map company names to integer IDs for fast set operations, then check
            each person's set against all others.

        Approach:
            Assign unique integer IDs to each company name. Convert each person's
            list to a set of IDs. For each person, check if their set is a proper
            subset of any other person's set. If not, include their index.

        Complexity:
            Time: O(n^2 * m) where n is people count and m is max companies per person
            Space: O(n * m) for the sets
        """
        company_to_id: dict[str, int] = {}
        next_id = 0
        company_sets: list[set[int]] = []

        for companies in favoriteCompanies:
            for company in companies:
                if company not in company_to_id:
                    company_to_id[company] = next_id
                    next_id += 1
            company_sets.append({company_to_id[c] for c in companies})

        result: list[int] = []
        for i, set_i in enumerate(company_sets):
            is_unique = True
            for j, set_j in enumerate(company_sets):
                if i == j:
                    continue
                if not (set_i - set_j):
                    is_unique = False
                    break
            if is_unique:
                result.append(i)
        return result
