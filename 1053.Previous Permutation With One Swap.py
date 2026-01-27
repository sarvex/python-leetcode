class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        """Find the largest permutation smaller than arr with one swap.

        Intuition:
            Find the rightmost descent and swap with the largest smaller element
            to its right to get the previous permutation.

        Approach:
            Scan right-to-left for a descent, then find the rightmost element
            smaller than the descent point (skipping duplicates) and swap.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        n = len(arr)
        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                for j in range(n - 1, i - 1, -1):
                    if arr[j] < arr[i - 1] and arr[j] != arr[j - 1]:
                        arr[i - 1], arr[j] = arr[j], arr[i - 1]
                        return arr
        return arr
