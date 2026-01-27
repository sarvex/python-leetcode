class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        """DP counting binary trees where children multiply to parent.

        Intuition:
            Sort the array so we process smaller values first. For each value,
            check all pairs of factors that could be its children.

        Approach:
            1. Sort the array and create a value-to-index mapping.
            2. For each element, iterate over smaller elements as left child.
            3. If the quotient is also in the array, multiply tree counts.
            4. Sum all tree counts modulo 10^9 + 7.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        modulo = 10**9 + 7
        length = len(arr)
        arr.sort()
        value_index = {value: i for i, value in enumerate(arr)}
        tree_count = [1] * length
        for i, parent in enumerate(arr):
            for j in range(i):
                child = arr[j]
                if parent % child == 0 and (quotient := parent // child) in value_index:
                    tree_count[i] = (
                        tree_count[i]
                        + tree_count[j] * tree_count[value_index[quotient]]
                    ) % modulo
        return sum(tree_count) % modulo
