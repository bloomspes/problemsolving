class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1 = []
        word2 = []

        word1_sum = sum(word1)
        word2_sum = sum(word2)

        if (word1_sum == word2_sum):
            return True
        else:
            return False
