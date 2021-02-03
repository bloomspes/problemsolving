# You are given two strings a and b that consist of lowercase letters.
# In one operation, you can change any character in a or b to any lowercase letter.
# Your goal is to satisfy one of the following three conditions:
#
#
# Every letter in a is strictly less than every letter in b in the alphabet.
# Every letter in b is strictly less than every letter in a in the alphabet.
# Both a and b consist of only one distinct letter.

from collections import Counter
import string


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        dict_a = Counter(a)
        dict_b = Counter(b)

        ans = len(a) + len(b)

        a_less_than_b = [0 for _ in range(26)]
        b_less_than_a = [0 for _ in range(26)]

        a_less_than_b[0] = dict_a["a"]
        b_less_than_a[0] = dict_b["a"]

        for i in range(1, 26):
            a_less_than_b[i] = a_less_than_b[i - 1] + dict_a[string.ascii_lowercase[i]]
            b_less_than_a[i] = b_less_than_a[i - 1] + dict_b[string.ascii_lowercase[i]]

        for i in range(25):
            ans = min(
                ans,
                (a_less_than_b[i] + len(b) - b_less_than_a[i]),
                (b_less_than_a[i] + len(a) - a_less_than_b[i]),
            )

        for char in string.ascii_lowercase:
            ans = min(ans, len(a) + len(b) - dict_a[char] - dict_b[char])

        return ans
