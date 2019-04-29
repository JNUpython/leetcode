# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 22:00
# @Author  : kean
# @Email   : ?
# @File    : add_2_numbers.py
# @Software: PyCharm

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def parse(self, l):
        now = l
        res = []
        while now:
            res.append(now.val)
            now = now.next
        return res

    def __str__(self):
        return "".join([str(_) for _ in reversed(self.parse(self))])


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.parse(l1)
        l2 = self.parse(l2)
        l1_len = len(l1)
        l2_len = len(l2)
        diff_len = l1_len - l2_len
        if diff_len > 0:
            l2 += [0] * diff_len
        if diff_len < 0:
            l1 += [0] * (- diff_len)
        res = []
        add_next = 0
        for v1, v2 in zip(l1, l2):
            div, mod = divmod(v1 + v2 + add_next, 10)
            res.append(mod)
            add_next = div
        if add_next:
            res.append(add_next)
        # print(res)
        return self.create(res)

    def parse(self, l):
        now = l
        res = []
        while now:
            res.append(now.val)
            now = now.next
        return res

    def create(self, l):
        if l and isinstance(l, list):
            l = reversed(l)
            node_inner = None
            for v in l:
                node = ListNode(v)
                node.next = node_inner
                node_inner = node
            return node_inner
        return None


if __name__ == '__main__':
    node1 = ListNode(5)
    solution = Solution()
    print(solution.addTwoNumbers(node1, node1))