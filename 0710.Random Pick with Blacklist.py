from random import randrange


class Solution:
    """Random pick using blacklist remapping to whitelist range.

    Intuition:
        Map blacklisted numbers in the valid range [0, k) to non-blacklisted
        numbers in the upper range [k, n), where k = n - len(blacklist).

    Approach:
        1. Compute k = n - len(blacklist) as the whitelist size.
        2. Build a mapping: for each blacklisted number < k, map it to a
           non-blacklisted number >= k.
        3. On pick, generate a random number in [0, k) and return its
           mapped value if it exists, otherwise return it directly.

    Complexity:
        Time: O(b) for init where b is blacklist size, O(1) for pick
        Space: O(b) for the remapping dictionary
    """

    def __init__(self, n: int, blacklist: list[int]) -> None:
        self.whitelist_size = n - len(blacklist)
        self.remap: dict[int, int] = {}
        next_available = self.whitelist_size
        black_set = set(blacklist)
        for blocked in blacklist:
            if blocked < self.whitelist_size:
                while next_available in black_set:
                    next_available += 1
                self.remap[blocked] = next_available
                next_available += 1

    def pick(self) -> int:
        index = randrange(self.whitelist_size)
        return self.remap.get(index, index)
