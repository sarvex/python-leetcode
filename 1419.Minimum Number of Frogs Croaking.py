class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """Find minimum number of frogs to produce the given croak sequence.

        Intuition:
            Track how many frogs are at each stage of saying "croak".
            A frog starting 'c' needs a free frog or a new one.

        Approach:
            Map each character to its position in "croak". Track counts at
            each stage. When a character appears, ensure the previous stage
            has a frog available. Track maximum concurrent frogs.

        Complexity:
            Time: O(n) single pass through the string
            Space: O(1) fixed-size tracking arrays
        """
        if len(croakOfFrogs) % 5 != 0:
            return -1
        char_index = {ch: i for i, ch in enumerate("croak")}
        stage_count = [0] * 5
        max_frogs = active_frogs = 0
        for idx in map(char_index.get, croakOfFrogs):
            stage_count[idx] += 1
            if idx == 0:
                active_frogs += 1
                max_frogs = max(max_frogs, active_frogs)
            else:
                if stage_count[idx - 1] == 0:
                    return -1
                stage_count[idx - 1] -= 1
                if idx == 4:
                    active_frogs -= 1
        return -1 if active_frogs else max_frogs
