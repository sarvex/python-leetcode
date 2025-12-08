import math


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for c in range(1, n + 1):
            for a in range(1, c):
                s = c * c - a * a
                b = math.isqrt(s)
                if b * b == s:
                    count += 1
        return count
