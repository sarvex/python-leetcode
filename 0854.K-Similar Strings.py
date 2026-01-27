from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        """BFS exploring minimum adjacent swaps to transform s1 into s2.

        Intuition:
            Each swap fixes at least one position. BFS over string states finds
            the minimum number of swaps since each level represents one more swap.

        Approach:
            1. Start BFS from s1, target is s2
            2. At each state, find the first mismatched position
            3. Try swapping with later positions that would fix that mismatch
            4. Prune by only swapping characters that also fix their own position

        Complexity:
            Time: O(n! / (n-k)!) in worst case where k is the answer
            Space: O(n! / (n-k)!) for visited states
        """

        def generate_next_states(current: str) -> list[str]:
            first_mismatch = 0
            while current[first_mismatch] == s2[first_mismatch]:
                first_mismatch += 1
            candidates: list[str] = []
            for swap_pos in range(first_mismatch + 1, length):
                if (
                    current[swap_pos] == s2[first_mismatch]
                    and current[swap_pos] != s2[swap_pos]
                ):
                    candidates.append(
                        s2[: first_mismatch + 1]
                        + current[first_mismatch + 1 : swap_pos]
                        + current[first_mismatch]
                        + current[swap_pos + 1 :]
                    )
            return candidates

        queue: deque[str] = deque([s1])
        visited: set[str] = {s1}
        swap_count = 0
        length = len(s1)
        while True:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == s2:
                    return swap_count
                for next_state in generate_next_states(current):
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)
            swap_count += 1
