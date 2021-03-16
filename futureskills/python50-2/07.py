# itr 리스트의 각 원소에 주어진 함수 fn를 리스트의 마지막 값부터 실행하는 함수를 작성하세요.

itr = [1, 2, 3]


def for_each_right(itr, fn):
    [fn(x) for x in itr[::-1]]


for_each_right(itr, print)
