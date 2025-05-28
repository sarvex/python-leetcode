class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in a given string.
        
        Approach: Dynamic Programming
        Intuition: A string is a palindrome if its first and last characters are the same and the
        substring between them is also a palindrome. We can use a 2D DP table where dp[i][j] is True
        if the substring s[i...j] is a palindrome.
        
        Time Complexity: O(n²), where n is the length of the string.
        Space Complexity: O(n²) for the DP table.
        """
        if not s:
            return ""
            
        n = len(s)
        # dp[i][j] will be True if the substring s[i...j] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
            
        start, max_length = 0, 1  # Track the start index and length of the longest palindrome
        
        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check for lengths greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of current substring
                
                # The substring s[i...j] is a palindrome if s[i] == s[j] and the
                # substring s[i+1...j-1] is also a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
        
        return s[start:start + max_length]

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_cases = ["babad", "cbbd", "a", "ac"]
    for test in test_cases:
        print(f"Input: {test}")
        print(f"Output: {sol.longestPalindrome(test)}\n")
