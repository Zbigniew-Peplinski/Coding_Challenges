# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:14:08 2020

@author: z
"""


def majorityElement(nums):
 
    """
    calculates the element that occurs the most often
    in the list nums
    """

    nums.sort()
    i = 0
    ans = [0,0]
    while i < len(nums):
        a = nums.count(nums[i])
        if a > ans[1]:
            ans[0] = nums[i]
            ans[1] = a
            i += a
        else:
            i += a
    return ans[0]