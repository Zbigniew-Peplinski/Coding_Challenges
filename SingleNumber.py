# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:40:30 2020

@author: z
"""


def singleNumber(nums):

    """
    finds the singular number in a list, where all others are in even multiples
    """
 
    result = 0
    for number in nums:
        result ^= number
    return result