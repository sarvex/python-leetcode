from collections import defaultdict
from heapq import nlargest


class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        """Return the average of top 5 scores for each student.

        Intuition:
            Group scores by student ID, then average the top 5 for each.

        Approach:
            Use a defaultdict to collect scores per student. For each student
            in order, compute the average of the 5 largest scores.

        Complexity:
            Time: O(n log n) for nlargest calls across all scores
            Space: O(n) for the score dictionary
        """
        scores_by_student: dict[int, list[int]] = defaultdict(list)
        max_id = 0
        for student_id, score in items:
            scores_by_student[student_id].append(score)
            max_id = max(max_id, student_id)
        result: list[list[int]] = []
        for student_id in range(1, max_id + 1):
            if student_scores := scores_by_student[student_id]:
                average = sum(nlargest(5, student_scores)) // 5
                result.append([student_id, average])
        return result
