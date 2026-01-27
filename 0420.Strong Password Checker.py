class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        """Greedy approach handling insertions, replacements, and deletions.

        Intuition:
            The password must satisfy length (6-20), character type (lowercase,
            uppercase, digit), and no three consecutive identical characters.
            The strategy depends on the password length range.

        Approach:
            1. Count missing character types (lowercase, uppercase, digit).
            2. If length < 6, return max(6 - n, 3 - types) as insertions fix both.
            3. If length <= 20, count replacements needed for repeating sequences
               (every group of 3+ consecutive chars needs cnt // 3 replacements).
            4. If length > 20, combine deletions with replacement optimization:
               prioritize removing from groups where len % 3 == 0 (saves 1 delete
               per replacement), then len % 3 == 1 (saves 2 deletes).

        Complexity:
            Time: O(n) for a single pass through the password.
            Space: O(1) using only constant extra variables.
        """

        def count_types(text: str) -> int:
            has_lower = has_upper = has_digit = 0
            for char in text:
                if char.islower():
                    has_lower = 1
                elif char.isupper():
                    has_upper = 1
                elif char.isdigit():
                    has_digit = 1
            return has_lower + has_upper + has_digit

        types = count_types(password)
        length = len(password)
        if length < 6:
            return max(6 - length, 3 - types)
        if length <= 20:
            replacements = consecutive = 0
            prev = "~"
            for curr in password:
                if curr == prev:
                    consecutive += 1
                else:
                    replacements += consecutive // 3
                    consecutive = 1
                    prev = curr
            replacements += consecutive // 3
            return max(replacements, 3 - types)
        replacements = consecutive = 0
        removals, removals_saving_two = length - 20, 0
        prev = "~"
        for curr in password:
            if curr == prev:
                consecutive += 1
            else:
                if removals > 0 and consecutive >= 3:
                    if consecutive % 3 == 0:
                        removals -= 1
                        replacements -= 1
                    elif consecutive % 3 == 1:
                        removals_saving_two += 1
                replacements += consecutive // 3
                consecutive = 1
                prev = curr
        if removals > 0 and consecutive >= 3:
            if consecutive % 3 == 0:
                removals -= 1
                replacements -= 1
            elif consecutive % 3 == 1:
                removals_saving_two += 1
        replacements += consecutive // 3
        use_two = min(replacements, removals_saving_two, removals // 2)
        replacements -= use_two
        removals -= use_two * 2

        use_three = min(replacements, removals // 3)
        replacements -= use_three
        removals -= use_three * 3
        return length - 20 + max(replacements, 3 - types)
