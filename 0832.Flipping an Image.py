class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """Reverse each row and invert bits in one pass using two pointers.

        Intuition:
            When reversing and inverting, if the two mirrored elements are equal,
            both need flipping. If different, they effectively swap and invert
            to the same values, so no change is needed.

        Approach:
            1. For each row, use two pointers from both ends.
            2. If the mirrored values are equal, flip both.
            3. If they differ, swapping and inverting cancels out.
            4. Handle the middle element for odd-length rows.

        Complexity:
            Time: O(n^2)
            Space: O(1) in-place
        """
        cols = len(image)
        for row in image:
            left, right = 0, cols - 1
            while left < right:
                if row[left] == row[right]:
                    row[left] ^= 1
                    row[right] ^= 1
                left, right = left + 1, right - 1
            if left == right:
                row[left] ^= 1
        return image
