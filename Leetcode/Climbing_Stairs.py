# 문제 해설
# n개의 계단을 오르는 방법은 1st, 2st 이렇게 두 종류이다.
# dp[1] = 1, dp[2] = 2, dp[3] = 3, dp[4] = 5 = dp[3] + dp[2]
# dp[k] = dp[k-1] + dp[k-2]

# tc : O(1) (n이 45까지 이므로)

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = ""
        dp = [0 for k in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        if (n == 1):
            ans = dp[1]
            return ans

        elif (n == 2):
            ans = dp[2]
            return ans

        else:
            for k in range(3, n+1):
                dp[k] = dp[k-1] + dp[k-2]
                ans = dp[n]
                return ans
