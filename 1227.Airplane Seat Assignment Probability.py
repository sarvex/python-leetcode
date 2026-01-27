class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """Airplane seat assignment probability.

        Intuition:
            The first person picks randomly. Through mathematical induction,
            for n > 1 the probability that the last person gets their seat
            is always 1/2.

        Approach:
            Return 1.0 for n=1 (only one person, gets their seat) and 0.5
            for all n > 1 based on the mathematical proof.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return 1.0 if n == 1 else 0.5
