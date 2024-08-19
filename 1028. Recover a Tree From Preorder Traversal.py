from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
    stack = []
    i = 0

    while i < len(traversal):
      depth = 0
      while traversal[i] == '-':
        depth += 1
        i += 1

      value = ''
      while i < len(traversal) and traversal[i] != '-':
        value += traversal[i]
        i += 1
      value = int(value)

      current = TreeNode(val=value)

      while stack and len(stack) > depth:
        stack.pop()

      if stack:
        if stack[-1].left is None:
          stack[-1].left = current
        else:
          stack[-1].right = current

      stack.append(current)
    return stack[0]
