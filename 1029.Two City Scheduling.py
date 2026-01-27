class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        """Two City Scheduling using greedy sort by cost difference.

        Intuition:
            Sort people by the relative savings of sending them to city A
            versus city B. Send the first half to city A and the rest to city B.

        Approach:
            Sort costs by (cost_a - cost_b). The first n people go to city A
            (cheapest relative advantage), and the remaining n go to city B.

        Complexity:
            Time: O(n log n)
            Space: O(1) excluding sort
        """
        costs.sort(key=lambda x: x[0] - x[1])
        half = len(costs) >> 1
        return sum(costs[i][0] + costs[i + half][1] for i in range(half))
