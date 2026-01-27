class Solution:
    def numberToWords(self, num: int) -> str:
        """Recursive conversion of number segments into English words.

        Intuition:
            Break the number into groups of three digits (billions, millions,
            thousands, units) and convert each group independently.

        Approach:
            1. Handle the special case of zero.
            2. Define word arrays for numbers below 20, tens, and scale labels.
            3. Use a recursive helper to convert a number less than 1000 to words.
            4. Process each three-digit group from billions down to units,
               appending the scale label.

        Complexity:
            Time: O(1) since the number has at most 10 digits
            Space: O(1) for the fixed-size word arrays
        """
        if num == 0:
            return "Zero"

        below_twenty = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens_words = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        scale_labels = ["Billion", "Million", "Thousand", ""]

        def convert_chunk(value: int) -> str:
            if value == 0:
                return ""
            if value < 20:
                return below_twenty[value] + " "
            if value < 100:
                return tens_words[value // 10] + " " + convert_chunk(value % 10)
            return below_twenty[value // 100] + " Hundred " + convert_chunk(value % 100)

        parts: list[str] = []
        divisor, scale_index = 1000000000, 0
        while divisor > 0:
            if num // divisor != 0:
                parts.append(convert_chunk(num // divisor))
                parts.append(scale_labels[scale_index])
                parts.append(" ")
                num %= divisor
            scale_index += 1
            divisor //= 1000
        return "".join(parts).strip()
