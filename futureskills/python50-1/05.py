# 리스트에서 false 인 원소 제거하는 코드 작성

lst = [0, 1, False, 2, '', 3, 'a', 's', 34]


def compact(lst):
    return list(filter(None, lst))


print(compact(lst))
