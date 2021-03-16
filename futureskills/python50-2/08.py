# 리스트에 중복된 값이 있다면 True를 없다면 False를 반환하는 코드를 작성하세요.

lst = [1, 2, 3]


def has_duplicates(lst):
    return len(lst) == len(set(lst))


print(has_duplicates(lst))
