class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        """Enumerate all x^i + y^j combinations within the bound.

        Intuition:
        Since x^i and y^j grow exponentially, only a small number of powers
        need to be checked. Use a set to collect unique sums within the bound.

        Approach:
        1. Iterate powers of x while x^i <= bound
        2. For each x^i, iterate powers of y while x^i + y^j <= bound
        3. Add valid sums to a set for deduplication
        4. Handle x == 1 or y == 1 to avoid infinite loops

        Complexity:
        Time: O(log(bound)^2) for iterating powers of x and y
        Space: O(log(bound)^2) for storing unique results
        """
        result: set[int] = set()
        power_x = 1
        while power_x <= bound:
            power_y = 1
            while power_x + power_y <= bound:
                result.add(power_x + power_y)
                power_y *= y
                if y == 1:
                    break
            if x == 1:
                break
            power_x *= x
        return list(result)
