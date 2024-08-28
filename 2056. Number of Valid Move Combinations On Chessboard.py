from typing import List


class Solution:
  def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
    moves = ((1, 0), (- 1, 0), (0, 1), (0, - 1), (1, 1), (- 1, - 1), (1, - 1), (- 1, 1))
    pmoves = {"queen": moves[:], "bishop": moves[- 4:], "rook": moves[:4]}

    def enc(x, y, t):
      return 1 << ((x - 1) + 8 * (y - 1) + 64 * (t - 1))

    def search(mask, i):
      if i == len(pieces):
        return 1
      res = 0
      # stay option
      cur = positions[i]
      cur_enc = sum(enc(*cur, t) for t in range(1, 8))
      if cur_enc & mask == 0:
        res += search(mask ^ cur_enc, i + 1)
      # move option
      for move in pmoves[pieces[i]]:
        cur = list(positions[i])
        cur_enc = 0
        for t in range(1, 8):
          for dim in range(2):
            cur[dim] += move[dim]
          if not all(1 <= cur[dim] <= 8 for dim in range(2)):
            break
          cur_enc ^= enc(*cur, t)
          remains = sum(enc(*cur, nt) for nt in range(t + 1, 8))
          if (cur_enc ^ remains) & mask == 0:
            res += search(mask ^ cur_enc ^ remains, i + 1)
      return res

    return search(0, 0)
