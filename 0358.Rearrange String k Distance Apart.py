from collections import Counter, deque
from heapq import heapify, heappop, heappush


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """Rearrange string so same characters are k distance apart using greedy heap.

        Intuition:
            Greedily place the most frequent character first. Use a cooldown
            queue to enforce the k-distance constraint before reusing a character.

        Approach:
            Build a max-heap of (-frequency, character) pairs. Pop the most
            frequent character, append it to the result, decrement its count,
            and push it into a cooldown queue. When the queue reaches size k,
            release the front element back into the heap if it still has
            remaining count. If the heap empties before building the full
            string, return empty string.

        Complexity:
            Time: O(n log n) where n is the length of the string
            Space: O(n)
        """
        heap = [(-freq, char) for char, freq in Counter(s).items()]
        heapify(heap)
        cooldown = deque()
        result = []
        while heap:
            neg_freq, char = heappop(heap)
            freq = -neg_freq
            result.append(char)
            cooldown.append((freq - 1, char))
            if len(cooldown) >= k:
                remaining, released_char = cooldown.popleft()
                if remaining:
                    heappush(heap, (-remaining, released_char))
        return "" if len(result) != len(s) else "".join(result)
