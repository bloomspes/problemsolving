# 숫자를 자릿수를 기준으로 분리해서 리스트로 만드는 코드를 작성하세요
a = 123


def digitize(n):
    return list(map(int, str(n)))


print(digitize(a))
