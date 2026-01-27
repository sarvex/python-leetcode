from collections import deque


HOLE, MOUSE_START, CAT_START = 0, 1, 2
MOUSE_TURN, CAT_TURN = 0, 1
MOUSE_WIN, CAT_WIN, TIE = 1, 2, 0


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        """Topological game theory with backward induction BFS.

        Intuition:
            This is a combinatorial game where we determine the outcome from
            known terminal states (mouse at hole = mouse wins, cat catches
            mouse = cat wins) and propagate backwards through all reachable
            game states.

        Approach:
            1. Initialize terminal states: mouse at hole (mouse wins) and
               mouse at same position as cat (cat wins).
            2. Track the degree (number of moves) for each state.
            3. BFS backward from terminal states: if a previous state can
               reach a winning state for the current player, mark it as won.
               Otherwise, decrement degree and mark as lost when no moves left.
            4. Return the result for the initial state.

        Complexity:
            Time: O(n^3) where n is the number of nodes
            Space: O(n^2)
        """

        def get_prev_states(state: tuple[int, int, int]) -> list[tuple[int, int, int]]:
            mouse_pos, cat_pos, turn = state
            prev_turn = turn ^ 1
            predecessors: list[tuple[int, int, int]] = []
            if prev_turn == CAT_TURN:
                for prev_cat in graph[cat_pos]:
                    if prev_cat != HOLE:
                        predecessors.append((mouse_pos, prev_cat, prev_turn))
            else:
                for prev_mouse in graph[mouse_pos]:
                    predecessors.append((prev_mouse, cat_pos, prev_turn))
            return predecessors

        num_nodes = len(graph)
        result = [[[0, 0] for _ in range(num_nodes)] for _ in range(num_nodes)]
        degree = [[[0, 0] for _ in range(num_nodes)] for _ in range(num_nodes)]
        for mouse in range(num_nodes):
            for cat in range(1, num_nodes):
                degree[mouse][cat][MOUSE_TURN] = len(graph[mouse])
                degree[mouse][cat][CAT_TURN] = len(graph[cat])
            for neighbor in graph[HOLE]:
                degree[mouse][neighbor][CAT_TURN] -= 1

        queue: deque[tuple[int, int, int]] = deque()
        for cat in range(1, num_nodes):
            result[0][cat][MOUSE_TURN] = result[0][cat][CAT_TURN] = MOUSE_WIN
            queue.append((0, cat, MOUSE_TURN))
            queue.append((0, cat, CAT_TURN))
        for pos in range(1, num_nodes):
            result[pos][pos][MOUSE_TURN] = result[pos][pos][CAT_TURN] = CAT_WIN
            queue.append((pos, pos, MOUSE_TURN))
            queue.append((pos, pos, CAT_TURN))

        while queue:
            state = queue.popleft()
            outcome = result[state[0]][state[1]][state[2]]
            for prev_state in get_prev_states(state):
                prev_mouse, prev_cat, prev_turn = prev_state
                if result[prev_mouse][prev_cat][prev_turn] == TIE:
                    is_winning_move = (
                        outcome == MOUSE_WIN and prev_turn == MOUSE_TURN
                    ) or (outcome == CAT_WIN and prev_turn == CAT_TURN)
                    if is_winning_move:
                        result[prev_mouse][prev_cat][prev_turn] = outcome
                        queue.append(prev_state)
                    else:
                        degree[prev_mouse][prev_cat][prev_turn] -= 1
                        if degree[prev_mouse][prev_cat][prev_turn] == 0:
                            result[prev_mouse][prev_cat][prev_turn] = outcome
                            queue.append(prev_state)
        return result[MOUSE_START][CAT_START][MOUSE_TURN]
