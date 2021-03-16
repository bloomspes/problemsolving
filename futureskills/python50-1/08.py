# 리스트의 차집합을 변환하는 코드 작성

lst1 = [1, 2, 3]
lst2 = [1, 2, 4]


def difference(lst1, lst2):
    lst2_ = set(lst2)
    return [item for item in lst1 if item not in lst2_]


print(difference(lst1, lst2))
