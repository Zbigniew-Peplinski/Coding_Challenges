# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:06:00 2020

@author: z
"""


def romantoint(s):
     
    """
    converts roman value to integers
    """

    dict = {"M" : 1000, "D" : 500, "C" : 100, "L":50, "X":10, "V":5, "I":1}
    s += 'I'
    ans = 0
    i = 1

    while i < len(s):
        if dict[s[-(i+1)]] < dict[s[-i]]:
            ans -= dict[s[-(i+1)]]
        else:
            ans += dict[s[-(i+1)]]
        i += 1
    return ans