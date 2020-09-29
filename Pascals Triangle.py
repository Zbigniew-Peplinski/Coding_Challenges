# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:05:42 2020

@author: z
"""


def generate(num):

    """
    Generates the indicies of the pascals triangle at level = num
    """

    ans = []
    if num == 0:
        ans = ans
    elif num == 1:
        ans.append([1])
    elif num == 2:
        ans.append([1])
        ans.append([1,1])
    else:
        ans.append([1])
        ans.append([1,1])
        for i in range(num - 2):
            b = []
            b.append(1)
            for j in range(len(ans[-1]) - 1):
                b.append(ans[-1][j] + ans[-1][j+1])
            b.append(1)
            ans.append(b)
    return ans