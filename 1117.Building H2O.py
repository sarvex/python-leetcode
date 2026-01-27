from collections.abc import Callable
from threading import Semaphore


class H2O:
    """Synchronize hydrogen and oxygen threads to form water molecules.

    Intuition:
        Each water molecule requires exactly two hydrogen atoms and one oxygen
        atom, so we must barrier hydrogen and oxygen in a 2:1 ratio.

    Approach:
        Use a hydrogen semaphore initialized to 2 and an oxygen semaphore
        initialized to 0. Two hydrogen threads must acquire before oxygen is
        signaled. After oxygen releases, it replenishes the hydrogen semaphore.

    Complexity:
        Time: O(1) per atom release
        Space: O(1) for the two semaphores
    """

    def __init__(self) -> None:
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(0)

    def hydrogen(self, release_hydrogen: Callable[[], None]) -> None:
        self.hydrogen_semaphore.acquire()
        release_hydrogen()
        if self.hydrogen_semaphore._value == 0:
            self.oxygen_semaphore.release()

    def oxygen(self, release_oxygen: Callable[[], None]) -> None:
        self.oxygen_semaphore.acquire()
        release_oxygen()
        self.hydrogen_semaphore.release(2)
