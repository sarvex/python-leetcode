from functools import cache


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """Binary search within memoized recursion for optimal egg drop strategy.

        Intuition:
            For each state (floors, eggs), find the optimal floor to drop
            from by binary searching for the crossover point where the
            break and no-break cases are balanced.

        Approach:
            1. Define a recursive function with floors remaining and eggs available.
            2. Base cases: 0 floors needs 0 moves; 1 egg needs linear search.
            3. Binary search for the floor where break-case and survive-case
               costs cross, minimizing the worst case.
            4. Memoize all states.

        Complexity:
            Time: O(n * k * log n)
            Space: O(n * k)
        """

        @cache
        def search(floors: int, eggs: int) -> int:
            if floors < 1:
                return 0
            if eggs == 1:
                return floors
            low, high = 1, floors
            while low < high:
                mid = (low + high + 1) >> 1
                break_case = search(mid - 1, eggs - 1)
                survive_case = search(floors - mid, eggs)
                if break_case <= survive_case:
                    low = mid
                else:
                    high = mid - 1
            return max(search(low - 1, eggs - 1), search(floors - low, eggs)) + 1

        return search(n, k)
