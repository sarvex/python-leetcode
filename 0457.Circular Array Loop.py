class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        """Floyd's cycle detection on a circular array with direction constraints.

        Intuition:
            Treat each index as a node pointing to the next index (wrapping around).
            Use slow/fast pointers to detect cycles, ensuring all elements in the
            cycle move in the same direction and the cycle length > 1.

        Approach:
            1. For each unvisited index, use slow and fast pointers.
            2. Advance while the direction (sign) is consistent.
            3. If slow == fast and the cycle length > 1, return True.
            4. Mark visited indices as 0 to skip them in future iterations.

        Complexity:
            Time: O(n) since each index is visited at most twice.
            Space: O(1) using in-place marking.
        """
        length = len(nums)

        def advance(index: int) -> int:
            return (index + nums[index] % length + length) % length

        for start in range(length):
            if nums[start] == 0:
                continue
            slow, fast = start, advance(start)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[advance(fast)] > 0:
                if slow == fast:
                    if slow != advance(slow):
                        return True
                    break
                slow, fast = advance(slow), advance(advance(fast))
            current = start
            while nums[current] * nums[advance(current)] > 0:
                nums[current] = 0
                current = advance(current)
        return False
