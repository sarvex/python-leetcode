class Solution:
  def minSteps(self, n: int) -> int:
    @cache
    def search(n):
      if n == 1:
        return 0
      i, ans = 2, n
      while i * i <= n:
        if n % i == 0:
          ans = min(ans, search(n // i) + i)
        i += 1
      return ans

    return search(n)
