from collections import deque


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        """BFS with pruning for minimum insertions to clear the board.

        Intuition:
            Try inserting hand balls at each position on the board. After
            insertion, recursively remove groups of 3+ consecutive same-color
            balls. Use BFS to find the minimum steps.

        Approach:
            Sort the hand for deduplication. Use BFS over (board, hand)
            states. For each state, try inserting each hand ball at each
            board position, pruning redundant placements. After insertion,
            recursively collapse groups of 3+ same-color balls. Track
            visited states to avoid re-exploration.

        Complexity:
            Time: O(m^n * n!) where m = board length, n = hand length
            Space: O(states) for the visited set
        """

        def remove_consecutive(s: str, index: int) -> str:
            if index < 0:
                return s
            left = right = index
            while left > 0 and s[left - 1] == s[index]:
                left -= 1
            while right + 1 < len(s) and s[right + 1] == s[index]:
                right += 1
            length = right - left + 1
            if length >= 3:
                new_s = s[:left] + s[right + 1 :]
                return remove_consecutive(new_s, left - 1)
            return s

        hand = "".join(sorted(hand))
        queue = deque([(board, hand, 0)])
        visited = {(board, hand)}

        while queue:
            current_board, current_hand, step = queue.popleft()
            for i in range(len(current_board) + 1):
                for j in range(len(current_hand)):
                    if j > 0 and current_hand[j] == current_hand[j - 1]:
                        continue
                    if i > 0 and current_board[i - 1] == current_hand[j]:
                        continue

                    should_pick = False
                    if i < len(current_board) and current_board[i] == current_hand[j]:
                        should_pick = True
                    if (
                        0 < i < len(current_board)
                        and current_board[i - 1] == current_board[i]
                        and current_board[i] != current_hand[j]
                    ):
                        should_pick = True

                    if should_pick:
                        new_board = remove_consecutive(
                            current_board[:i] + current_hand[j] + current_board[i:], i
                        )
                        new_hand = current_hand[:j] + current_hand[j + 1 :]
                        if not new_board:
                            return step + 1
                        if (new_board, new_hand) not in visited:
                            queue.append((new_board, new_hand, step + 1))
                            visited.add((new_board, new_hand))

        return -1
