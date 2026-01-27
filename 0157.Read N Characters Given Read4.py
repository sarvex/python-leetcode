class Solution:
    def read(self, buf: list[str], n: int) -> int:
        """Buffered Read Using read4 API.

        Intuition:
            Read chunks of 4 characters at a time using read4 and copy them
            into the destination buffer until we have n characters or reach EOF.

        Approach:
            Repeatedly call read4 to fill a temporary buffer. Copy characters
            from the temporary buffer to the destination buffer. Stop when
            n characters have been read or read4 returns fewer than 4 characters.

        Complexity:
            Time: O(n) reading at most n characters
            Space: O(1) using a fixed-size temporary buffer of 4
        """
        total_read = 0
        buf4 = [0] * 4
        chars_read = 5
        while chars_read >= 4:
            chars_read = read4(buf4)
            for j in range(chars_read):
                buf[total_read] = buf4[j]
                total_read += 1
                if total_read >= n:
                    return n
        return total_read
