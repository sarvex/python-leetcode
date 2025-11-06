from typing import List
import heapq


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        """Tagline: DSU for static components + per-component min-heap with lazy deletions.

        Intuition:
            Connectivity never changes—offline nodes remain in their grids. So we can precompute
            connected components once using DSU. For each component, we need to quickly obtain the
            smallest online station id; a min-heap per component with lazy deletions suffices.

        Approach:
            - Build DSU on stations 1..c and union all connections.
            - For each node i, push i into the heap of its component root.
            - Maintain an `online` boolean list. On [2, x], mark offline.
            - On [1, x]: if `online[x]`, return x. Otherwise, clean the heap of x's component by
              popping all offline tops until an online station emerges or heap empties.
              Return that id or -1.

        Complexity:
            Time: O((c + n) α(c) + q log c) amortized
            Space: O(c)
        """

        parent: List[int] = list(range(c + 1))
        rank: List[int] = [0] * (c + 1)

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for u, v in connections:
            union(u, v)

        # Compress paths once for stable component ids
        for i in range(1, c + 1):
            parent[i] = find(i)

        # Heaps per component root
        heaps: List[List[int]] = [[] for _ in range(c + 1)]
        for i in range(1, c + 1):
            heaps[parent[i]].append(i)
        for h in heaps:
            if h:
                heapq.heapify(h)

        online: List[bool] = [False] * (c + 1)
        for i in range(1, c + 1):
            online[i] = True

        def clean_top(root: int) -> int:
            h = heaps[root]
            while h and not online[h[0]]:
                heapq.heappop(h)
            return h[0] if h else -1

        ans: List[int] = []
        for t, x in queries:
            if t == 1:
                if online[x]:
                    ans.append(x)
                else:
                    root = parent[x]
                    ans.append(clean_top(root))
            else:  # t == 2
                online[x] = False

        return ans
