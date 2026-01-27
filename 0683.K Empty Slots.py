class BinaryIndexedTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        total = 0
        while index:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        """Binary Indexed Tree to track lit bulbs with k empty gap.

        Intuition:
            When a bulb is turned on, check if there exists another lit bulb
            exactly k+1 positions away with all bulbs between them off. A BIT
            efficiently counts lit bulbs in any range.

        Approach:
            1. Maintain a BIT and a visited array tracking which bulbs are on.
            2. For each newly lit bulb, check both k+1 positions to the left
               and right.
            3. If the target position has a lit bulb and the range between them
               has zero other lit bulbs, return the current day.

        Complexity:
            Time: O(n log n) for n bulbs with BIT operations
            Space: O(n) for the BIT and visited array
        """
        num_bulbs = len(bulbs)
        tree = BinaryIndexedTree(num_bulbs)
        visited = [False] * (num_bulbs + 1)
        for day, position in enumerate(bulbs, 1):
            tree.update(position, 1)
            visited[position] = True
            left_target = position - k - 1
            if (
                left_target > 0
                and visited[left_target]
                and tree.query(position - 1) - tree.query(left_target) == 0
            ):
                return day
            right_target = position + k + 1
            if (
                right_target <= num_bulbs
                and visited[right_target]
                and tree.query(right_target - 1) - tree.query(position) == 0
            ):
                return day
        return -1
