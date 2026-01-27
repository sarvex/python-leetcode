class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        """Two-pointer greedy: spend power on cheapest, gain power from most expensive.

        Intuition:
            Sort tokens. Use smallest tokens face-up (spend power, gain score)
            and largest tokens face-down (spend score, gain power) to maximize score.

        Approach:
            1. Sort tokens in ascending order.
            2. Use two pointers: left for face-up, right for face-down.
            3. If power >= tokens[left], play face-up (gain score).
            4. Else if score > 0, play face-down from right (gain power).
            5. Track maximum score achieved.

        Complexity:
            Time: O(n log n) — sorting dominates
            Space: O(1) — constant extra space (in-place sort)
        """
        tokens.sort()
        max_score = score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score, left = score + 1, left + 1
                max_score = max(max_score, score)
            elif score:
                power += tokens[right]
                score, right = score - 1, right - 1
            else:
                break
        return max_score
