class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        """Find convex hull of tree positions using Andrew's monotone chain algorithm.

        Intuition:
            The fence must enclose all trees using the minimum perimeter, which
            is the convex hull problem. We use the monotone chain approach.

        Approach:
            1. Sort points by x-coordinate, then y-coordinate.
            2. Build lower hull by iterating left to right, removing points
               that make a clockwise turn (negative cross product).
            3. Build upper hull by iterating right to left similarly.
            4. Combine both hulls, excluding duplicate start point.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """

        def cross_product(i: int, j: int, k: int) -> int:
            point_a, point_b, point_c = trees[i], trees[j], trees[k]
            return (point_b[0] - point_a[0]) * (point_c[1] - point_b[1]) - (
                point_b[1] - point_a[1]
            ) * (point_c[0] - point_b[0])

        num_trees = len(trees)
        if num_trees < 4:
            return trees
        trees.sort()
        visited = [False] * num_trees
        stack = [0]
        for i in range(1, num_trees):
            while len(stack) > 1 and cross_product(stack[-2], stack[-1], i) < 0:
                visited[stack.pop()] = False
            visited[i] = True
            stack.append(i)
        lower_size = len(stack)
        for i in range(num_trees - 2, -1, -1):
            if visited[i]:
                continue
            while (
                len(stack) > lower_size and cross_product(stack[-2], stack[-1], i) < 0
            ):
                stack.pop()
            stack.append(i)
        stack.pop()
        return [trees[i] for i in stack]
