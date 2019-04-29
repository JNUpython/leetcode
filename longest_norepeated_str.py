# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 23:19
# @Author  : kean
# @Email   : ?
# @File    : longest_norepeated_str.py
# @Software: PyCharm

""""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        component = {v for v in s}
        s = [i for i in s]
        num = len(component)
        # print(component)
        res_map = dict()
        res_list = list()
        res_set = set()
        res = 0
        for i in range(len(s)):
            # print(res_list, res_set, i)
            v = s[i]
            if v not in res_set:
                res_set.add(v)
                res_list.append(v)
                tmp = len(res_list)
                if tmp > res:
                    res = tmp
            else:
                # print(res_map[v])
                tmp = len(res_list)
                if tmp > res:
                    res = tmp
                res_list = s[res_map[v]+1:i+1]
                # print(res_list)
                res_set = set(res_list)
            if len(res_list) == num:
                return num
            res_map[v] = i
        return res


if __name__ == '__main__':
    string = "dvdf"
    string = "bbtablud"
    string = "ohvhjdml"
    string = "nfpdmpi"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(string))
