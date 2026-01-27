from collections import defaultdict, deque


class Solution:
    def findClosestLeaf(self, root: "TreeNode | None", k: int) -> int:
        """BFS from target node on an undirected graph built from the tree.

        Intuition:
            Convert the tree into an undirected graph so we can BFS outward
            from the target node and find the nearest leaf.

        Approach:
            1. DFS to build an adjacency list linking each node to its parent
               and children.
            2. Find the node with value k.
            3. BFS from that node; the first leaf encountered is the answer.

        Complexity:
            Time: O(N)
            Space: O(N)
        """

        def build_graph(node: "TreeNode | None", parent: "TreeNode | None") -> None:
            if node:
                graph[node].append(parent)
                graph[parent].append(node)
                build_graph(node.left, node)
                build_graph(node.right, node)

        graph: dict[object, list] = defaultdict(list)
        build_graph(root, None)
        queue = deque(node for node in graph if node and node.val == k)
        visited = set(queue)
        while True:
            node = queue.popleft()
            if node:
                if node.left == node.right:
                    return node.val
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
