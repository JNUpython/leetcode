# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 14:11
# @Author  : kean
# @Email   : ?
# @File    : two_sum.py
# @Software: PyCharm

"""
Share
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_set = set(nums)
        maxv = max(nums)
        minv = min(nums)
        for indx in range(len(nums)):
            x1 = nums[indx]
            x2 = target - x1
            if x2 > maxv or x2 < minv or x2 not in nums_set:
                continue
            sub_nums = nums[indx + 1:]
            if x2 in set(sub_nums):
                return [indx, indx + sub_nums.index(x2) + 1]
        return []


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print(solution.twoSum(nums, target))
