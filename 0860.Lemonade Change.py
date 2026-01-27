class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """Greedy change-making using available five and ten dollar bills.

        Intuition:
        Process each customer in order, greedily giving change with the
        largest bills first. A $10 bill is more versatile to save $5 bills
        for $20 customers.

        Approach:
        1. Track count of $5 and $10 bills
        2. For $5: no change needed, increment fives
        3. For $10: give one $5 as change
        4. For $20: prefer giving one $10 + one $5, else three $5s

        Complexity:
        Time: O(n) where n is the number of bills
        Space: O(1)
        """
        five_count = 0
        ten_count = 0
        for bill in bills:
            if bill == 5:
                five_count += 1
            elif bill == 10:
                ten_count += 1
                five_count -= 1
            else:
                if ten_count:
                    ten_count -= 1
                    five_count -= 1
                else:
                    five_count -= 3
            if five_count < 0:
                return False
        return True
