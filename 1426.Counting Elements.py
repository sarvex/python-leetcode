from collections import Counter


class Solution:
    def countElements(self, arr: list[int]) -> int:
        """Count elements where element + 1 also exists in the array.

        Intuition:
            For each distinct value, if value + 1 exists in the array,
            all occurrences of value count toward the result.

        Approach:
            Count frequencies of each element. For each value with a
            non-zero count for value + 1, add its frequency to the result.

        Complexity:
            Time: O(n) for counting and iterating
            Space: O(n) for the frequency counter
        """
        frequency = Counter(arr)
        return sum(count for value, count in frequency.items() if frequency[value + 1])
