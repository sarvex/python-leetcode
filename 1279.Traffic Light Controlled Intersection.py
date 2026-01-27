from collections.abc import Callable
from threading import Lock


class TrafficLight:
    """Traffic light controlled intersection using mutex.

    Intuition:
        Only one car can pass through the intersection at a time, and the light
        must be switched when a car from a different road arrives.

    Approach:
        Use a lock to ensure mutual exclusion. Track the current green road and
        only call turnGreen when the arriving car is on a different road.

    Complexity:
        Time: O(1) per carArrived call
        Space: O(1)
    """

    def __init__(self) -> None:
        self.lock = Lock()
        self.current_road = 1

    def carArrived(
        self,
        carId: int,
        roadId: int,
        direction: int,
        turnGreen: Callable[[], None],
        crossCar: Callable[[], None],
    ) -> None:
        self.lock.acquire()
        if self.current_road != roadId:
            self.current_road = roadId
            turnGreen()
        crossCar()
        self.lock.release()
