class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """Track bottles drunk and empty bottles separately for exchange.

        Intuition
        ---------
        Consume all available bottles, then exchange empty bottles when enough are
        accumulated. The exchange cost increases by 1 after each exchange.

        Approach
        --------
        - Use two counters: numDrunk for total consumed, numEmpty for available empties
        - While bottles remain or exchange is possible:
          - If enough empties exist, exchange for new bottle and increment cost
          - Drink all available bottles, converting them to empties
        - Return total drunk count

        Complexity
        ----------
        - Time: O(n) where n is number of exchanges performed
        - Space: O(1) constant extra space
        """
        numDrunk = 0
        numEmpty = 0
        while numBottles > 0 or numEmpty >= numExchange:
            if numEmpty >= numExchange:
                numBottles += 1
                numEmpty -= numExchange
                numExchange += 1
            numDrunk += numBottles
            numEmpty += numBottles
            numBottles = 0
        return numDrunk
