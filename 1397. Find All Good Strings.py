class Solution:
  def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
    p = 10 ** 9 + 7
    ord_a = ord('a')
    l = len(evil)
    dup = []
    for i in range(1, l):
      if evil[i:] == evil[:l - i]:
        dup.append(i)
    lend = len(dup)

    def count(s):
      tmp_ct = 0
      bd = 1
      ind = n
      without_s = []
      for i in range(n):
        tmp_ct *= 26
        if bd:
          tmp_ct += ord(s[i]) - ord_a
        if i >= l - 1 and ind > i - l and evil < s[i - l + 1:i + 1]:
          tmp_ct -= 1
        if i >= l:
          tmp_ct -= without_s[i - l]
        if i >= l - 1:
          if s[i - l + 1:i + 1] == evil:
            bd = 0
            ind = i
        tmp_ct %= p
        tmp_with_s = 0
        for j in range(lend):
          d = dup[j]
          if i >= d:
            tmp_with_s += without_s[i - d]
          if i >= d - 1 and ind > i - d and evil[:d] < s[i - d + 1:i + 1]:
            tmp_with_s += 1
        without_s.append(tmp_ct - tmp_with_s)
      return tmp_ct, bd

    str_ct1, bd1 = count(s1)
    str_ct2, bd2 = count(s2)
    return (str_ct2 - str_ct1 + bd2) % p
