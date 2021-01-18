# 문제 해설
# 원래의 arr 구하기
# arr[i] = encoded[i-1] ^ arr[i-1]

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for i in encoded:
            arr.append(arr[-1] ^ i)
        return arr
