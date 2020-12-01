# 문제 해설
# 소문자 문자를 각각 숫자로 대응 a = 1, b = 2, c = 3, ..., z = 26
# string 값은 각각 알파벳에 해당하는 index의 합 이다. "abe" = 1+2+5 = 8
# lexicographically = 사전에 기록된 순서대로, 사전순으로
# 그러니까, 길이가 n이고 숫자값이 k인 사전식으로 가장 작은 문자열을 반환 하라는게 이 문제의 요점.

# 문제 조건
# index_sum = k, string_length = n
# string 뽑아낼때 a b c.... 순서대로 출력할 것

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # dict_value = list(string.ascii_lowercase)
        # dict = {string : i for i, string in enumerate(dict_value)}
        #   for key in dict:
        #       dict[key] += 1
        #   print(dict)
        #   list_value = dict.values()

        k = k - n
        list = ['a']*n

        for i in range(n-1, -1, -1):
            dict_value = min(k, 25)
            list[i] = chr(dict_value + 97)
            k = k - dict_value

        return ''.join(list)
