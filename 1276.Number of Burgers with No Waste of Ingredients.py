class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        """Make burgers with no waste of ingredients.

        Intuition:
            Solve the system of linear equations: 4x + 2y = tomatoSlices, x + y = cheeseSlices.

        Approach:
            Derive y = (4*cheeseSlices - tomatoSlices) / 2 and x = cheeseSlices - y.
            Return empty list if the solution is not valid (non-integer or negative).

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        remainder = 4 * cheeseSlices - tomatoSlices
        small_burgers = remainder // 2
        jumbo_burgers = cheeseSlices - small_burgers
        return (
            []
            if remainder % 2 or small_burgers < 0 or jumbo_burgers < 0
            else [jumbo_burgers, small_burgers]
        )
