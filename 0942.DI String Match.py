class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        """Greedy assignment using low/high pointers for D/I pattern.

        Intuition:
            For 'I' (increase), use the smallest available number to maximize
            room for future increases. For 'D' (decrease), use the largest
            available number similarly.

        Approach:
            1. Maintain low and high pointers starting at 0 and len(s).
            2. For each 'I', append low and increment it.
            3. For each 'D', append high and decrement it.
            4. Append the remaining value (low == high) at the end.

        Complexity:
            Time: O(n) — single pass through the string
            Space: O(n) — output array
        """
        low, high = 0, len(s)
        result = []
        for char in s:
            if char == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result
