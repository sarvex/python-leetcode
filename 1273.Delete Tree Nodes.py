from collections import defaultdict


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: list[int], value: list[int]) -> int:
        """Delete subtrees whose node values sum to zero and count remaining.

        Intuition:
            Process the tree bottom-up. If a subtree's total value is zero,
            remove all its nodes. The count of remaining nodes propagates up.

        Approach:
            Build an adjacency list from parent array. DFS from the root,
            computing subtree sums and node counts. If a subtree sum equals
            zero, set its node count to zero, effectively pruning it.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(node: int) -> tuple[int, int]:
            subtree_sum, node_count = value[node], 1
            for child in children[node]:
                child_sum, child_count = dfs(child)
                subtree_sum += child_sum
                node_count += child_count
            if subtree_sum == 0:
                node_count = 0
            return subtree_sum, node_count

        children: dict[int, list[int]] = defaultdict(list)
        for i in range(1, nodes):
            children[parent[i]].append(i)
        return dfs(0)[1]
