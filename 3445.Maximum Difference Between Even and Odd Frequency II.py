from collections import deque
from itertools import permutations

class Solution:
    """Optimized solution using index tracking and monotonic deques

    Intuition:
    - Instead of iterating through the string multiple times, we track indices of each character
    - We use monotonic deques to efficiently track the minimum difference for each parity combination
    - By considering permutations of character indices, we can find the optimal difference

    Approach:
    1. Preprocess the string to get indices of each character
    2. For each pair of distinct characters, calculate the maximum difference
    3. Use monotonic deques to efficiently track the minimum difference for each parity
    4. Return the maximum difference found

    Complexity:
    - Time: O(n), where n is the length of string s
    - Space: O(n), for storing character indices and deques
    """
    def maxDifference(self, s: str, k: int) -> int:
        # Preprocess to get indices of each character (0-4)
        char_indices = [[] for _ in range(5)]
        for position, digit in enumerate(s):
            char_indices[int(digit)].append(position)

        # Keep only characters that appear in the string
        char_indices = [indices for indices in char_indices if indices]

        string_length = len(s)
        # Add sentinel value to simplify boundary handling
        for indices in char_indices:
            indices.append(string_length)

        def calculate_max_difference(char1_indices, char2_indices):
            """Calculate maximum difference between odd frequency of char1 and even frequency of char2"""
            # Create deques for each parity combination (00, 01, 10, 11)
            parity_deques = [deque() for _ in range(4)]
            min_differences = [float('inf')] * 4  # Track minimum differences for each parity

            # Initialize with first valid position
            parity_deques[0].append((max(char1_indices[0], char2_indices[0], k-1), 0))

            char1_count = char2_count = 0  # Count of characters seen so far
            max_difference = -float('inf')
            current_position = -1  # Current processing position

            # Process indices until we reach the end of both character lists
            while char1_indices[char1_count] != string_length or char2_indices[char2_count] != string_length:
                # Determine which character appears next in the string
                if char1_indices[char1_count] < char2_indices[char2_count]:
                    # Next character is char1
                    if char1_indices[char1_count] > current_position:
                        current_position = char1_indices[char1_count]
                    char1_count += 1
                else:
                    # Next character is char2
                    if char2_indices[char2_count] > current_position:
                        current_position = char2_indices[char2_count]
                    char2_count += 1

                # Calculate the right boundary of current window
                right_boundary = min(char1_indices[char1_count], char2_indices[char2_count]) - 1

                # Calculate parity status (bit representation of odd/even counts)
                current_parity = (char1_count & 1) | ((char2_count & 1) << 1)
                opposite_parity = current_parity ^ 1  # Toggle bit 0 to get opposite parity

                # Process deque entries that are now within the window
                while parity_deques[opposite_parity] and parity_deques[opposite_parity][0][0] <= right_boundary:
                    _, min_differences[opposite_parity] = parity_deques[opposite_parity].popleft()

                # Update max difference (char1_count - char2_count - minimum_difference)
                max_difference = max(max_difference, char1_count - char2_count - min_differences[opposite_parity])

                # Calculate current difference value
                current_diff = char1_count - char2_count

                # Add to deque if it improves the minimum
                if current_diff < min_differences[current_parity] and (not parity_deques[current_parity] or
                                                                  current_diff < parity_deques[current_parity][-1][1]):
                    # Store (valid_until_position, difference_value)
                    valid_until = max(current_position + k, char1_indices[char1_count], char2_indices[char2_count])
                    parity_deques[current_parity].append((valid_until, current_diff))

            return max_difference

        # Try all permutations of character pairs
        max_result = -float('inf')
        for char1_indices, char2_indices in permutations(char_indices, 2):
            max_result = max(max_result, calculate_max_difference(char1_indices, char2_indices))

        return max_result
