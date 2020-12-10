# 내일 풀기
# 미분 관점에서 생각해서 풀어 볼 것 (스터디에서 힌트를 얻었다.)

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        ans = []

        for i in range(len(nums) // 2):
            moves = min(nums[i])
