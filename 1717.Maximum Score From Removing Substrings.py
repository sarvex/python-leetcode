class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """Greedy approach to maximize score by prioritizing higher-value removals.

        Intuition:
        To maximize score, we should prioritize removing the substring that gives
        higher points first. By processing characters sequentially and greedily
        removing high-value pairs, we can achieve optimal results.

        Approach:
        1. Determine which removal ('ab' or 'ba') gives higher score
        2. Process string character by character, greedily removing high-value pairs
        3. Count remaining characters for lower-value pair removal
        4. When encountering non-a/b characters, process accumulated counts

        Complexity:
        Time: O(n) - single pass through string
        Space: O(1) - only using counters
        """
        def _process_remaining_pairs(count_first: int, count_second: int, score: int) -> int:
            """Calculate score from remaining character pairs."""
            return min(count_first, count_second) * score

        # Ensure we prioritize higher-scoring removal first
        first_char, second_char = ('a', 'b') if x >= y else ('b', 'a')
        high_score, low_score = (x, y) if x >= y else (y, x)

        total_score = 0
        first_count = 0
        second_count = 0

        for char in s:
            if char == first_char:
                first_count += 1
            elif char == second_char:
                if first_count > 0:
                    # Greedily form high-scoring pair
                    total_score += high_score
                    first_count -= 1
                else:
                    second_count += 1
            else:
                # Process accumulated counts when hitting separator
                total_score += _process_remaining_pairs(first_count, second_count, low_score)
                first_count = second_count = 0

        # Process any remaining counts
        total_score += _process_remaining_pairs(first_count, second_count, low_score)

        return total_score
