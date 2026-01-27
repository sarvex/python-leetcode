from collections.abc import Callable
from threading import Semaphore


class ZeroEvenOdd:
    """Print the series 0102030405... using three threads.

    Intuition:
        Three semaphores coordinate the zero, odd, and even threads so that
        zero always prints between consecutive numbers.

    Approach:
        The zero thread prints 0 and then signals either the odd or even
        semaphore based on the current iteration parity. The odd and even
        threads wait for their respective signals and release the zero
        semaphore after printing.

    Complexity:
        Time: O(n) across all threads
        Space: O(1) for the three semaphores
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.zero_semaphore = Semaphore(1)
        self.even_semaphore = Semaphore(0)
        self.odd_semaphore = Semaphore(0)

    def zero(self, print_number: Callable[[int], None]) -> None:
        for i in range(self.n):
            self.zero_semaphore.acquire()
            print_number(0)
            if i % 2 == 0:
                self.odd_semaphore.release()
            else:
                self.even_semaphore.release()

    def even(self, print_number: Callable[[int], None]) -> None:
        for i in range(2, self.n + 1, 2):
            self.even_semaphore.acquire()
            print_number(i)
            self.zero_semaphore.release()

    def odd(self, print_number: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_semaphore.acquire()
            print_number(i)
            self.zero_semaphore.release()
