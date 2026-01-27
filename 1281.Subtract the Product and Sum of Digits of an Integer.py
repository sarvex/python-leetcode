class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """Subtract the product and sum of digits of an integer.

        Intuition:
            Extract each digit, accumulate the product and sum, then return the difference.

        Approach:
            Use divmod to extract digits one by one, multiplying into product and
            adding into digit_sum, then return product - digit_sum.

        Complexity:
            Time: O(d) where d is the number of digits
            Space: O(1)
        """
        product, digit_sum = 1, 0
        while n:
            n, digit = divmod(n, 10)
            product *= digit
            digit_sum += digit
        return product - digit_sum
