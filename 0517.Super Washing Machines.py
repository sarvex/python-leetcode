class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        """Greedy approach tracking net flow through each machine.

        Intuition:
            Each machine needs to reach the average number of dresses. The
            bottleneck is the maximum of absolute cumulative surplus and
            individual machine surplus.

        Approach:
            Compute the target per machine. Track running surplus. The answer
            is the maximum of the absolute running surplus and any single
            machine's excess over target.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        count = len(machines)
        target, remainder = divmod(sum(machines), count)
        if remainder:
            return -1
        result = running_surplus = 0
        for dresses in machines:
            excess = dresses - target
            running_surplus += excess
            result = max(result, abs(running_surplus), excess)
        return result
