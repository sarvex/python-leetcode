from typing import List


# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children


class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    def search(root):
      if root is None:
        return
      for child in root.children:
        search(child)
      ans.append(root.val)

    ans = []
    search(root)
    return ans
