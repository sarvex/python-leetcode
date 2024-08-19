class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    def search(a: int, fa: int):
      nonlocal now
      now += 1
      dfn[a] = low[a] = now
      for b in g[a]:
        if b == fa:
          continue
        if not dfn[b]:
          search(b, a)
          low[a] = min(low[a], low[b])
          if low[b] > dfn[a]:
            ans.append([a, b])
        else:
          low[a] = min(low[a], dfn[b])

    g = [[] for _ in range(n)]
    for a, b in connections:
      g[a].append(b)
      g[b].append(a)

    dfn = [0] * n
    low = [0] * n
    now = 0
    ans = []
    search(0, -1)
    return ans
