import re
from collections import Counter


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        count = 0

        result = re.sub('[a-zA-Z]', " ", word)
        nums = [int(i) for i in result.split()]
        nums_dict = Counter(nums)

        return len(nums_dict)
