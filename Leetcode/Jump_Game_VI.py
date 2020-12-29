# 문제 해설
# index 0번 부터 시작, 뛸 수 있는 최대 스텝수는 k이다.
# 내가 있는 인덱스를 기준으로 해서 sum을 최대화 하려면 다음 인덱스의 값이 가장 큰 것으로 이동해야 된다.
# 파이썬 내장 모듈인 heapq 사용

import heapq

#      1  ---> root
#    /   \
#   3     5
#  / \   /
# 4   8 7


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        score = []
        pq = []

        for i, num in enumerate(nums):
            if i == 0:
                score.append(num)
                heapq.heappush(pq, (-num, 0))
            else:
                while pq[0][1] < i - k:
                    heapq.heappop(pq)

                max_score, j = pq[0]
                score.append(-max_score + num)
                heapq.heappush(pq, (-score[-1], i))

        return score[-1]
