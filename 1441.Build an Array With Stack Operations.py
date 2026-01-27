class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        """Build target array from stream using Push and Pop operations.

        Intuition:
            Process the natural number stream and push each number; pop
            immediately if it is not in the target sequence.

        Approach:
            Track the current stream number. For each target value, emit
            Push+Pop pairs for skipped numbers, then Push for the target value.

        Complexity:
            Time: O(n) where n is the last element in target
            Space: O(n) for the result list
        """
        current = 0
        operations: list[str] = []
        for value in target:
            current += 1
            while current < value:
                operations.extend(["Push", "Pop"])
                current += 1
            operations.append("Push")
        return operations
