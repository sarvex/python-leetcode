import threading
from collections.abc import Callable


class Foo:
    """Ensure three methods execute in order using locks.

    Intuition:
        Use locks to enforce sequential execution regardless of thread
        scheduling order.

    Approach:
        Initialize two locks in acquired state. The first method releases
        lock2 after executing, the second waits on lock2 then releases
        lock3, and the third waits on lock3.

    Complexity:
        Time: O(1) per method call
        Space: O(1) for the two locks
    """

    def __init__(self) -> None:
        self.lock_second = threading.Lock()
        self.lock_third = threading.Lock()
        self.lock_second.acquire()
        self.lock_third.acquire()

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.lock_second.release()

    def second(self, print_second: Callable[[], None]) -> None:
        self.lock_second.acquire()
        print_second()
        self.lock_third.release()

    def third(self, print_third: Callable[[], None]) -> None:
        self.lock_third.acquire()
        print_third()
