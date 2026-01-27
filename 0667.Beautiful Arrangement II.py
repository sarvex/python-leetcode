class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        """Zigzag construction to achieve exactly k distinct differences.

        Intuition:
        Alternate between the smallest and largest remaining values for the first
        k elements to create k distinct differences. Fill the rest sequentially.

        Approach:
        1. Use two pointers (left, right) starting at 1 and n.
        2. For the first k elements, alternate picking from left and right.
        3. Fill remaining elements in monotone order (direction depends on k parity).

        Complexity:
        Time: O(n)
        Space: O(n)
        """
        left, right = 1, n
        result = []
        for i in range(k):
            if i % 2 == 0:
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        for i in range(k, n):
            if k % 2 == 0:
                result.append(right)
                right -= 1
            else:
                result.append(left)
                left += 1
        return result
