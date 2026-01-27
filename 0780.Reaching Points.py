class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """Work backwards from target using modular reduction.

        Intuition:
            Forward search branches exponentially, but working backwards from
            (tx, ty) the larger coordinate can only have been produced by subtracting
            the smaller one. Using modulo speeds up repeated subtractions.

        Approach:
            1. While tx > sx and ty > sy and tx != ty, reduce the larger by modding
               with the smaller
            2. If we reach (sx, sy) exactly, return True
            3. If only one coordinate matches, check if the other can be reached
               by repeated addition of the matching coordinate

        Complexity:
            Time: O(log(max(tx, ty))) due to modular reduction
            Space: O(1)
        """
        while tx > sx and ty > sy and tx != ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        if tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        if ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        return False
