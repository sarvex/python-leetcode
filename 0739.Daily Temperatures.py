from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic Stack - Find the next greater element

        Intuition:
        For each temperature, we need to find the first day in the future with a higher temperature.
        This is a classic "next greater element" problem which can be efficiently solved using a monotonic stack.

        Approach:
        1. Initialize an answer array with zeros (default if no warmer day exists)
        2. Use a stack to keep track of indices of temperatures
        3. For each temperature:
           a. While current temperature is greater than the temperature at the stack's top index:
              - Pop the stack and calculate the waiting days
           b. Push current index to the stack
        4. Return the answer array

        Complexity:
        Time: O(n) where n is the length of temperatures array (each element is pushed and popped at most once)
        Space: O(n) for the stack and answer array
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i, current_temp in enumerate(temperatures):
            # Process all temperatures in stack that are lower than current temperature
            while stack and temperatures[stack[-1]] < current_temp:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day

            # Add current day to the stack
            stack.append(i)

        return answer
