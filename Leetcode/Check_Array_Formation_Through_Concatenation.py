# 문제 해설
# arr 라는 정수를 담아놓은 배열이 있고, pieces라는 배열은 정수를 담은 배열 자체를 원소로 가지는 배열이다.
# pieces 안의 원소를 서로 연결 시켜서 arr의 배열을 구성하는 것이 문제의 핵심이다.
# 이 때, pieces 안의 배열의 원소를 재정렬 하는 것은 허용되지 않는다.
# arr를 만들 수 있으면 true, 그렇지 못하면 false를 반환한다.


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if not arr and not pieces:
            return true
        if not arr or not pieces:
            return false

        answer = list()  # 결과 담아서 arr 리스트에 리턴

        hashmap = dict()  # hashmap 구현
        for p in pieces:
            hashmap[p[0]] = p
            print(hashmap)

        for a in arr:
            if a in hashmap:
                answer.extend(hashmap[a])
            print(answer)

        return arr == answer
