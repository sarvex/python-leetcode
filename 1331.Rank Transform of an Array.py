from bisect import bisect_right


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """Replace each element with its rank in the sorted unique array.

        Intuition:
            The rank of an element is its 1-based position in the sorted
            unique values. Binary search gives this efficiently.

        Approach:
            Sort unique elements, then use bisect_right on the sorted array
            to determine each element's rank.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        sorted_unique = sorted(set(arr))
        return [bisect_right(sorted_unique, x) for x in arr]
