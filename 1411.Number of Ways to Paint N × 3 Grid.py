class Solution:
    """
    1411. Number of Ways to Paint N × 3 Grid
    
    You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).
    
    Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.
    """
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        # color2: count of patterns in a row using exactly 2 colors (e.g., ABA)
        # color3: count of patterns in a row using exactly 3 colors (e.g., ABC)
        
        # Base case for n=1:
        # 3 colors options for 1st cell * 2 options for 2nd * 1 option for 3rd = 6 ways (ABC, etc)
        # 3 colors options for 1st cell * 2 options for 2nd * 1 option for 3rd (must match 1st) = 6 ways (ABA, etc)
        color2 = 6
        color3 = 6
        
        for _ in range(n - 1):
            # Transitions:
            # If previous row was 2-color pattern (ABA):
            #   - Can generate 3 new 2-color patterns (BAB, BCB, CAC)
            #   - Can generate 2 new 3-color patterns (BAC, CAB)
            # If previous row was 3-color pattern (ABC):
            #   - Can generate 2 new 2-color patterns (BAB, BCA)
            #   - Can generate 2 new 3-color patterns (BCA, CAB)
            
            new_color2 = (3 * color2 + 2 * color3) % MOD
            new_color3 = (2 * color2 + 2 * color3) % MOD
            
            color2, color3 = new_color2, new_color3
            
        return (color2 + color3) % MOD