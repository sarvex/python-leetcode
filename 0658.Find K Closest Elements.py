class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        """Sort by distance to target and return k closest elements sorted.

        Intuition:
        Sort elements by their absolute distance to x, take the k closest,
        then sort the result to maintain order.

        Approach:
        1. Sort the array by absolute distance to x (ties broken by value due to stable sort).
        2. Take the first k elements.
        3. Sort the selected elements in ascending order.

        Complexity:
        Time: O(n log n)
        Space: O(n)
        """
        arr.sort(key=lambda val: abs(val - x))
        return sorted(arr[:k])
