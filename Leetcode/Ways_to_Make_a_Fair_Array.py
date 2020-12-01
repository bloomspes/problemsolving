# 문제 해설
# list의 value가 remove 되면 list의 element들이 재정렬 된다.
# 주어진 list의 odd index element 합 = even index element 합 인 경우 fair 하다
# element를 제거 해서 리스트가 fair 한 경우 제거할 수 있는 index의 수를 반환 한다.
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # ans = []

        # for i in range(len(nums)):
        #   if (i % 2 == 0):
        #       even_index += nums[i]
        #   else:
        #       odd_index += nums[i]

        odd_sum = [0]*(n+1)
        even_sum = [0]*(n+1)

        for i, k in enumerate(nums):
            if (i % 2 == 0):
                even_sum[i+1] = even_sum[i] + k
                odd_sum[i+1] = odd_sum[i]

            else:
                odd_sum[i+1] = odd_sum[i] + k
                even_sum[i+1] = even_sum[i]

        answer = 0
