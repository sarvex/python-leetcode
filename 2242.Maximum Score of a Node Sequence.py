from collections import defaultdict
from typing import List

class Solution:
   def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
       """Optimized DFS with pruning for maximum score node sequence

       Intuition:
          We aim to find a sequence of 4 distinct nodes (a-b-c-d) where each consecutive
           pair is connected. A naive DFS is exponential, but we can prune by bounding the
           best achievable remaining score with the global maximum node score.
       Approach:
           - Build an adjacency list of the graph.
           - Use DFS to explore sequences up to length 4, tracking the current score.
           - Apply pruning: if current_score + (4 - depth) * ms <= max_score, no need to continue.
           - Iterate start nodes in descending score order to tighten the pruning bound early.
       Complexity:
           - Time: Exponential in the worst case, but practical due to strong pruning.
           - Space: O(n + m) for the graph; recursion depth is at most 4.
       """
       n = len(scores)
       max_score = -1
       ms = max(scores)
       graph: dict[int, list[int]] = defaultdict(list)
       for a, b in edges:
           graph[a].append(b)
           graph[b].append(a)

       sorted_nodes = sorted(range(n), key=lambda x: scores[x], reverse=True)
       for start in sorted_nodes:
           # Stack entries: (sequence, depth, current_score)
           stack: list[tuple[list[int], int, int]] = [([start], 1, scores[start])]
           while stack:
               sequence, depth, current_score = stack.pop()
               if depth == 4:
                   if current_score > max_score:
                       max_score = current_score
                   continue
               # Prune if upper bound cannot beat current best
               if current_score + (4 - depth) * ms <= max_score:
                   continue
               last = sequence[-1]
               for nei in graph[last]:
                   if nei in sequence:
                       continue
                   # push extended path
                   stack.append((sequence + [nei], depth + 1, current_score + scores[nei]))
       return max_score
