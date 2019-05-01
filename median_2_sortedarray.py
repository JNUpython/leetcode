# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 10:26
# @Author  : kean
# @Email   : ?
# @File    : median_2_sortedarray.py
# @Software: PyCharm

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        n = len(nums1) + len(nums2)
        for indx in range(n // 2 + 1):
            cond1 = self.func1(nums1, nums2)
            if cond1 is not None:
                return cond1
            nums1, nums2 = self.func2(nums1, nums2)


    def func1(self, nums1, nums2):
        nums12 = None
        if not nums1 or not nums2 or (len(nums1) == 1 and len(nums2) == 1):
            nums12 = nums1 + nums2
        else:
            n1_left = nums1[0]
            n1_right = nums1[-1]
            n2_left = nums2[0]
            n2_right = nums2[-1]
            if n1_right <= n2_left:
                nums12 = nums1 + nums2
            if n2_right <= n1_left:
                nums12 = nums2 + nums1
        if nums12:
            n = len(nums12)
            div, mod = divmod(n, 2)
            if mod == 0:
                return (nums12[div - 1] + nums12[div]) / 2
            else:
                return nums12[div]
        else:
            return None

    def func2(self, nums1, nums2):
        if not nums1 or not nums2:
            return nums1 + nums2, []
        n1l = nums1[0]
        n1r = nums1[-1]
        n2l = nums2[0]
        n2r = nums2[-1]
        if n1l <= n2l:
            nums1 = nums1[1:]
        else:
            nums2 = nums2[1:]
        if n1r >= n2r:
            nums1 = nums1[:-1]
        else:
            nums2 = nums2[:-1]
        return nums1, nums2






