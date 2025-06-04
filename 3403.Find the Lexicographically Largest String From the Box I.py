class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        window = len(word) - numFriends + 1
        result = -1
        max_score = ""
        for idx in range(len(word)):
            if word[idx: idx + window] > max_score:
                max_score = word[idx: idx + window]
                result = idx
        return word[result: result + window]
