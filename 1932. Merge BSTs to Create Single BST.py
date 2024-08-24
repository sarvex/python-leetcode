from sys import maxsize
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:

    leaves = set()
    treeDict = {}

    for tree in trees:
      treeDict[tree.val] = tree
      if tree.left:
        leaves.add(tree.left.val)
      if tree.right:
        leaves.add(tree.right.val)

    root = None

    for tree in trees:
      if tree.val not in leaves:
        root = tree
        break

    if not root:
      return None

    curleaves = {}
    if root.left:
      curleaves[root.left.val] = (-maxsize, root.val, root, 0)

    if root.right:
      curleaves[root.right.val] = (root.val, maxsize, root, 1)

    del treeDict[root.val]

    while treeDict:
      findTree = False
      for leaf, (low, high, par, lor) in curleaves.items():
        if leaf in treeDict:
          newTree = treeDict[leaf]
          del curleaves[leaf]

          if newTree.left:
            if low < newTree.left.val < high and newTree.left.val not in curleaves:
              curleaves[newTree.left.val] = (low, newTree.val, newTree, 0)
            else:
              return None
          if newTree.right:
            if low < newTree.right.val < high and newTree.right.val not in curleaves:
              curleaves[newTree.right.val] = (newTree.val, high, newTree, 1)
            else:
              return None

          if lor == 0:
            par.left = newTree
          else:
            par.right = newTree

          findTree = True
          del treeDict[newTree.val]
          break
      if not findTree:
        return None
    return root
