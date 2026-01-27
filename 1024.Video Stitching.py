class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        """Video Stitching using greedy jump game approach.

        Intuition:
            This is equivalent to the jump game problem. For each position,
            track the farthest reachable endpoint from any clip starting there.

        Approach:
            Build an array where each index stores the maximum end time of
            clips starting at that index. Then greedily sweep left to right,
            tracking the farthest reach and counting jumps when we must extend.

        Complexity:
            Time: O(n + time)
            Space: O(time)
        """
        farthest = [0] * time
        for start, end in clips:
            if start < time:
                farthest[start] = max(farthest[start], end)
        jumps = max_reach = previous_end = 0
        for i, reach in enumerate(farthest):
            max_reach = max(max_reach, reach)
            if max_reach <= i:
                return -1
            if previous_end == i:
                jumps += 1
                previous_end = max_reach
        return jumps
