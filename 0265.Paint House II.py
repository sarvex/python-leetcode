from math import inf


class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        """Dynamic programming with k colors, tracking minimum cost excluding current color.

        Intuition:
            For each house, the minimum cost of painting it color j depends on
            the minimum cost among all other colors for the previous house.

        Approach:
            1. Initialize the DP array with the first house costs.
            2. For each subsequent house, compute the new cost for each color
               by adding the current paint cost to the minimum of all other
               colors from the previous house.
            3. Return the minimum value in the final DP array.

        Complexity:
            Time: O(n * k^2) where n is the number of houses and k is the number of colors
            Space: O(k) for the DP arrays
        """
        num_houses, num_colors = len(costs), len(costs[0])
        prev_costs = costs[0][:]
        for i in range(1, num_houses):
            curr_costs = costs[i][:]
            for j in range(num_colors):
                min_other = min(prev_costs[h] for h in range(num_colors) if h != j)
                curr_costs[j] += min_other
            prev_costs = curr_costs
        return min(prev_costs)
