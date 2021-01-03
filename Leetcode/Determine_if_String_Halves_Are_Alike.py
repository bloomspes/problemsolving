# 문제 해설
# 짝수개의 string을 s에 저장한다.
# string을 반으로 갈라서 앞의 반개는 a에, 뒤의 반개는 b에 저장.
# a와 b의 모음 갯수가 서로 같으면 alike 리턴.
# 모음에서 대/소문자 구분 된다.

# 풀이 방법
# a와 b로 나눠서 갯수를 비교하는 방법을 일차적으로 떠올렸지만
# 더 메모리를 적게 쓰고 사용하는 방법은 없을지 고민.
# 굳이 a와 b로 나눌 필요가 없이
# 한 문장 내에서 모음 갯수를 비교하면 되는데, 이를 왼쪽에서 카운트 하는 횟수와 오른쪽에서 카운트 하는 횟수로 나눠서 풀이
# 두 횟수가 같은 경우에 bool값 리턴해주면 끝.

# 시간복잡도 : O(n) / 공간복잡도: O(1)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left_pointer = 0
        right_pointer = 0

        for i in range(len(s)//2):
            if s[i] in vowel:
                left_pointer += 1
            if s[(len(s) - 1) - i] in vowel:
                right_pointer += 1

        return left_pointer == right_pointer
