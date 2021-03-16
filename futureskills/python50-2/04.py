# 리스트에서 non-unique 값 제거하는 코드 작성하기

from typing import Counter


lst = [1, 2, 2, 3, 4, 4, 5]


def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count == 1]


print(filter_non_unique(lst))
