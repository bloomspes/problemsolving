class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 0, maxSum + 1
        answer = 0

        while left < right:
            mid_index = (left + right) // 2

            left_part = min(mid_index - 1, index + 1)
            right_part = min(mid_index - 1, n - index)

            left_sum = (mid_index - left_part + mid_index - 1) * left_part // 2
            right_sum = (mid_index - right_part +
                         mid_index - 1) * right_part // 2

            total_sum = left_sum + right_sum - mid_index + 1 + n

            if total_sum <= maxSum:
                left = mid_index + 1
            else:
                right = mid_index

        answer = left - 1

        return answer
