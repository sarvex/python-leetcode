from heapq import heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """Build the longest string with no three consecutive identical chars.

        Intuition:
            Greedily use the most frequent character, switching to the next
            most frequent when two consecutive are already placed.

        Approach:
            Use a max-heap (negated counts) to always pick the character
            with the highest remaining count. If the top character would
            create three consecutive, pop the next character instead.

        Complexity:
            Time: O((a + b + c) * log 3) which is O(a + b + c)
            Space: O(a + b + c) for the result
        """
        heap: list[list[int | str]] = []
        if a > 0:
            heappush(heap, [-a, "a"])
        if b > 0:
            heappush(heap, [-b, "b"])
        if c > 0:
            heappush(heap, [-c, "c"])

        result: list[str] = []
        while heap:
            current = heappop(heap)
            if (
                len(result) >= 2
                and result[-1] == current[1]
                and result[-2] == current[1]
            ):
                if not heap:
                    break
                next_char = heappop(heap)
                result.append(next_char[1])
                if -next_char[0] > 1:
                    next_char[0] += 1
                    heappush(heap, next_char)
                heappush(heap, current)
            else:
                result.append(current[1])
                if -current[0] > 1:
                    current[0] += 1
                    heappush(heap, current)

        return "".join(result)
