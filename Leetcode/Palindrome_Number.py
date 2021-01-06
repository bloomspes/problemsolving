class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        return True if (x >= 0 and a == a[::-1]) else False
