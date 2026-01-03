class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        _min = -float('inf')
        for x in nums:
            if _min < x - k:
                _min = x - k
                answer += 1
            elif _min < x + k:
                _min = _min + 1
                answer += 1
        return answer
