class Solution:
    def intersect(self, quadTree1: "Node", quadTree2: "Node") -> "Node":
        """Compute logical OR of two quad-trees using recursive merge.

        Intuition:
            If either tree is a leaf with value True, the result is that leaf.
            If either is a leaf with value False, the result is the other tree.
            Otherwise, recursively merge all four quadrants and simplify.

        Approach:
            1. Base cases: both leaves, or one leaf with known value.
            2. Recursively merge topLeft, topRight, bottomLeft, bottomRight.
            3. If all four children are leaves with the same value, collapse
               into a single leaf.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(n)
        """

        def dfs(tree1: "Node", tree2: "Node") -> "Node":
            if tree1.isLeaf and tree2.isLeaf:
                return Node(tree1.val or tree2.val, True)
            if tree1.isLeaf:
                return tree1 if tree1.val else tree2
            if tree2.isLeaf:
                return tree2 if tree2.val else tree1
            result = Node()
            result.topLeft = dfs(tree1.topLeft, tree2.topLeft)
            result.topRight = dfs(tree1.topRight, tree2.topRight)
            result.bottomLeft = dfs(tree1.bottomLeft, tree2.bottomLeft)
            result.bottomRight = dfs(tree1.bottomRight, tree2.bottomRight)
            all_leaves = (
                result.topLeft.isLeaf
                and result.topRight.isLeaf
                and result.bottomLeft.isLeaf
                and result.bottomRight.isLeaf
            )
            same_value = (
                result.topLeft.val
                == result.topRight.val
                == result.bottomLeft.val
                == result.bottomRight.val
            )
            if all_leaves and same_value:
                result = result.topLeft
            return result

        return dfs(quadTree1, quadTree2)
