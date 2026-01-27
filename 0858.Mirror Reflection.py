from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """GCD reduction to determine which corner the laser beam hits.

        Intuition:
        The laser reflects and eventually hits a corner receptor. By reducing
        p and q by their GCD, the parity of the resulting values determines
        which receptor is hit.

        Approach:
        1. Compute GCD of p and q
        2. Divide both by GCD to get reduced values
        3. Use parity: if both odd -> receptor 1, p odd q even -> receptor 0,
           p even q odd -> receptor 2

        Complexity:
        Time: O(log(min(p, q))) for GCD computation
        Space: O(1)
        """
        common = gcd(p, q)
        reduced_p = (p // common) % 2
        reduced_q = (q // common) % 2
        if reduced_p == 1 and reduced_q == 1:
            return 1
        return 0 if reduced_p == 1 else 2
