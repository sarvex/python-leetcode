class Solution:
    def __init__(self) -> None:
        self.buf4: list[str | None] = [None] * 4
        self.buf4_index = self.buf4_size = 0

    def read(self, buf: list[str], n: int) -> int:
        """Buffered Read with Internal State for Multiple Calls.

        Intuition:
            Since read can be called multiple times, we need to preserve
            leftover characters from previous read4 calls between invocations.

        Approach:
            Maintain an internal buffer and position tracking across calls.
            When the internal buffer is exhausted, call read4 to refill it.
            Copy characters from the internal buffer to the destination
            until n characters are read or EOF is reached.

        Complexity:
            Time: O(n) reading at most n characters per call
            Space: O(1) fixed internal buffer of size 4
        """
        output_index = 0
        while output_index < n:
            if self.buf4_index == self.buf4_size:
                self.buf4_size = read4(self.buf4)
                self.buf4_index = 0
                if self.buf4_size == 0:
                    break
            while output_index < n and self.buf4_index < self.buf4_size:
                buf[output_index] = self.buf4[self.buf4_index]
                self.buf4_index += 1
                output_index += 1
        return output_index
