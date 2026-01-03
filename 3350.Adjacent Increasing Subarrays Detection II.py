class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        """
        Find the maximum number of adjacent increasing subarrays.
        
        Intuition:
        We can find all increasing subarrays and then determine the maximum number of adjacent ones.
        
        Approach:
        1. Traverse the array to find increasing subarrays
        2. For each increasing subarray of length 'cur_cnt':
           - The maximum adjacent pairs is min(previous_count, current_count) or current_count//2
           - Update the answer with the maximum value found
        3. Continue until all elements are processed
        
        Complexity:
        Time: O(n) - Single pass through the array
        Space: O(1) - Constant extra space used
        """
        n = len(nums)
        pre_cnt = 0
        cur_cnt = 0
        i = 0
        ans = 1  # At least one subarray exists (the whole array)

        while i < n - 1:
            # Skip non-increasing elements
            if nums[i] >= nums[i + 1]:
                i += 1
                pre_cnt = 1  # Reset previous count for non-increasing pairs
                continue
            
            # Find the length of current increasing subarray
            start = i
            i += 1
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            
            # Calculate current subarray length and update answer
            cur_cnt = i - start
            ans = max(ans, min(pre_cnt, cur_cnt), cur_cnt // 2)
            pre_cnt = cur_cnt
            
        return ans
