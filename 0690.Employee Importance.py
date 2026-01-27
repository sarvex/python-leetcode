class Solution:
    def getImportance(self, employees: list["Employee"], id: int) -> int:
        """DFS traversal to sum importance values of employee and subordinates.

        Intuition:
            Build a lookup map from employee ID to employee object, then
            recursively sum the importance of the target employee and all
            their direct and indirect subordinates.

        Approach:
            1. Create a dictionary mapping employee IDs to employee objects.
            2. Use DFS starting from the given ID.
            3. At each node, add the importance value and recurse into
               all subordinates.

        Complexity:
            Time: O(n) visiting each employee at most once
            Space: O(n) for the lookup dictionary and recursion stack
        """

        def dfs(employee_id: int) -> int:
            return employee_map[employee_id].importance + sum(
                dfs(sub_id) for sub_id in employee_map[employee_id].subordinates
            )

        employee_map = {emp.id: emp for emp in employees}
        return dfs(id)
