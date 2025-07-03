class Solution:
    """
    Group-based Dynamic Programming with Inclusion-Exclusion

    Intuition:
    When Alice types a string, each character can be pressed once or multiple times.
    We can group consecutive identical characters and count their frequencies.
    The problem reduces to selecting which groups to keep or merge.

    Approach:
    1. Group consecutive identical characters and count frequencies
    2. If we have enough groups (>= k), all combinations are valid
    3. Otherwise, use inclusion-exclusion principle with DP to count valid strings
    4. Calculate total valid combinations with length >= k

    Complexity:
    - Time: O(n + k²) where n is the length of word and k is the minimum length
    - Space: O(k) for the DP arrays
    """
    def countOriginalStrings(self, word: str, k: int) -> int:
        MOD: int = 10**9 + 7
        n: int = len(word)

        # Step 1: Group consecutive identical characters
        groups: list[int] = []
        current_count: int = 1

        for i in range(1, n):
            if word[i] == word[i-1]:
                current_count += 1
            else:
                groups.append(current_count)
                current_count = 1
        groups.append(current_count)  # Add the last group

        # Calculate total possible combinations (product of all group frequencies)
        total_combinations: int = 1
        for count in groups:
            total_combinations = (total_combinations * count) % MOD

        # Step 2: Early return if we have enough groups
        if len(groups) >= k:
            return total_combinations

        # Step 3: Use DP with inclusion-exclusion principle
        # exact[j] = number of ways to form strings with exactly j groups
        # at_most[j] = number of ways to form strings with at most j groups
        exact = [1] + [0] * (k - 1)  # exact[0] = 1 (empty string has 0 groups)
        at_most = [1] * k  # at_most[j] = sum of exact[0...j]

        # Process each group frequency
        for freq in groups:
            # Calculate new exact values
            new_exact = [0] * k

            for j in range(1, k):
                # Add a new group
                new_exact[j] = at_most[j - 1]

                # Apply inclusion-exclusion principle
                if j > freq:
                    new_exact[j] = (new_exact[j] - at_most[j - freq - 1]) % MOD

            # Calculate new at_most values (prefix sums)
            new_at_most = [new_exact[0]] + [0] * (k - 1)
            for j in range(1, k):
                new_at_most[j] = (new_at_most[j - 1] + new_exact[j]) % MOD

            # Update for next iteration
            at_most = new_at_most

        # Step 4: Return total combinations minus invalid combinations
        return (total_combinations - at_most[k - 1]) % MOD


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    assert solution.countOriginalStrings("aabbccdd", 7) == 5

    # Example 2
    assert solution.countOriginalStrings("aabbccdd", 8) == 1

    # Example 3
    assert solution.countOriginalStrings("aaabbb", 3) == 8

    print("All test cases passed!")
