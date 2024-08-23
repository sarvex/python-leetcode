from typing import List


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
class Solution:
  def findSecretWord(self, words: List[str], master: 'Master') -> None:
    freq_at_positions = []
    for i in range(6):
      pos_count = {}
      for word in words:
        if (word[i] in pos_count):
          pos_count[word[i]] += 1
        else:
          pos_count[word[i]] = 1
      freq_at_positions.append(pos_count)

    def calc_score(w):
      s = 0
      for i in range(len(w)):
        s += freq_at_positions[i][w[i]]
      return s

    words.sort(key=lambda word: calc_score(word))

    def find_common_sum(w1, w2):
      common_sum = 0
      for i in range(6):
        if (w1[i] == w2[i]): common_sum += 1
      return common_sum

    while (len(words) > 0):
      word = words.pop()
      matches = master.guess(word)

      if (matches == 6):
        break
      else:
        words = [w for w in words if matches == find_common_sum(w, word)]
