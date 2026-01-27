from heapq import heapify, heappop, heappush


class Solution:
    def minBuildTime(self, blocks: list[int], split: int) -> int:
        """Minimum time to build all blocks using worker splitting.

        Intuition:
            This is analogous to Huffman coding: always merge the two smallest
            tasks, adding the split cost to create a combined task.

        Approach:
            Use a min-heap. Repeatedly pop the two smallest blocks, discard one,
            and push back the other plus the split cost. The remaining element
            is the minimum total time.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        heapify(blocks)
        while len(blocks) > 1:
            heappop(blocks)
            heappush(blocks, heappop(blocks) + split)
        return blocks[0]
