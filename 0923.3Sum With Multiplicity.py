from collections import Counter


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        """Counting approach with frequency map for three-sum combinations.

        Intuition:
            For each pair (a, b), the third element c = target - a - b.
            By maintaining a running frequency count of elements after the
            current position, we can efficiently count valid triplets.

        Approach:
            1. Count all element frequencies.
            2. Iterate through each element as the middle element b.
            3. Decrement b's count (to avoid reuse as third element).
            4. For each prior element a, look up count of c = target - a - b.
            5. Sum all valid triplet counts modulo 10^9 + 7.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        modulo = 10**9 + 7
        frequency = Counter(arr)
        result = 0
        for mid_idx, mid_val in enumerate(arr):
            frequency[mid_val] -= 1
            for first_val in arr[:mid_idx]:
                third_val = target - first_val - mid_val
                result = (result + frequency[third_val]) % modulo
        return result
