from collections import Counter, deque


class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        """BFS with bitmask to find minimum stickers to spell target.

        Intuition:
            Represent the state of which target characters have been covered
            as a bitmask. BFS explores states level by level, where each level
            corresponds to using one more sticker.

        Approach:
            1. Use BFS starting from state 0 (no characters covered).
            2. For each state, try applying each sticker to cover additional
               target characters.
            3. Track visited states to avoid reprocessing.
            4. Return the BFS level when the fully-covered state is reached.

        Complexity:
            Time: O(2^n * m * L) where n is target length, m is sticker count, L is sticker length
            Space: O(2^n) for visited states
        """
        num_chars = len(target)
        queue = deque([0])
        visited = [False] * (1 << num_chars)
        visited[0] = True
        steps = 0
        while queue:
            for _ in range(len(queue)):
                current_state = queue.popleft()
                if current_state == (1 << num_chars) - 1:
                    return steps
                for sticker in stickers:
                    char_count = Counter(sticker)
                    next_state = current_state
                    for i, char in enumerate(target):
                        if (current_state >> i & 1) == 0 and char_count[char] > 0:
                            char_count[char] -= 1
                            next_state |= 1 << i
                    if not visited[next_state]:
                        visited[next_state] = True
                        queue.append(next_state)
            steps += 1
        return -1
