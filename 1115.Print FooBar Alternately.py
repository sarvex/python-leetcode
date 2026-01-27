from collections.abc import Callable
from threading import Semaphore


class FooBar:
    """Print 'foo' and 'bar' alternately n times using semaphores.

    Intuition:
        Two semaphores can enforce strict alternation between two threads.

    Approach:
        Initialize the foo semaphore with count 1 and bar with 0. Each thread
        acquires its own semaphore before printing and releases the other
        thread's semaphore after printing.

    Complexity:
        Time: O(n) for each thread
        Space: O(1) for the two semaphores
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.foo_semaphore = Semaphore(1)
        self.bar_semaphore = Semaphore(0)

    def foo(self, print_foo: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.foo_semaphore.acquire()
            print_foo()
            self.bar_semaphore.release()

    def bar(self, print_bar: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.bar_semaphore.acquire()
            print_bar()
            self.foo_semaphore.release()
