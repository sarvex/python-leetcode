class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        """Stack-based simulation to compute exclusive execution time per function.

        Intuition:
        Use a stack to track currently running functions. When a new function starts,
        charge elapsed time to the previous function on the stack.

        Approach:
        1. Maintain a stack of function IDs and track current timestamp.
        2. On 'start', charge elapsed time to the stack top, push new function.
        3. On 'end', pop the function, charge time including the end timestamp.
        4. Update current time after each log entry.

        Complexity:
        Time: O(L) where L is the number of log entries
        Space: O(n)
        """
        result = [0] * n
        stack = []
        current_time = -1
        for log in logs:
            parts = log.split(":")
            func_id = int(parts[0])
            timestamp = int(parts[2])
            if parts[1] == "start":
                if stack:
                    result[stack[-1]] += timestamp - current_time
                stack.append(func_id)
                current_time = timestamp
            else:
                func_id = stack.pop()
                result[func_id] += timestamp - current_time + 1
                current_time = timestamp + 1
        return result
