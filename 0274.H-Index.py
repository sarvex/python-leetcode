from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Counting sort approach for finding H-Index of a researcher.

        Intuition:
        A researcher has an h-index of h if h of their papers have at least h citations each,
        and the other papers have no more than h citations each. We can use counting sort
        to efficiently find this value without full sorting.

        Approach:
        1. Use counting sort to count papers with each citation count
        2. Traverse from the highest count to find where count of papers >= current index

        Complexity:
        Time: O(n) where n is the number of papers
        Space: O(n) for the counts array
        """
        n = len(citations)
        counts = [0] * (n + 1)

        # Count papers for each citation number, capping at n
        for citation in citations:
            counts[min(citation, n)] += 1

        # Start from the highest possible h-index and work backwards
        h = n
        papers = counts[n]

        while h > papers:
            h -= 1
            papers += counts[h]

        return h
