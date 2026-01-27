class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        """Greedy insertion sorted by height descending, position ascending.

        Intuition:
            Process tallest people first. When inserting a person, all
            previously inserted people are at least as tall, so the
            person's k-value directly gives the correct insertion index.

        Approach:
            1. Sort people by height descending, then by k-value ascending.
            2. Insert each person at index equal to their k-value.
            3. Since taller people are already placed, the insertion index
               correctly represents the number of taller-or-equal people ahead.

        Complexity:
            Time: O(n^2) due to list insertions
            Space: O(n) for the result list
        """
        people.sort(key=lambda person: (-person[0], person[1]))
        result: list[list[int]] = []
        for person in people:
            result.insert(person[1], person)
        return result
