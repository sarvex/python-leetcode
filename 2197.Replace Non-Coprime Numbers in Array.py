class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        """Stack + LCM compression of adjacent non-coprimes
        
        Intuition:
        Replace any adjacent non-coprime pair with their LCM. After a merge,
        the new value may also be non-coprime with the previous number, so we
        must continue collapsing until the boundary becomes coprime.
        
        Approach:
        Maintain a stack of finalized values and a rolling current value. For
        each incoming number, if it is non-coprime with the current value,
        merge by LCM and keep collapsing with the stack top as long as they
        remain non-coprime. Otherwise, push the current value to the stack and
        advance. Finally, append the last current value.
        
        Complexity:
        Time: O(n * log A) amortized due to gcd operations; A is value size.
        Space: O(n) for the stack.
        """
        def _gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def _lcm(a: int, b: int) -> int:
            return a // _gcd(a, b) * b

        if not nums:
            return []

        ans: list[int] = []
        curr: int = nums[0]
        for x in nums[1:]:
            if _gcd(curr, x) > 1:
                curr = _lcm(curr, x)
                while ans and _gcd(curr, ans[-1]) > 1:
                    curr = _lcm(curr, ans.pop())
            else:
                ans.append(curr)
                curr = x

        ans.append(curr)
        return ans
