# 문제 해설
# [박스의 수, 박스당 담겨있는 유닛(컨테이너)의 수]
# 그런고로, 최대로 들어갈 수 있는 유닛의 수를 구하시오.

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        # boxTypes.sort(reverse=True)
        # 왜 안되지 생각했다가.. 아차..! (2차원 배열이었지...)
        boxTypes.sort(key=lambda x: -x[-1])
        unit = 0

        for i, j in enumerate(boxTypes):
            if boxTypes[i][0] <= truckSize:
                unit += (boxTypes[i][0] * boxTypes[i][1])
                truckSize -= boxTypes[i][0]

            else:
                unit += truckSize * boxTypes[i][1]
                truckSize = 0

        return unit
