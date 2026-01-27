import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """Find most frequent non-banned word using regex and counter.

        Intuition:
            Extract all words, count frequencies, and return the most common
            one that is not in the banned set.

        Approach:
            1. Extract lowercase words using regex.
            2. Count word frequencies with Counter.
            3. Return the most common word not in the banned set.

        Complexity:
            Time: O(n + b) where n = paragraph length, b = banned list size
            Space: O(n + b)
        """
        banned_set = set(banned)
        word_counts = Counter(re.findall("[a-z]+", paragraph.lower()))
        return next(
            word for word, _ in word_counts.most_common() if word not in banned_set
        )
