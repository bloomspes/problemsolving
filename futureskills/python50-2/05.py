# 리스트에서 unique한 값들만 제거하는 코드 작성

from collections import Counter

lst = [1, 2, 2, 3, 4, 4, 5]


def filter_unique(lst):
    return [item for item, count in Counter(lst).items() if count > 1]


print(filter_unique(lst))
