# stack 을 이용하면 쉽다
# len(stack) + len(nums) - i == k 일때 까지
# loop 반복
# 이걸 우선순위 큐로 바꿔서 다시 풀어 보기


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []

        for i in range(len(nums)):
            while stack and len(stack) + len(nums) - i > k:
                stack.pop()
            stack.append(nums[i])

        return stack[:k]
