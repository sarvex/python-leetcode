class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        """Simulation approach to count total bottles consumed.

        Intuition:
        Start with initial bottles and drink them all. Then repeatedly exchange
        empty bottles for new ones until we don't have enough empties to exchange.

        Approach:
        Track total consumed bottles and current empty bottles. While we have
        enough empties to exchange, trade them for new bottles, drink those,
        and accumulate empties. Each exchange reduces empties by (num_exchange - 1)
        since we trade num_exchange empties for 1 full bottle.

        Complexity:
        Time: O(num_bottles / num_exchange) - loop runs until empties < num_exchange
        Space: O(1) - constant extra space
        """
        total_consumed = num_bottles
        empty_bottles = num_bottles

        while empty_bottles >= num_exchange:
            empty_bottles -= num_exchange - 1
            total_consumed += 1

        return total_consumed
