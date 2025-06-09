class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """Denary tree traversal to find the k-th lexicographically smallest number.

        Intuition:
            Numbers in lexicographical order form a denary tree (10-ary tree) where each
            node has up to 10 children (0-9). We can count how many numbers are in each
            subtree and use this to navigate to the k-th number efficiently.

        Approach:
            1. Start from the smallest digit (1)
            2. For each current number, calculate how many numbers are in its subtree
            3. If k is greater than the count, move horizontally (curr + 1)
            4. Otherwise, move down the tree (curr * 10) and decrease k
            5. Continue until k becomes 0

        Complexity:
            Time: O(log(n)²) where log(n) is the number of digits in n
            Space: O(1), constant extra space
        """
        def count(curr: int) -> int:
            """Count numbers in the subtree starting with curr that are <= n."""
            next_prefix, count = curr + 1, 0
            while curr <= n:
                # Add the count of numbers between curr and min(next_prefix-1, n)
                count += min(n - curr + 1, next_prefix - curr)
                # Move to the next level in the tree
                next_prefix, curr = next_prefix * 10, curr * 10
            return count

        current = 1  # Start from 1 (lexicographically smallest digit)
        k -= 1    # We're already at the first number (1)

        while k > 0:
            subtree_size = count(current)
            if k >= subtree_size:
                # Skip the entire subtree and move horizontally
                k -= subtree_size
                current += 1
            else:
                # Move down the tree (add a digit)
                k -= 1
                current *= 10

        return current
