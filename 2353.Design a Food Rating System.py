from heapq import heappop, heappush
from collections import defaultdict
from typing import Dict, List, Tuple

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]) -> None:
        """Heap-backed food rating system

        Intuition:
            Maintain, for each cuisine, a max-heap of foods by rating and name. Updates push a new entry; queries lazily pop stale ones.

        Approach:
            - Keep a map `self.foods` from food -> (rating, cuisine) as the single source of truth.
            - For each cuisine, keep a heap of tuples (-rating, food). Use negative rating to simulate a max-heap.
            - On changeRating, update `self.foods` and push the new tuple to the cuisine heap (lazy deletion).
            - On highestRated, pop from the heap while the top doesn't match the current rating in `self.foods`.

        Complexity:
            - changeRating: O(log n) per update.
            - highestRated: Amortized O(log n) due to lazy deletions.
        """
        self.foods: Dict[str, Tuple[int, str]] = {}
        self.rated_cuisine: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (rating, cuisine)
            heappush(self.rated_cuisine[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        """Update a food's rating with lazy heap update

        Intuition:
            Push the new (rating, food) entry and let queries discard stale entries.

        Approach:
            - Look up the cuisine from `self.foods`.
            - Overwrite the current rating in `self.foods`.
            - Push (-newRating, food) to that cuisine's heap.

        Complexity:
            - Time: O(log n)
            - Space: O(1) extra (heap may temporarily grow due to lazy deletion)
        """
        _, curr_cuisine = self.foods[food]
        self.foods[food] = (newRating, curr_cuisine)
        heappush(self.rated_cuisine[curr_cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        """Return the highest rated food for a cuisine

        Intuition:
            Pop stale entries until the heap top matches the current rating in `self.foods`.

        Approach:
            - While heap top's rating doesn't equal the latest rating for that food, pop it.
            - Return the food name at the top.

        Complexity:
            - Amortized Time: O(log n)
            - Space: O(1)
        """
        heap = self.rated_cuisine[cuisine]
        while heap and -heap[0][0] != self.foods[heap[0][1]][0]:
            heappop(heap)
        return heap[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
