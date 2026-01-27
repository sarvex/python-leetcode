class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        """Find common restaurants with minimum index sum between two lists.

        Intuition:
            Map restaurants from the second list to their indices, then scan
            the first list to find common entries with the smallest combined
            index sum.

        Approach:
            1. Build an index map for list2 entries.
            2. Iterate through list1, checking for common restaurants.
            3. Track the minimum index sum and collect all restaurants achieving it.

        Complexity:
            Time: O(m + n) where m and n are the list lengths
            Space: O(n)
        """
        result: list[str] = []
        index_map = {restaurant: i for i, restaurant in enumerate(list2)}
        min_index_sum = 2000
        for i, restaurant in enumerate(list1):
            if restaurant in index_map:
                index_sum = i + index_map[restaurant]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_index_sum:
                    result.append(restaurant)
        return result
