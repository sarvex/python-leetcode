class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        """Find the destination city that has no outgoing path.

        Intuition:
            The destination city never appears as a source in any path.

        Approach:
            Collect all source cities into a set, then find the destination
            city that is not in the source set.

        Complexity:
            Time: O(n) where n is the number of paths
            Space: O(n) for the source set
        """
        sources = {source for source, _ in paths}
        return next(
            destination for _, destination in paths if destination not in sources
        )
