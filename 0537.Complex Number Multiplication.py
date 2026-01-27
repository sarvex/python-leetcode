class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """Multiply two complex numbers given as strings.

        Intuition:
            Parse real and imaginary parts, apply the complex multiplication
            formula: (a+bi)(c+di) = (ac-bd) + (ad+bc)i.

        Approach:
            Split each string at '+' and strip 'i' to extract components.
            Compute real and imaginary parts using the formula.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        real1, imag1 = map(int, num1[:-1].split("+"))
        real2, imag2 = map(int, num2[:-1].split("+"))
        return f"{real1 * real2 - imag1 * imag2}+{real1 * imag2 + real2 * imag1}i"
