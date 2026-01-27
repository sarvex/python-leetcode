class UndergroundSystem:
    """Design an underground system to track travel times between stations.

    Intuition:
        Track check-in events per passenger and aggregate travel time
        statistics per station pair.

    Approach:
        Store check-in data (time, station) keyed by passenger id. On
        check-out, compute travel time and update running totals for the
        station pair. Average time is total time divided by trip count.

    Complexity:
        Time: O(1) for each check-in, check-out, and getAverageTime call
        Space: O(n + k) where n is active passengers and k is station pairs
    """

    def __init__(self) -> None:
        self.check_ins: dict[int, tuple[int, str]] = {}
        self.travel_data: dict[tuple[str, str], tuple[int, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.check_ins[id]
        route = (start_station, stationName)
        total_time, trip_count = self.travel_data.get(route, (0, 0))
        self.travel_data[route] = (total_time + t - start_time, trip_count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, trip_count = self.travel_data[(startStation, endStation)]
        return total_time / trip_count
