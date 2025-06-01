from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group anagrams using sorted string as key.

        Intuition:
            Anagrams have the same characters but in different orders.
            If we sort each string, all anagrams will result in the same sorted string.
            We can use this sorted string as a key in a hash map to group anagrams.

        Approach:
            1. Create a defaultdict to store groups of anagrams
            2. For each string, sort its characters to create a key
            3. Append the original string to the list associated with that key
            4. Return all the grouped anagrams as a list of lists

        Complexity:
            Time: O(n * k log k) where n is the length of strs and k is the maximum length of a string in strs
            Space: O(n * k) for storing all strings in the dictionary
        """
        anagram_groups = defaultdict(list)

        for s in strs:
            # Create a key by sorting the characters in the string
            key = ''.join(sorted(s))
            # Group strings with the same sorted key
            anagram_groups[key].append(s)

        return list(anagram_groups.values())
