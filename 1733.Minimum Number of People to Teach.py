from typing import List


class Solution:
    def minimumTeachings( self, n: int, languages: List[List[int]], friendships: List[List[int]] ) -> int:
        """
        Calculates the minimum number of people to teach a language so all friends can communicate.

        Intuition:
        The core idea is to identify the smallest group of people that need teaching.
        These are individuals in friendships where no common language is shared.
        Once this group is identified, we find the most common language among them.
        The number of people to teach will be the size of this group minus the number
        of people who already speak that most common language.

        Approach:
        1.  Convert each person's list of languages to a set for efficient lookups.
        2.  Identify all unique individuals who are in friendships but share no common language.
            These are the only candidates who might need teaching.
        3.  Keep a frequency map (a list `cnt` acting as a hash map) of all languages spoken
            by these candidate individuals.
        4.  The total number of people who are candidates for teaching is `total`.
        5.  The maximum number of people in the candidate group who speak any single language is `max(cnt)`.
        6.  The minimum number of teachings is `total - max(cnt)`.
            This is because we can teach the most common language to those in the group who don't already know it.

        Complexity:
        - Time complexity: O(U + F*L), where U is the total number of users, F is the number of friendships,
          and L is the average number of languages per user. The `map(set, languages)` takes O(U*L).
          The loop over friendships takes O(F*L) for the `isdisjoint` check.
        - Space complexity: O(U*L + N), for storing the language sets and the language counts.
        """
        language_sets = list(map(set, languages))

        needs_teaching = [False] * len(languages)
        unconnected_users = set()

        for u, v in friendships:
            user1, user2 = u - 1, v - 1
            if language_sets[user1].isdisjoint(language_sets[user2]):
                unconnected_users.add(user1)
                unconnected_users.add(user2)

        if not unconnected_users:
            return 0

        lang_counts = [0] * (n + 1)
        for user_idx in unconnected_users:
            for lang in language_sets[user_idx]:
                lang_counts[lang] += 1

        return len(unconnected_users) - max(lang_counts)
