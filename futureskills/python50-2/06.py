# itr 리스트의 각 원소에 주어진 함수 fn 을 실행하는 함수 작성

itr = [1, 2, 3]
fn = print


def for_each(itr, fn):
    [fn(x) for x in itr if len(itr) != 0]


print(for_each(itr, fn))
