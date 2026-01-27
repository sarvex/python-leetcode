from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        """Find all invalid transactions based on amount and city rules.

        Intuition:
            A transaction is invalid if amount > 1000 or if another transaction
            with the same name occurs in a different city within 60 minutes.

        Approach:
            Group transactions by name. For each transaction, check the amount
            threshold and compare against all previous transactions of the same
            name for the city/time conflict rule. Collect invalid indices.

        Complexity:
            Time: O(n^2) in worst case for same-name comparisons
            Space: O(n)
        """
        name_transactions: dict[str, list[tuple[int, str, int]]] = defaultdict(list)
        invalid_indices: set[int] = set()
        for i, transaction in enumerate(transactions):
            name, time_str, amount_str, city = transaction.split(",")
            time, amount = int(time_str), int(amount_str)
            name_transactions[name].append((time, city, i))
            if amount > 1000:
                invalid_indices.add(i)
            for prev_time, prev_city, prev_idx in name_transactions[name]:
                if prev_city != city and abs(time - prev_time) <= 60:
                    invalid_indices.add(i)
                    invalid_indices.add(prev_idx)
        return [transactions[i] for i in invalid_indices]
