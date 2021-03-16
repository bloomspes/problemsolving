# degrees 를 rads로 변환 하는 코드를 작성하세요.

from math import degrees, pi
degrees = 180


def degrees_to_rads(degrees):
    return degrees * pi / 180.0


print(degrees_to_rads(degrees))
