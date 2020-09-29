# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:56:11 2020

@author: z
"""


def happynum(n):

    """
    checks whether an integer is a happy numer
    
    A happy number is a number defined by the following process: 
    Starting with any positive integer, replace the number by the 
    sum of the squares of its digits, and repeat the process 
    until the number equals 1 (where it will stay), or 
    it loops endlessly in a cycle which does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers.
    """

    a = str(n)
    i = 0
    while i < 20:
        ans = 0
        for j in range(len(a)):
            ans += int(a[j])**2
        a = str(ans)
        i += 1
    if a[-1] == '1':
        ans = True
    else:
        ans = False
    return ans
            