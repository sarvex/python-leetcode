class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """Generate FizzBuzz sequence using modulo checks.

        Intuition:
            Classic problem: replace multiples of 3 with "Fizz", multiples
            of 5 with "Buzz", and multiples of both with "FizzBuzz".

        Approach:
            1. Iterate from 1 to n inclusive.
            2. Check divisibility by 15 first (both 3 and 5), then 3, then 5.
            3. Otherwise, convert the number to string.

        Complexity:
            Time: O(n)
            Space: O(n) for the result list
        """
        result: list[str] = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
