from functools import cmp_to_key
from typing import List


class Expr:
  def __init__(self):
    self.coef = 0
    self.vars = []

  def getVal(self):
    if not self.coef:
      return ""
    if not self.vars:
      return str(self.coef)
    return str(self.coef) + "*" + "*".join(self.vars)


def mul(expr1, expr2):
  ret = Expr()
  ret.coef = expr1.coef * expr2.coef
  if ret.coef == 0:
    return ret
  ret.vars = list(sorted(expr1.vars + expr2.vars))
  return ret


def mergeExpr(stack, signs, expr):
  sign = signs[-1][-1]
  match sign:
    case "+":
      stack[-1].append([expr])
    case "-":
      expr.coef = - expr.coef
      stack[-1].append([expr])
    case "*":
      last = stack[-1][-1]
      temp = []
      for prev in last:
        temp.append(mul(prev, expr))
      stack[-1][-1] = temp
  signs[-1].pop()


def mergeGroup(stack, signs, group):
  sign = signs[-1][-1]
  match sign:
    case "+":
      stack[-1].append(group)
    case "-":
      temp = []
      for expr in group:
        expr.coef = -expr.coef
        temp.append(expr)
      stack[-1].append(temp)
    case "*":
      last = stack[-1].pop()
      temp = []
      for expr1 in last:
        for expr2 in group:
          temp.append(mul(expr1, expr2))
      stack[-1].append(temp)
  signs[-1].pop()


def compare(c, d):
  a, b = c.split("*"), d.split("*")
  if len(a) != len(b):
    return len(b) - len(a)
  return 1 if a > b else -1


def getSum(curLevel):
  exprs = {"": 0}
  for groups in curLevel:
    for expr in groups:
      if not expr.vars:
        exprs[""] += expr.coef
      else:
        key = "*".join(expr.vars)
        if key not in exprs:
          exprs[key] = expr
        else:
          exprs[key].coef += expr.coef
  ret = [exprs[key] for key in sorted(exprs.keys(), key=cmp_to_key(compare)) if key != "" and exprs[key].coef]

  if exprs[""] != 0:
    temp = Expr()
    temp.coef = exprs[""]
    ret.append(temp)
  return ret


def calculate(s, a, b):
  stack, signs = [[]], [["+"]]
  i, n = 0, len(s)
  dic = {x: y for x, y in zip(a, b)}
  while i < n:
    if s[i] == " ":
      i += 1
      continue
    if s[i].isalpha():
      expr = Expr()
      temp = s[i]
      while i + 1 < n and s[i + 1].isalpha():
        temp += s[i + 1]
        i += 1
      if temp in dic:
        expr.coef = dic[temp]
      else:
        expr.coef = 1
        expr.vars = [temp]
      mergeExpr(stack, signs, expr)
    elif s[i].isdigit():
      expr = Expr()
      num = int(s[i])
      while i + 1 < n and s[i + 1].isdigit():
        num = num * 10 + int(s[i + 1])
        i += 1
      expr.coef = num
      mergeExpr(stack, signs, expr)
    elif s[i] in "+-*":
      signs[-1].append(s[i])
    elif s[i] == "(":
      stack.append([])
      signs.append(["+"])
    elif s[i] == ")":
      curLevel = getSum(stack.pop())
      signs.pop()
      mergeGroup(stack, signs, curLevel)
    i += 1
  res = getSum(stack.pop())
  return [expr.getVal() for expr in res]


class Solution:
  def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
    return calculate(expression, evalvars, evalints)
