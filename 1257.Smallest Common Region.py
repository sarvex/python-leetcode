class Solution:
    def findSmallestRegion(
        self, regions: list[list[str]], region1: str, region2: str
    ) -> str:
        """Find lowest common ancestor region using parent traversal.

        Intuition:
            Regions form a tree where each sub-region has one parent. Finding the
            smallest common region is equivalent to finding the lowest common
            ancestor of two nodes in a tree.

        Approach:
            Build a parent map from the region lists. Traverse from region1 to
            root, collecting all ancestors in a set. Then traverse from region2
            upward until finding an ancestor that exists in the set.

        Complexity:
            Time: O(n) — building parent map and traversing ancestors
            Space: O(n) — for parent map and ancestor set
        """
        parent_map: dict[str, str] = {}
        for region in regions:
            for sub_region in region[1:]:
                parent_map[sub_region] = region[0]
        ancestors: set[str] = set()
        while parent_map.get(region1):
            ancestors.add(region1)
            region1 = parent_map[region1]
        while parent_map.get(region2):
            if region2 in ancestors:
                return region2
            region2 = parent_map[region2]
        return region1
