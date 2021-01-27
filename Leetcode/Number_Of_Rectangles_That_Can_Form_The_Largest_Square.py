# 문제 해설
# 주어진 사각형을 rectangles 라고 하고 retangles의 높이, 너비의 값이 각각 l과 w로 주어진다.
# 정사각형의 너비의 길이를 k라고 했을 때, k의 값은 k <= l and k <= w를 만족하는 최댓값이다.
# regtangles 로 부터 k 값을 리턴 받을 때, 가장 길이가 긴 정사각형의 갯수를 구하시오.


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        square = []
        for i in rectangles:
            square.append(min(i))

        maximum = max(square)
        ans = square.count(maximum)
        return ans
