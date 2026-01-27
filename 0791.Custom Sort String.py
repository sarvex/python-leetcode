class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """Sort string by custom character ordering using a priority map.

        Intuition:
            Characters in the order string define relative priority. Characters
            not in the order can appear anywhere, so we assign them a default
            low priority.

        Approach:
            1. Build a dictionary mapping each character in order to its index
            2. Sort the string s using the dictionary as the sort key
            3. Characters not in order get priority 0 (appear first by default)

        Complexity:
            Time: O(n log n) where n is the length of s
            Space: O(n) for the sorted result
        """
        priority = {char: idx for idx, char in enumerate(order)}
        return "".join(sorted(s, key=lambda char: priority.get(char, 0)))
