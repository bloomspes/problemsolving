# 리스트에서 주어진 값이 몇개 있는지 알려주는 코드를 작성하세요.

lst = [1, 1, 2, 1, 2, 3]


def count_occurences(lst, val):
    return len([i for i in lst if i == val and type(i) == type(val)])


print(count_occurences([1, 1, 2, 1, 2, 3], 1))
