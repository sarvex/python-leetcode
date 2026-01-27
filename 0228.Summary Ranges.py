class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """Two-pointer scan to merge consecutive numbers into ranges.

        Intuition:
            Walk through the sorted array, extending a range as long as
            consecutive numbers differ by exactly one.

        Approach:
            1. Use two pointers: start and end of the current range.
            2. Extend end while the next number is consecutive.
            3. Format as "start->end" or just "start" if single element.

        Complexity:
            Time: O(n)
            Space: O(n) for the result
        """

        def format_range(start: int, end: int) -> str:
            return str(nums[start]) if start == end else f"{nums[start]}->{nums[end]}"

        pos = 0
        length = len(nums)
        result: list[str] = []
        while pos < length:
            end = pos
            while end + 1 < length and nums[end + 1] == nums[end] + 1:
                end += 1
            result.append(format_range(pos, end))
            pos = end + 1
        return result
