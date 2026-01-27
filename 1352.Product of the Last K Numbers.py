class ProductOfNumbers:
    """Supports adding numbers and querying the product of the last k numbers.

    Intuition:
        Maintain a prefix product list so that the product of the last k
        elements is simply the ratio of the last prefix product to the one
        k positions earlier.

    Approach:
        Store cumulative products in a list. When a zero is added, reset the
        list since any product including zero is zero. For getProduct, if k
        exceeds the list length (meaning a zero appeared), return 0; otherwise
        return the ratio of the last two relevant prefix products.

    Complexity:
        Time: O(1) per add and getProduct call.
        Space: O(n) where n is the number of added elements since last zero.
    """

    def __init__(self) -> None:
        self.prefix_products: list[int] = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
            return
        self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.prefix_products) <= k:
            return 0
        return self.prefix_products[-1] // self.prefix_products[-k - 1]
