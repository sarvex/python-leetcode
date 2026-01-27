class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """Monotonic stack greedy removal of k digits.

        Intuition:
            To minimize the resulting number, greedily remove digits that
            are larger than the next digit, using a monotonic increasing stack.

        Approach:
            1. Iterate through digits, maintaining a monotonic increasing stack.
            2. While the stack top is greater than the current digit and
               removals remain, pop from the stack and decrement k.
            3. Push the current digit onto the stack.
            4. Take only the first (len(num) - k) digits from the stack.
            5. Strip leading zeros and return "0" if empty.

        Complexity:
            Time: O(n) where n is the length of num
            Space: O(n) for the stack
        """
        stack: list[str] = []
        remaining = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return "".join(stack[:remaining]).lstrip("0") or "0"
