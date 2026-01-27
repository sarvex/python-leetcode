from heapq import heapify, heappop, heappush


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        """Find minimum cost to connect all sticks using a min-heap.

        Intuition:
            Always combining the two smallest sticks minimizes total cost,
            similar to Huffman coding.

        Approach:
            Use a min-heap. Repeatedly extract the two smallest sticks, combine
            them, add the cost, and push the combined stick back. Continue until
            one stick remains.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        heapify(sticks)
        total_cost = 0
        while len(sticks) > 1:
            combined = heappop(sticks) + heappop(sticks)
            total_cost += combined
            heappush(sticks, combined)
        return total_cost
