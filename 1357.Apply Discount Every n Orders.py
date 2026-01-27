class Cashier:
    """Cashier system that applies a discount every n-th customer.

    Intuition:
        Track the customer count and apply the percentage discount on every
        n-th order by reducing each item's cost proportionally.

    Approach:
        Store product prices in a dictionary for O(1) lookup. Maintain a
        counter incremented on each getBill call. When the counter is
        divisible by n, apply the discount percentage to the total bill.

    Complexity:
        Time: O(m) per getBill where m is the number of products purchased.
        Space: O(p) where p is the number of distinct products.
    """

    def __init__(
        self, n: int, discount: int, products: list[int], prices: list[int]
    ) -> None:
        self.customer_count = 0
        self.frequency = n
        self.discount = discount
        self.price_map: dict[int, int] = dict(zip(products, prices))

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.customer_count += 1
        discount = self.discount if self.customer_count % self.frequency == 0 else 0
        total = 0.0
        for prod, qty in zip(product, amount):
            item_cost = self.price_map[prod] * qty
            total += item_cost - (discount * item_cost) / 100
        return total
