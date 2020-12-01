# 문제 해설
# pointer 값이 가리키고 있는 인덱스가 가진 value를 반환한다.
# 구해야 할 것은 pointer == id 구간 에서의 stream chunk를 리턴하는 일 이다.
# pointer의 값은 1부터 시작하므로 초기값은 1로 지정한다.

# O(N) / O(N)

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.stream = [""] * (n+1)

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        res = []

        if id == self.ptr:
            # stream의 ptr 번째 엘리먼트가 0 or none 이면 true 반환
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1

        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
