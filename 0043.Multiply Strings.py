class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Digit-by-digit multiplication with carry handling

        Intuition:
        Multiply each digit of the first number with each digit of the second number,
        similar to how we perform multiplication by hand. Store the results in an
        intermediate array and handle carries appropriately.

        Approach:
        1. Handle edge case: if either number is "0", return "0"
        2. Create an array to store intermediate results with size len(num1) + len(num2)
        3. Multiply each digit pair and add to the corresponding position in the array
        4. Process carries from right to left
        5. Remove leading zero if present and convert the result to string

        Complexity:
        Time: O(m * n) where m and n are the lengths of the input strings
        Space: O(m + n) for the result array
        """
        # Handle edge case
        if num1 == "0" or num2 == "0":
            return "0"

        # Get lengths of both numbers
        len1, len2 = len(num1), len(num2)

        # Initialize result array with zeros
        # The result can have at most len1 + len2 digits
        result = [0] * (len1 + len2)

        # Perform digit-by-digit multiplication
        for i in range(len1 - 1, -1, -1):
            digit1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
                # Add to the correct position in the result array
                result[i + j + 1] += digit1 * digit2

        # Process carries
        for i in range(len1 + len2 - 1, 0, -1):
            result[i - 1] += result[i] // 10
            result[i] %= 10

        # Remove leading zero if present
        start_index = 0 if result[0] else 1

        # Convert result to string
        return "".join(str(digit) for digit in result[start_index:])
