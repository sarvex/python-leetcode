class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        """DFS search over pairwise operations to reach 24
        
        Tagline:
            Depth-first search over all pairwise arithmetic operations with memoization.
        
        Intuition:
            Repeatedly pick two numbers, apply an operation, and recurse with the result joined
            to the remaining numbers. If any path evaluates to 24 (within tolerance), the goal is
            achievable.
        
        Approach:
            Use DFS on multiset states. Iterate unordered pairs (i < j) and try these results:
            a + b, a - b, b - a, a * b, a / b (if b != 0), b / a (if a != 0). Memoize visited
            float states using a rounded, sorted signature to prune duplicates caused by commutativity
            and floating error. Early-return when a single number remains near 24.
        
        Complexity:
            Time: Exponential in branching; small in practice for n = 4.
            Space: O(n) recursion depth; memo set proportional to visited states.
        """

        TARGET: float = 24.0
        EPS: float = 1e-6

        seen: set[tuple[float, ...]] = set()

        def signature(nums: list[float]) -> tuple[float, ...]:
            # Rounded sorted tuple to mitigate FP noise and treat permutations equally
            return tuple(sorted(round(x, 3) for x in nums))

        def dfs(nums: list[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPS

            sig = signature(nums)
            if sig in seen:
                return False
            seen.add(sig)

            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    rest = [nums[k] for k in range(n) if k != i and k != j]

                    candidates: list[float] = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(rest + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])
