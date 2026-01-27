from bisect import bisect_left


"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution:
    def findSolution(self, customfunction: "CustomFunction", z: int) -> list[list[int]]:
        """Find all positive integer pairs (x, y) where f(x, y) == z.

        Intuition:
            Since f is monotonically increasing in both x and y, for each x
            we can binary search for the correct y value.

        Approach:
            Iterate x from 1 to z. For each x, binary search over y in [1, z]
            using the monotonicity of f. If f(x, y) equals z, add the pair.

        Complexity:
            Time: O(z log z)
            Space: O(1) excluding output
        """
        result: list[list[int]] = []
        for x in range(1, z + 1):
            y = 1 + bisect_left(
                range(1, z + 1), z, key=lambda y: customfunction.f(x, y)
            )
            if customfunction.f(x, y) == z:
                result.append([x, y])
        return result
