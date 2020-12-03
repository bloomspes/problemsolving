# 문제 해설
# 2xn 크기의 직사각형을 채우는 방법은 1x2가 왔을 경우, 2x1이 두개 왔을 경우
# 두 가지로 나뉘어 질 수 있다
# 각각의 경우의 수를 더하면 끝

n = int(input())

dp = [0 for i in range(n+1)]
print(dp)

dp[0] = 1
dp[1] = 1
print(dp)

ans = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    ans = dp[n] % 10007

print(ans)
