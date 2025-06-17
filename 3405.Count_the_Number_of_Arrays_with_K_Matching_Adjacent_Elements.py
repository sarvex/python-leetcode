MOD = 10**9 + 7
MX = 10**5

fact = [0] * MX
inv_fact = [0] * MX


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Optimized combinatorial approach using precomputation with local functions
        
        Intuition:
        - We need arrays of length n with exactly k matching adjacent elements
        - For each matching pair, we need to decide which positions have matching elements
        - Once positions are decided, we need to assign values to each position
        
        Approach:
        1. Choose k positions out of (n-1) possible adjacent pairs: C(n-1, k)
        2. Choose m possible values for the first element
        3. For each non-matching position, we have (m-1) choices
        4. Total formula: C(n-1, k) * m * (m-1)^(n-1-k)
        
        Complexity:
        - Time: O(MX + log(m)) - dominated by precomputation and modular exponentiation
        - Space: O(MX) - for storing factorials and inverses
        """
        # Local function for binary exponentiation
        def qpow(x, n):
            res = 1
            while n:
                if n & 1:
                    res = res * x % MOD
                x = x * x % MOD
                n >>= 1
            return res
        
        # Local function to initialize factorial arrays
        def init():
            if fact[0] != 0:
                return
            fact[0] = 1
            for i in range(1, MX):
                fact[i] = fact[i - 1] * i % MOD
            inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
            for i in range(MX - 1, 0, -1):
                inv_fact[i - 1] = inv_fact[i] * i % MOD
        
        # Local function for combination calculation
        def comb(n, m):
            return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD
        
        # Initialize factorial arrays
        init()
        
        # Calculate using the formula: C(n-1, k) * m * (m-1)^(n-1-k)
        return comb(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: n = 3, m = 2, k = 1
    print(sol.countGoodArrays(3, 2, 1))  # Output: 4

    # Example 2: n = 4, m = 2, k = 2
    print(sol.countGoodArrays(4, 2, 2))  # Output: 6

    # Example 3: n = 5, m = 2, k = 0
    print(sol.countGoodArrays(5, 2, 0))  # Output: 2
