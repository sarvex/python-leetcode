class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return all(s.count(char) == t.count(char) for char in set(s))
