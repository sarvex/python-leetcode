from collections import Counter


class Solution:
    def findDuplicateSubtrees(self, root: "TreeNode | None") -> list["TreeNode | None"]:
        """Serialize subtrees via DFS and detect duplicates using a counter.

        Intuition:
        Serialize each subtree into a unique string representation. Count occurrences
        and collect roots whose serialization appears exactly twice.

        Approach:
        1. DFS to serialize each subtree as "val,left_serial,right_serial".
        2. Use a Counter to track how many times each serialization appears.
        3. When a count reaches 2, add the root to the result list.

        Complexity:
        Time: O(n^2) due to string concatenation
        Space: O(n^2)
        """

        def dfs(node: "TreeNode | None") -> str:
            if node is None:
                return "#"
            serialized = f"{node.val},{dfs(node.left)},{dfs(node.right)}"
            counter[serialized] += 1
            if counter[serialized] == 2:
                duplicates.append(node)
            return serialized

        duplicates: list["TreeNode | None"] = []
        counter: Counter[str] = Counter()
        dfs(root)
        return duplicates
