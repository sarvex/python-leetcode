from collections import Counter


class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        """Build a display table of food orders grouped by table number.

        Intuition:
            Aggregate food orders by table and food item, then format as
            a sorted table with food names as column headers.

        Approach:
            Collect unique table numbers and food names. Count orders per
            table-food pair using a counter. Build the header row and data
            rows sorted by table number.

        Complexity:
            Time: O(n + t * f * log(f)) where t is tables and f is foods
            Space: O(n) for the counter and result
        """
        table_numbers: set[int] = set()
        food_names: set[str] = set()
        order_counts: Counter[str] = Counter()
        for _, table, food in orders:
            table_numbers.add(int(table))
            food_names.add(food)
            order_counts[f"{table}.{food}"] += 1
        sorted_foods = sorted(food_names)
        sorted_tables = sorted(table_numbers)
        result: list[list[str]] = [["Table"] + sorted_foods]
        for table in sorted_tables:
            row = [str(table)]
            for food in sorted_foods:
                row.append(str(order_counts[f"{table}.{food}"]))
            result.append(row)
        return result
