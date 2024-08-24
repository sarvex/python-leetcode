from collections import defaultdict
from typing import List


class Node:
  def __init__(self, ind=None):
    self.ind = ind
    self.d = defaultdict(Node)


class Solution:
  def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
    root = Node()
    for ind, path in enumerate(paths):
      cur = root
      for node in path:
        cur = cur.d[node]
      cur.ind = ind

    hashes = defaultdict(list)
    rev = {}

    # encode: 50 bits node, up to 500 * 50 = 25 000 bit path
    def dfs(node, val, ind):
      if not node:
        return 0
      childs = []
      for child in node.d:
        childs.append(dfs(node.d[child], child, node.d[child].ind))
      cur = hash(tuple(sorted(childs)))
      if ind >= 0:
        hashes[cur].append(ind)
        rev[ind] = cur
      return hash((cur, val))

    dfs(root, 'a', - 1)
    mark = [False] * len(paths)

    def dfs1(node, marked=False):
      if node.ind is not None and node.d and len(hashes[rev[node.ind]]) > 1:
        marked = True
      if node.ind is not None:
        mark[node.ind] = marked
      for child in node.d:
        dfs1(node.d[child], marked)

    dfs1(root)

    return [paths[i] for i in range(len(paths)) if not mark[i]]
