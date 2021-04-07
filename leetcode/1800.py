class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cnt, ans = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += nums[i]
            else:
                cnt = nums[i]
            ans = max(ans, cnt)

        return ans
