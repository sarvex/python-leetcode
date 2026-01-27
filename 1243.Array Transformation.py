class Solution:
    def transformArray(self, arr: list[int]) -> list[int]:
        """Transform array by repeatedly adjusting local extrema until stable.

        Intuition:
            Each pass smooths local peaks and valleys by decrementing peaks and
            incrementing valleys. The process converges when no element changes.

        Approach:
            Repeatedly iterate through the array. Compare each interior element
            with its neighbors using a snapshot from before the pass. Adjust
            values accordingly. Stop when a full pass makes no changes.

        Complexity:
            Time: O(n * max_value) in the worst case
            Space: O(n)
        """
        changed = True
        while changed:
            changed = False
            snapshot = arr[:]
            for i in range(1, len(snapshot) - 1):
                if snapshot[i] > snapshot[i - 1] and snapshot[i] > snapshot[i + 1]:
                    arr[i] -= 1
                    changed = True
                if snapshot[i] < snapshot[i - 1] and snapshot[i] < snapshot[i + 1]:
                    arr[i] += 1
                    changed = True
        return arr
