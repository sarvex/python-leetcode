from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def maxSumBST(self, root: Optional[TreeNode]) -> int:
    def search(root: Optional[TreeNode]) -> tuple:
      if root is None:
        return 1, inf, -inf, 0
      lbst, lmi, lmx, ls = search(root.left)
      rbst, rmi, rmx, rs = search(root.right)
      if lbst and rbst and lmx < root.val < rmi:
        nonlocal ans
        s = ls + rs + root.val
        ans = max(ans, s)
        return 1, min(lmi, root.val), max(rmx, root.val), s
      return 0, 0, 0, 0

    ans = 0
    search(root)
    return ans
