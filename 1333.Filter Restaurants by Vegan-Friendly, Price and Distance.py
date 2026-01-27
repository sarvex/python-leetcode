class Solution:
    def filterRestaurants(
        self,
        restaurants: list[list[int]],
        vegan_friendly: int,
        max_price: int,
        max_distance: int,
    ) -> list[int]:
        """Filter and sort restaurants by criteria, returning IDs.

        Intuition:
            Sort by rating then ID descending, then filter by the given constraints.

        Approach:
            Sort restaurants by (-rating, -id), then iterate and collect IDs
            of restaurants matching vegan, price, and distance filters.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        restaurants.sort(key=lambda r: (-r[1], -r[0]))
        result: list[int] = []
        for restaurant_id, _, vegan, price, distance in restaurants:
            if (
                vegan >= vegan_friendly
                and price <= max_price
                and distance <= max_distance
            ):
                result.append(restaurant_id)
        return result
