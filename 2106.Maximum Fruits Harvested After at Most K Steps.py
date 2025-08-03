from typing import List
import bisect

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        max_res = 0
        left = bisect.bisect_left(fruits, [startPos - k, float("-inf")]) # >=
        right = bisect.bisect_right(fruits, [startPos, float("inf")]) # >


        curr_subarray_sum = sum([fruits[i][1] for i in range(left, right)])
        max_res = curr_subarray_sum

        for i in range(right, len(fruits)):
            curr_subarray_sum += fruits[i][1]
            right_loc = fruits[i][0]

            if right_loc - startPos > k:
                break

            while min(abs(right_loc - startPos), abs(startPos- fruits[left][0])) + right_loc - fruits[left][0] > k:
                curr_subarray_sum -= fruits[left][1]
                left += 1
            max_res = max(max_res, curr_subarray_sum)

        return max_res
