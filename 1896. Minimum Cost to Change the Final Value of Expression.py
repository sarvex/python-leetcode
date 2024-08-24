class Solution:
  def minOperationsToFlip(self, expression: str) -> int:
    def rec(i):
      if expression[i] == ")":
        e1val, e1cost, i = rec(i - 1)
      else:
        e1val = int(expression[i])
        e1cost = 1
      i -= 1

      if i < 0:
        return e1val, e1cost, i
      elif expression[i] == "(":
        return e1val, e1cost, i

      op = expression[i]
      e2val, e2cost, i = rec(i - 1)
      if i >= 0 and expression[i] != "(":
        i -= 1

      if op == "|":
        val = e1val | e2val
        cost_case = 0 if e1val == e2val == 0 else 1
      else:
        val = e1val & e2val
        cost_case = 1 if e1val == e2val == 0 else 0

      if e1val != e2val:
        cost = 1
      elif cost_case == 0:
        cost = min(e1cost, e2cost)
      else:
        cost = min(e1cost + e2cost, e1cost + 1, e2cost + 1)
      return val, cost, i

    return rec(len(expression) - 1)[1]
