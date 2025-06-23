from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        Greedy approach with sorting to minimize the number of partitions.

        Intuition:
        To minimize the number of partitions, we want to include as many elements as possible
        in each partition while ensuring the max difference is at most k. Sorting the array
        allows us to easily track the min and max values in each potential partition.

        Approach:
        1. Sort the array to group similar elements together
        2. Start a new partition with the first element
        3. For each element, if its difference from the partition's min exceeds k,
           start a new partition
        4. Return the total number of partitions needed

        Complexity:
        Time: O(n log n) due to sorting
        Space: O(1) as we only use constant extra space
        """
        if k == 0:
            return len(set(nums))

        nums.sort()
        result, min_val = 1, nums[0]

        for num in nums:
            if num - min_val > k:
                min_val = num
                result += 1

        return result
