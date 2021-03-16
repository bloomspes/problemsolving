# 오른쪽으로부터 n개의 값이 끝에서 부터 제거된 리스트 반환 코드

def drop_right(lst, n=1):
    return lst[:-n]


print(drop_right([1, 2, 3]))
print(drop_right([1, 2, 3], 2))
print(drop_right([1, 2, 3], 42))
