class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Flag-based Character Tracking

        Intuition:
        When we have more than 2 consecutive identical characters, we need to remove the extras.
        Instead of checking the last two characters in our result each time, we can use a flag
        to track when we've already seen two consecutive identical characters.

        Approach:
        1. Handle edge case: strings with length < 3 are already fancy
        2. Initialize with the first character and track it as the previous character
        3. For each subsequent character:
           - If it's different from the previous, reset the flag and add it
           - If it's the same and we haven't seen two consecutive yet, add it and set flag
           - If it's the same and we've already seen two consecutive, skip it
        4. Join the list into the final string

        Complexity:
        Time: O(n) where n is the length of the input string
        Space: O(n) for storing the result
        """
        # Edge case: strings with length < 3 are already fancy
        if len(s) < 3:
            return s

        # Initialize with first character
        prev = s[0]
        result = [s[0]]
        has_duplicate = False

        # Process remaining characters
        for char in s[1:]:
            if prev != char:
                # Different character - add it and reset flag
                prev = char
                result.append(char)
                has_duplicate = False
                continue

            if not has_duplicate:
                # Same character but only seen once - add it and set flag
                result.append(char)
                has_duplicate = True

        return "".join(result)
