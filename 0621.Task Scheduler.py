from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """Find minimum intervals to schedule all tasks with cooldown constraint.

        Intuition:
            The most frequent task determines the minimum time. We arrange
            tasks in frames of size (n+1), with the most frequent task anchoring
            each frame. Idle slots fill the gaps.

        Approach:
            1. Count frequency of each task.
            2. Find the maximum frequency and how many tasks share it.
            3. The answer is max(total_tasks, (max_freq - 1) * (n + 1) + count_of_max).

        Complexity:
            Time: O(n) where n is the number of tasks
            Space: O(1) since there are at most 26 distinct tasks
        """
        frequency = Counter(tasks)
        max_freq = max(frequency.values())
        max_freq_count = sum(count == max_freq for count in frequency.values())
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_count)
