from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """Stack-based parsing to count atoms in a chemical formula.

        Intuition:
            Parentheses create nested scopes where a multiplier applies to all
            atoms inside. A stack of counters naturally handles nesting.

        Approach:
            1. Push a new Counter on '(' and pop/multiply on ')'.
            2. Parse element names (uppercase + lowercase letters) and counts.
            3. After processing, sort elements alphabetically and format output.

        Complexity:
            Time: O(n + k * log(k)) where n is formula length, k is unique elements
            Space: O(n) for the stack of counters
        """
        stack: list[Counter] = [Counter()]
        pos = 0
        length = len(formula)

        while pos < length:
            if formula[pos] == "(":
                stack.append(Counter())
                pos += 1
            elif formula[pos] == ")":
                pos += 1
                start = pos
                while pos < length and formula[pos].isdigit():
                    pos += 1
                multiplier = int(formula[start:pos] or 1)
                top = stack.pop()
                for element, count in top.items():
                    stack[-1][element] += count * multiplier
            else:
                start = pos
                pos += 1
                while pos < length and formula[pos].islower():
                    pos += 1
                element = formula[start:pos]
                start = pos
                while pos < length and formula[pos].isdigit():
                    pos += 1
                count = int(formula[start:pos] or 1)
                stack[-1][element] += count

        atom_counts = stack.pop()
        sorted_elements = sorted(atom_counts.items())
        output: list[str] = []
        for element, count in sorted_elements:
            output.append(element)
            if count > 1:
                output.append(str(count))

        return "".join(output)
