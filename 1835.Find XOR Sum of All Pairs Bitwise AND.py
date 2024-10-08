from functools import reduce
from operator import xor
from typing import List


class Solution:
  def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
    a = reduce(xor, arr1)
    b = reduce(xor, arr2)
    return a & b
