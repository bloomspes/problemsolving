# 문제 해설
# 열린 사과의 갯수와, 사과가 썩기 까지 걸리는 일의 수가 주어진다.

# apples = [3, 5, 7] days = [1, 3] 이라고 한다면

# 1 day = 사과 3개가 열리고 나는 1개를 섭취한다. remains = 2
# 2 day = 첫 째날에 남아있는 사과는 모두 썩는다. 사과가 5개가 열렸고 1개를 먹는다.
# 3 day = 둘 째날에 열린 사과 1개를 먹는다.

# 내가 먹을 수 있는 사과의 갯수를 최대로 늘리려면 어떻게 해야 할까?
# 사과가 썩는 날은 i와 days[i]의 영향을 받는다.
# 그러므로 사과의 freshness(== 썩기까지 남은 시간)가 가장 떨어지는 사과부터 먹는다.
# freshness를 기준점으로 min-heap 구현


from heapq import heappush as push
from heapq import heappop as pop

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        # 최소 힙 구현
        heap = []
        i= 0
        ans = 0
        
        while True:
            if i < len(apples) and apples[i] > 0:
                push(heap, [i+days[i], apples[i]])
            
            while heap and (heap[0][0] <= i or heap[0][1] <= 0):
                pop(heap)
            if heap:
                heap[0][1] -= 1
                ans += 1
            
            i += 1
        
        return ans
            