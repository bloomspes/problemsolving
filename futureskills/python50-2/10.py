# n이 start 와 end 사이에 있는 값인지 확인하는 코드를 작성하세요.
# (단, end 를 지정하지 않을 경우, 0 부터 start 까지로 간주하도록 하세요.)

def in_range(n, start, end=0):
    return start <= n <= end if end >= start else end <= n <= start
