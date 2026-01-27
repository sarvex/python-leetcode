class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """Transform words by Goat Latin rules with vowel/consonant handling.

        Intuition:
            Apply simple string transformations per word: move consonant to end
            if needed, append 'ma', then append increasing 'a's.

        Approach:
            1. Split sentence into words.
            2. For each word, if it starts with a consonant, move the first
               letter to the end.
            3. Append 'ma' and (i+1) 'a's where i is the word index.

        Complexity:
            Time: O(n * m) where n = number of words, m = max word length
            Space: O(n * m)
        """
        vowels = set("aeiouAEIOU")
        result: list[str] = []
        for i, word in enumerate(sentence.split()):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += "ma"
            word += "a" * (i + 1)
            result.append(word)
        return " ".join(result)
