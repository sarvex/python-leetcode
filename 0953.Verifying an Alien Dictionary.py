class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        """Column-by-column comparison using alien character ordering.

        Intuition:
            Check character positions column by column. If all previous columns
            are equal, the current column must be non-decreasing. If any column
            is strictly increasing everywhere, remaining columns don't matter.

        Approach:
            1. Map each alien character to its rank in the given order.
            2. For each column position, compare adjacent words.
            3. If previous word's character > current word's character, return False.
            4. If all pairs are strictly ordered in some column, return True early.

        Complexity:
            Time: O(n * m) — n words of max length m
            Space: O(1) — fixed-size character map (26 chars)
        """
        char_rank = {char: rank for rank, char in enumerate(order)}
        for col in range(20):
            prev_rank = -1
            is_all_distinct = True
            for word in words:
                curr_rank = -1 if col >= len(word) else char_rank[word[col]]
                if prev_rank > curr_rank:
                    return False
                if prev_rank == curr_rank:
                    is_all_distinct = False
                prev_rank = curr_rank
            if is_all_distinct:
                return True
        return True
