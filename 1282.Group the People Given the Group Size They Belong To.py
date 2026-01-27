from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        """Group people by their assigned group sizes.

        Intuition:
            People with the same group size should be grouped together, filling
            groups of exactly that size.

        Approach:
            Collect person indices by their group size using a dictionary, then
            split each collected list into chunks of the required size.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        groups_by_size: dict[int, list[int]] = defaultdict(list)
        for person_id, size in enumerate(groupSizes):
            groups_by_size[size].append(person_id)
        return [
            people[start : start + size]
            for size, people in groups_by_size.items()
            for start in range(0, len(people), size)
        ]
