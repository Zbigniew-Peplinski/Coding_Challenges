# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:41:13 2020

@author: z
"""
from random import randint

def selecta(buys, receives, n):
    """
    selects two people untill hey aren't the same
    
    """
    
    def rand(buys, receives, n):
        """
        randomly selects two people
        """
        b = randint(0, n - 1)
        r = randint(0, n - 1)
        return buys[b], receives[r]
    
    b, r = rand(buys, receives, n)
    while b == r:
        b, r = rand(buys, receives, n)
    return b, r

def secret_santa(List):
    """
    creates a dictionary, allocating everybody a random person from the list
    """
    def secret_santa_prev(List):
        dict = {}
        #splits list in two categories
        buys = List[:]
        receives = List[:]
    
        #goes through list until last pair
        n = len(buys)
        while n > 1:
            b, r = selecta(buys, receives, n)
            buys.remove(b)
            receives.remove(r)
            dict[b] = r
            n -= 1
        b = buys[0]
        r = receives[0]
        dict[b] = r
        return dict, b

    #ensure that final pair is not the same person
    d, b = secret_santa_prev(List)
    while d[b] == b:
        d, b = secret_santa_prev(List)
    return d



            
            
            