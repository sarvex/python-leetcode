from itertools import groupby

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [next(g) for _, g in groupby(words, sorted)]
