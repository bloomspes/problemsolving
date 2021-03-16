# 왼쪽으로부터 n개의 값이 제거된 리스트를 반환하는 코드 작성

def drop(lst, n=1):
    return lst[n:]


print(drop([1, 2, 3]))
print(drop([1, 2, 3], 2))
print(drop([1, 2, 3], 42))
