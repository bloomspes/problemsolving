# 문제 해설
# 열린 사과의 갯수와, 사과가 썩기 까지 걸리는 일의 수가 주어진다.

# apples = [3, 5, 7] days = [1, 3] 이라고 한다면

# 1 day = 사과 3개가 열리고 나는 1개를 섭취한다. remains = 2
# 2 day = 첫 째날에 남아있는 사과는 모두 썩는다. 사과가 5개가 열렸고 1개를 먹는다.
# 3 day = 둘 째날에 열린 사과 1개를 먹는다.

# 이렇게 내가 먹을 수 있는 사과의 갯수 n = 3개이다.
# 열리는 사과의 수와 사과가 썩는 날을 파악해서
# 썩은 사과는 내보내고, 남아있는 사과를 계산하는 알고리즘을 작성한다.

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        ans = 0
        pq = []
        rotting_apples = list(zip(apples, days))
