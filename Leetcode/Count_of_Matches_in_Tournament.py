# 문제 해설
# 짝수팀 : matches = n/2, advance = n/2
# 홀수팀 : matches = (n-1)/2, advance = (n-1)/2 + 1

# O(1) / O(1)
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1


# O(N) / O(1)
class otherSolution:
    def otherSolutions(self, n: int) -> int:
        ans = 0
        for n in range(0, n):
            ans += n//2
            n = n//2 + (n & 1)
        return ans
