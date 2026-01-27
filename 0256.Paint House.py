class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        """Dynamic programming with rolling state for minimum paint cost.

        Intuition:
            Each house can be painted one of three colors, and no two adjacent
            houses can share the same color. Track the minimum cost for each
            color choice using rolling variables.

        Approach:
            Maintain three variables for the cumulative cost of painting the
            previous house each color. For each new house, compute the new
            cost for each color as its paint cost plus the minimum of the
            other two previous costs.

        Complexity:
            Time: O(n) where n is the number of houses
            Space: O(1)
        """
        cost_red = cost_green = cost_blue = 0
        for red, green, blue in costs:
            cost_red, cost_green, cost_blue = (
                min(cost_green, cost_blue) + red,
                min(cost_red, cost_blue) + green,
                min(cost_red, cost_green) + blue,
            )
        return min(cost_red, cost_green, cost_blue)
