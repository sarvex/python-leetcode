from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Generate all possible permutations of the input array.

        Intuition:
            We can solve this using backtracking, which is a systematic way to generate
            all possible combinations by exploring all potential candidates and backtracking
            when we reach an invalid state. Alternatively, we can use Python's built-in
            permutations function for a concise solution.

        Approach:
            1. Backtracking: Build permutations incrementally by choosing one element at a time
               and recursively generating permutations of the remaining elements.
            2. Built-in: Use Python's itertools.permutations for a concise solution.

        Complexity:
            Time: O(n!), where n is the length of nums (we generate n! permutations)
            Space: O(n!), to store all the permutations
        """
        # Solution using backtracking
        return self._permute_backtracking(nums)

        # Alternatively, using Python's built-in permutations
        # from itertools import permutations
        # return list(permutations(nums))

    def _permute_backtracking(self, nums: List[int]) -> List[List[int]]:
        """Generate permutations using backtracking approach."""
        result = []

        def backtrack(curr: List[int], remaining: List[int]) -> None:
            # Base case: if no elements remain, we've found a permutation
            if not remaining:
                result.append(curr[:])
                return

            # Try each remaining element as the next element in the permutation
            for i, num in enumerate(remaining):
                # Add current element to permutation
                curr.append(num)
                # Recursively generate permutations without the chosen element
                backtrack(curr, remaining[:i] + remaining[i+1:])
                # Backtrack by removing the last element
                curr.pop()

        backtrack([], nums)
        return result

    def _permute_iterative(self, nums: List[int]) -> List[List[int]]:
        """Generate permutations using an iterative approach."""
        # Start with an empty permutation
        result = [[]]

        for num in nums:
            new_perms = []
            # For each existing permutation, insert the current number at every possible position
            for perm in result:
                for i in range(len(perm) + 1):
                    # Create a new permutation with num inserted at position i
                    new_perm = perm[:i] + [num] + perm[i:]
                    new_perms.append(new_perm)
            result = new_perms

        return result

    def _permute_builtin(self, nums: List[int]) -> List[List[int]]:
        """Generate permutations using Python's built-in function."""
        from itertools import permutations
        return list(permutations(nums))
