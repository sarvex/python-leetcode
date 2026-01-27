class Solution:
    def maskPII(self, s: str) -> str:
        """Mask email or phone number based on input format.

        Intuition:
            Detect whether the input is an email (contains '@') or phone number.
            Apply the respective masking rules.

        Approach:
            1. If starts with a letter, it's an email: lowercase, mask middle of name.
            2. Otherwise, extract digits, mask with country code prefix if needed.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        if s[0].isalpha():
            s = s.lower()
            return s[0] + "*****" + s[s.find("@") - 1 :]
        digits = "".join(char for char in s if char.isdigit())
        country_digits = len(digits) - 10
        suffix = "***-***-" + digits[-4:]
        return suffix if country_digits == 0 else f"+{'*' * country_digits}-{suffix}"
