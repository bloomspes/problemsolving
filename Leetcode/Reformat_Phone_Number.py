# 문제 해설
# 공백, 대쉬 없는 문자열로 치환
# 3문자 씩 끊어서 대쉬 붙이고 리턴하기
# 반복 루프를 진행하는 경우, 3개씩 끊어서 그 뒤의 문자열을 탐색해야 하므로 for 보다는 while loop가 좋음.
# O(n/3) / O(n)

import re


class Solution:
    def reformatNumber(self, number: str) -> str:

        number = re.sub('[ -]', '', number)
        ans = ""

        while len(number) > 3:
            ans += number[0:2] + "-"
            number = number[2:]

        if len(number) == 3:
            ans += number[:2] + "-" + number[2:]

        else:
            ans += number

        return ans
