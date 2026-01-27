class Solution:
    def similarRGB(self, color: str) -> str:
        """Find closest shorthand RGB color by rounding each component.

        Intuition:
            Shorthand colors have identical hex digits per component (e.g., 0x33).
            The closest shorthand value to any 2-digit hex is the nearest multiple of 17.

        Approach:
            1. Split color into three 2-digit hex components.
            2. For each component, find the nearest multiple of 17.
            3. Reconstruct the color string.

        Complexity:
            Time: O(1)
            Space: O(1)
        """

        def nearest_shorthand(hex_pair: str) -> str:
            quotient, remainder = divmod(int(hex_pair, 16), 17)
            if remainder > 8:
                quotient += 1
            return f"{17 * quotient:02x}"

        red, green, blue = color[1:3], color[3:5], color[5:7]
        return f"#{nearest_shorthand(red)}{nearest_shorthand(green)}{nearest_shorthand(blue)}"
