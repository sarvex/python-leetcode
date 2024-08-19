class Solution:
  def countOrders(self, n: int) -> int:
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(2, n + 1):
      ans = (ans * i * (2 * i - 1)) % mod
    return ans
