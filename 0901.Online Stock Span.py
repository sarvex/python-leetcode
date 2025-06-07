class StockSpanner:
    """Monotonic Stack approach to solve the Online Stock Span problem

    Intuition:
    When we see a new price, we need to find how many consecutive previous prices
    were less than or equal to the current price. This is a perfect use case for
    a monotonic stack where we can efficiently track spans.

    Approach:
    Use a stack to store pairs of (price, span). For each new price:
    1. Pop elements from stack while current price >= price at top of stack
    2. Add spans of all popped elements to current span
    3. Push the new (price, span) pair onto stack
    4. Return the span

    Complexity:
    Time: O(1) amortized for next() - each price is pushed and popped at most once
    Space: O(n) where n is the number of prices processed
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        # Pop elements while stack top has price <= current price
        # Add their spans to current span
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span

        # Push current price and its span to stack
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
