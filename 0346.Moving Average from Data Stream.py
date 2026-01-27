class MovingAverage:
    """Computes the moving average of the last `size` values in a data stream.

    Intuition:
        A circular buffer avoids shifting elements when the window slides,
        and maintaining a running sum avoids recomputing the sum from scratch.

    Approach:
        Allocate a fixed-size buffer. On each new value, compute the buffer
        index via modulo, subtract the old value at that position from the
        running sum, store the new value, and add it to the running sum.
        Return the sum divided by the current window size.

    Complexity:
        Time: O(1) per next call
        Space: O(n) where n is the window size
    """

    def __init__(self, size: int) -> None:
        """Initialize the circular buffer with the given window size."""
        self.buffer = [0] * size
        self.running_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        """Add a new value and return the current moving average."""
        idx = self.count % len(self.buffer)
        self.running_sum += val - self.buffer[idx]
        self.buffer[idx] = val
        self.count += 1
        return self.running_sum / min(self.count, len(self.buffer))
