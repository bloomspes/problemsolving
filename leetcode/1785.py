# You are given an integer array nums and two integers limit and goal.
# The array nums has an interesting property that abs(nums[i]) <= limit.
# Return the minimum number of elements you need to add to make the sum of the array equal to goal.
# The array Note that abs(x) equals x if x >= 0, and -x otherwise.

# 1 -10 9 1 -1 // can add -1
# goal을 만족 시키는 element 수를 return하기

import math


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        answer = 0

        array = sum(nums)
        d = abs(goal - array)

        answer = ceil(d / limit)
        return answer
