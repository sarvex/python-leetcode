class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """Hierholzer's algorithm on a de Bruijn graph to visit all combinations.

        Intuition:
            Model each (n-1)-digit prefix as a graph node with k outgoing edges
            (appending digits 0..k-1). An Eulerian circuit visits every edge
            (i.e., every n-digit combination) exactly once.

        Approach:
            1. Start from node 0 and perform DFS, marking edges as visited.
            2. After exploring all edges from a node, append the last digit used.
            3. Append the starting prefix at the end and reverse.

        Complexity:
            Time: O(k^n)
            Space: O(k^n)
        """

        def euler_dfs(node: int) -> None:
            for digit in range(k):
                edge = node * 10 + digit
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    next_node = edge % modulus
                    euler_dfs(next_node)
                    result.append(str(digit))

        modulus = 10 ** (n - 1)
        visited_edges: set[int] = set()
        result: list[str] = []
        euler_dfs(0)
        result.append("0" * (n - 1))
        return "".join(result)
