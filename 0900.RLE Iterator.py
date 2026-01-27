class RLEIterator:
    """Run-length encoded iterator consuming elements on demand.

    Intuition:
        Maintain a pointer into the encoding array and track how many
        elements have been consumed within the current run.

    Approach:
        1. Store the encoding and maintain a run index and offset within
           the current run.
        2. On each next(n) call, skip entire runs that are fully consumed,
           then advance the offset within the current run.
        3. Return the value of the current run, or -1 if exhausted.

    Complexity:
        Time: O(n) amortized per next call over all calls.
        Space: O(1) beyond the encoding storage.
    """

    def __init__(self, encoding: list[int]) -> None:
        self.encoding = encoding
        self.run_index = 0
        self.offset = 0

    def next(self, n: int) -> int:
        while self.run_index < len(self.encoding):
            remaining_in_run = self.encoding[self.run_index] - self.offset
            if remaining_in_run < n:
                n -= remaining_in_run
                self.run_index += 2
                self.offset = 0
            else:
                self.offset += n
                return self.encoding[self.run_index + 1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
