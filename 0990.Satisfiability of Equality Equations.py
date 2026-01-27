class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        """Determine if all equality and inequality equations are satisfiable.

        Intuition:
            Equality constraints form groups via union-find. Inequality
            constraints must not connect two variables in the same group.

        Approach:
            First pass: union all equality pairs. Second pass: check that no
            inequality pair shares the same root in the union-find structure.

        Complexity:
            Time: O(n * α(26)) ≈ O(n) where n is the number of equations
            Space: O(1) for the fixed-size parent array of 26 letters
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(26))
        for equation in equations:
            left = ord(equation[0]) - ord("a")
            right = ord(equation[-1]) - ord("a")
            if equation[1] == "=":
                parent[find(left)] = find(right)
        for equation in equations:
            left = ord(equation[0]) - ord("a")
            right = ord(equation[-1]) - ord("a")
            if equation[1] == "!" and find(left) == find(right):
                return False
        return True
