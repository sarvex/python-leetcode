from collections import defaultdict


class TwoSum:
    """Data structure supporting add and two-sum find operations.

    Uses a frequency counter to track added numbers and checks complement
    existence for find queries.
    """

    def __init__(self) -> None:
        """Initialize the frequency counter."""
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        """Add a number to the data structure.

        Intuition:
            Track frequency so duplicates can form valid pairs.

        Approach:
            Increment the count for the given number.

        Complexity:
            Time: O(1)
            Space: O(1) amortized
        """
        self.count[number] += 1

    def find(self, value: int) -> bool:
        """Check if any pair of added numbers sums to the given value.

        Intuition:
            For each stored number, check if its complement exists. Handle the
            case where number equals complement by requiring count > 1.

        Approach:
            Iterate through stored numbers, compute complement, and verify
            existence in the counter with proper duplicate handling.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        for number, freq in self.count.items():
            complement = value - number
            if complement in self.count and (number != complement or freq > 1):
                return True
        return False
