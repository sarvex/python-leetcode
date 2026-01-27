class Solution:
    def magicalString(self, n: int) -> int:
        """Generate the magical string and count ones.

        Intuition:
            The magical string describes its own run-length encoding.
            Generate it by reading group lengths from itself.

        Approach:
            Start with [1, 2, 2] and a pointer at index 2. Alternate
            between 1 and 2 as the current value. Append the current
            value s[pointer] times, advancing the pointer each step.
            Count how many 1s appear in the first n characters.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        sequence = [1, 2, 2]
        pointer = 2
        while len(sequence) < n:
            previous = sequence[-1]
            current = 3 - previous
            sequence += [current] * sequence[pointer]
            pointer += 1
        return sequence[:n].count(1)
