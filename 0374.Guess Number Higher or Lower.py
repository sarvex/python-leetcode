# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass  # Placeholder - actual implementation is provided by LeetCode


class Solution:
    def guessNumber(self, n: int) -> int:
        """Binary search to find the picked number.
        Intuition: Since we get feedback on whether our guess is too high or too low,
        we can use binary search to efficiently narrow down the search space.
        Approach: Use binary search to find the number. At each step, we make a guess
        and adjust our search range based on the feedback from the guess API.
        Complexity:
        Time: O(log n) - binary search halves the search space with each iteration
        Space: O(1) - only using a constant amount of extra space
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            match result:
                case 0:
                    return mid
                case -1:
                    right = mid - 1  # Our guess is higher than the picked number
                case _:
                    left = mid + 1   # result == 1, our guess is lower than the picked number
        return -1  # This should never be reached given the problem constraints
