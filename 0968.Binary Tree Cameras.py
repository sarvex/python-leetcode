from math import inf
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
  def minCameraCover(self, root: Optional[TreeNode]) -> int:
    def search(root):
      if root is None:
        return inf, 0, 0
      la, lb, lc = search(root.left)
      ra, rb, rc = search(root.right)
      a = min(la, lb, lc) + min(ra, rb, rc) + 1
      b = min(la + rb, lb + ra, la + ra)
      c = lb + rb
      return a, b, c

    a, b, _ = search(root)
    return min(a, b)
