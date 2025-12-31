class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = score = 0
        best_hour = 0
        for i, c in enumerate(customers):
            score += 1 if c == "Y" else -1
            if score > max_score:
                max_score = score
                best_hour = i + 1
        return best_hour
