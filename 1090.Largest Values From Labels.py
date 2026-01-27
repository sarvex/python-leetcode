from collections import Counter


class Solution:
    def largestValsFromLabels(
        self, values: list[int], labels: list[int], num_wanted: int, use_limit: int
    ) -> int:
        """Select items to maximize value sum with label usage limits.

        Intuition:
            Greedily pick highest-value items while respecting per-label limits
            and total selection count.

        Approach:
            Sort items by value descending. Greedily select items, tracking
            label usage with a counter. Stop when num_wanted items are selected.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for label counter
        """
        total_value = selected_count = 0
        label_usage: Counter[int] = Counter()
        for value, label in sorted(zip(values, labels), reverse=True):
            if label_usage[label] < use_limit:
                label_usage[label] += 1
                selected_count += 1
                total_value += value
                if selected_count == num_wanted:
                    break
        return total_value
