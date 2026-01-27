from collections import Counter


class Solution:
    def originalDigits(self, text: str) -> str:
        """Identify digits by unique and distinguishing letters in their English names.

        Intuition:
            Some digits have unique letters in their English spelling (e.g., 'z'
            only in 'zero'). After resolving those, remaining digits can be
            determined by subtracting known counts.

        Approach:
            1. Count character frequencies in the input string.
            2. Determine counts for digits with unique letters: 0(z), 2(w), 4(u),
               6(x), 8(g).
            3. Derive remaining digits: 3(h-8), 5(f-4), 7(s-6), 1(o-0-2-4),
               9(i-5-6-8).
            4. Build the result string in digit order.

        Complexity:
            Time: O(n) where n is the length of the input string.
            Space: O(1) since the counter has at most 26 keys.
        """
        frequency = Counter(text)
        digit_counts = [0] * 10

        digit_counts[0] = frequency["z"]
        digit_counts[2] = frequency["w"]
        digit_counts[4] = frequency["u"]
        digit_counts[6] = frequency["x"]
        digit_counts[8] = frequency["g"]

        digit_counts[3] = frequency["h"] - digit_counts[8]
        digit_counts[5] = frequency["f"] - digit_counts[4]
        digit_counts[7] = frequency["s"] - digit_counts[6]

        digit_counts[1] = (
            frequency["o"] - digit_counts[0] - digit_counts[2] - digit_counts[4]
        )
        digit_counts[9] = (
            frequency["i"] - digit_counts[5] - digit_counts[6] - digit_counts[8]
        )

        return "".join(digit_counts[i] * str(i) for i in range(10))
