class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        """Count good strings in range [s1, s2] that do not contain evil.

        Intuition:
            Use digit DP to count strings up to a bound that do not contain
            the evil substring, then subtract counts to get the range.

        Approach:
            Define a counting function that computes how many strings up to
            a given bound avoid the evil substring. Use suffix matching
            (KMP-like overlap tracking) to efficiently detect evil occurrences.
            Final answer is count(s2) - count(s1) + (s2 is valid).

        Complexity:
            Time: O(n * len(evil)) for each bound computation
            Space: O(n) for the auxiliary arrays
        """
        modulus = 10**9 + 7
        ord_a = ord("a")
        evil_length = len(evil)
        overlaps: list[int] = []
        for i in range(1, evil_length):
            if evil[i:] == evil[: evil_length - i]:
                overlaps.append(i)
        overlap_count = len(overlaps)

        def count_up_to(bound: str) -> tuple[int, int]:
            running_count = 0
            is_bounded = 1
            boundary_index = n
            without_evil: list[int] = []
            for i in range(n):
                running_count *= 26
                if is_bounded:
                    running_count += ord(bound[i]) - ord_a
                if (
                    i >= evil_length - 1
                    and boundary_index > i - evil_length
                    and evil < bound[i - evil_length + 1 : i + 1]
                ):
                    running_count -= 1
                if i >= evil_length:
                    running_count -= without_evil[i - evil_length]
                if i >= evil_length - 1:
                    if bound[i - evil_length + 1 : i + 1] == evil:
                        is_bounded = 0
                        boundary_index = i
                running_count %= modulus
                with_evil_count = 0
                for j in range(overlap_count):
                    offset = overlaps[j]
                    if i >= offset:
                        with_evil_count += without_evil[i - offset]
                    if (
                        i >= offset - 1
                        and boundary_index > i - offset
                        and evil[:offset] < bound[i - offset + 1 : i + 1]
                    ):
                        with_evil_count += 1
                without_evil.append(running_count - with_evil_count)
            return running_count, is_bounded

        count1, _ = count_up_to(s1)
        count2, is_s2_valid = count_up_to(s2)
        return (count2 - count1 + is_s2_valid) % modulus
