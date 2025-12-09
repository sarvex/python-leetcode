from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dic = {}
        dic2 = {}
        res = 0
        MOD = 10**9 + 7

        for num in nums:
            # Check if num can be 'k'
            if num % 2 == 0 and (num // 2) in dic2:
                res = (res + dic2[num // 2]) % MOD

            # Check if num can be 'j'
            if (num * 2) in dic:
                count_i = dic[num * 2]
                if num in dic2:
                    dic2[num] += count_i
                else:
                    dic2[num] = count_i

            # Update 'i' count
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        return res
