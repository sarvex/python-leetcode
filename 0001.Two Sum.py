class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find two numbers in the list that add up to the target.

        Intuition:
        We can use a hash map to store the complement of each number as we iterate through the list.
        For each number, we check if its complement (target - current number) exists in the map.
        If it does, we've found our pair. If not, we add the current number to the map.

        Approach:
        1. Initialize an empty dictionary to store number to index mappings
        2. Iterate through the list with both index and value
        3. For each number, calculate its complement (target - current number)
        4. Check if the complement exists in the dictionary
        5. If found, return the indices of the complement and current number
        6. If not found, add the current number and its index to the dictionary

        Complexity:
        Time: O(n) - We traverse the list once
        Space: O(n) - In the worst case, we store all n elements in the dictionary
        """
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []  # As per problem constraints, exactly one solution exists
