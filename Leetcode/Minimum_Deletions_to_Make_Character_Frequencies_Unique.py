# 문제 해설
# 동일한 중복을 갖는 문자열이 두 종류 이상이 아닌 경우 => 통과
# 서로 다른 두 문자열이 동일한 빈도로 중복을 가질 때 => good을 반환하기 위해 필요한 최소의 delete 수 반환

import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        # O(N) / O(N)
        # count.values() 의 길이를 n / len(s) 의 값을 m이라 했을 때
        # O(max(n, m)) = worst case

        ans = 0

        count = collections.Counter(s)
        print(count)

        freq = collections.Counter()

        for i in count.values():
            freq[i] += 1
        for i in range(len(s), 0, -1):
            if freq[i] > 1:
                delete = freq[i] - 1
                ans += delete
                freq[i-1] += delete

        return ans
