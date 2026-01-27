class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        """Binary search on the minimum radius that covers all houses.

        Intuition:
            If a radius r works, any larger radius also works. This
            monotonic property allows binary search on the answer.

        Approach:
            Sort both arrays. Binary search for the minimum radius. For
            each candidate radius, use a two-pointer check to verify all
            houses fall within some heater's range.

        Complexity:
            Time: O((m + n) log D) where D is the search range
            Space: O(1) aside from sorting
        """
        houses.sort()
        heaters.sort()

        def can_cover(radius: int) -> bool:
            num_houses, num_heaters = len(houses), len(heaters)
            house_idx = heater_idx = 0
            while house_idx < num_houses:
                if heater_idx >= num_heaters:
                    return False
                lower_bound = heaters[heater_idx] - radius
                upper_bound = heaters[heater_idx] + radius
                if houses[house_idx] < lower_bound:
                    return False
                if houses[house_idx] > upper_bound:
                    heater_idx += 1
                else:
                    house_idx += 1
            return True

        left, right = 0, int(1e9)
        while left < right:
            mid = (left + right) >> 1
            if can_cover(mid):
                right = mid
            else:
                left = mid + 1
        return left
