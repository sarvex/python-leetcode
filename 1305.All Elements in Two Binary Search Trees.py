class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> list[int]:
        """Merge all elements from two BSTs into a sorted list.

        Intuition:
            Inorder traversal of each BST produces a sorted list; merge the two
            sorted lists in linear time.

        Approach:
            Perform inorder DFS on both trees to get sorted lists, then merge them
            using a two-pointer technique.

        Complexity:
            Time: O(m + n)
            Space: O(m + n)
        """

        def inorder(node: TreeNode | None, result: list[int]) -> None:
            if node is None:
                return
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)

        def merge(first: list[int], second: list[int]) -> list[int]:
            merged: list[int] = []
            i = j = 0
            while i < len(first) and j < len(second):
                if first[i] <= second[j]:
                    merged.append(first[i])
                    i += 1
                else:
                    merged.append(second[j])
                    j += 1
            merged.extend(first[i:])
            merged.extend(second[j:])
            return merged

        sorted_first: list[int] = []
        sorted_second: list[int] = []
        inorder(root1, sorted_first)
        inorder(root2, sorted_second)
        return merge(sorted_first, sorted_second)
