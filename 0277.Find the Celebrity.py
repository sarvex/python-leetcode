class Solution:
    def findCelebrity(self, n: int) -> int:
        """Two-pass algorithm to identify the celebrity using the knows API.

        Intuition:
            If candidate knows person i, candidate is not the celebrity, so
            switch to i. After one pass, the remaining candidate is the only
            possible celebrity. A second pass verifies this.

        Approach:
            1. First pass: iterate through all people. If the current candidate
               knows person i, update candidate to i.
            2. Second pass: verify the candidate by checking that they know no
               one and everyone knows them.
            3. Return the candidate if valid, otherwise -1.

        Complexity:
            Time: O(n) for two passes through all people
            Space: O(1)
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if candidate != i:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1
        return candidate
