class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        """Merge sort counting reverse pairs where nums[i] > 2 * nums[j].

        Intuition:
            During merge sort, when merging two sorted halves, we can efficiently
            count pairs where an element in the left half is greater than twice an
            element in the right half.

        Approach:
            Use modified merge sort. Before merging two halves, count reverse pairs
            using two pointers. Then perform the standard merge to maintain sorted order.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """

        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0
            mid = (left + right) >> 1
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= 2 * nums[j]:
                    i += 1
                else:
                    count += mid - i + 1
                    j += 1
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            temp.extend(nums[i : mid + 1])
            temp.extend(nums[j : right + 1])
            nums[left : right + 1] = temp
            return count

        return merge_sort(0, len(nums) - 1)
