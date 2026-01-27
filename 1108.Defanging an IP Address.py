class Solution:
    def defangIPaddr(self, address: str) -> str:
        """Defang an IP address by replacing dots with brackets.

        Intuition:
            Every dot in a valid IP address must be wrapped with square brackets.

        Approach:
            Use the built-in string replace method to substitute each '.' with '[.]'.

        Complexity:
            Time: O(n) where n is the length of the address
            Space: O(n) for the resulting string
        """
        return address.replace(".", "[.]")
