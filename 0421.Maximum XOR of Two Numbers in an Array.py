class Trie:
    """Binary trie for storing and querying XOR values bit by bit."""

    __slots__ = ("children",)

    def __init__(self) -> None:
        """Initialize trie node with two possible children (0 and 1)."""
        self.children: list[Trie | None] = [None, None]

    def insert(self, value: int) -> None:
        """Insert a number into the trie bit by bit from the highest bit."""
        node = self
        for bit_position in range(30, -1, -1):
            bit = value >> bit_position & 1
            if node.children[bit] is None:
                node.children[bit] = Trie()
            node = node.children[bit]

    def search(self, value: int) -> int:
        """Find the maximum XOR achievable with any inserted number."""
        node = self
        result = 0
        for bit_position in range(30, -1, -1):
            bit = value >> bit_position & 1
            if node.children[bit ^ 1]:
                result |= 1 << bit_position
                node = node.children[bit ^ 1]
            else:
                node = node.children[bit]
        return result


class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        """Binary trie to maximize XOR by greedily choosing opposite bits.

        Intuition:
            To maximize XOR between two numbers, at each bit position we want
            to pick the opposite bit. A trie lets us efficiently find the best
            complement for each number.

        Approach:
            1. Insert all numbers into a binary trie.
            2. For each number, search the trie greedily choosing the opposite
               bit at each level to maximize XOR.
            3. Return the maximum XOR found.

        Complexity:
            Time: O(n * 31) where n is the number of elements.
            Space: O(n * 31) for the trie nodes.
        """
        trie = Trie()
        for num in nums:
            trie.insert(num)
        return max(trie.search(num) for num in nums)
