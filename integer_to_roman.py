# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def inttoroman(n):
    """
    converts integer values to roman values 
    up until the number 3999
    """
    n = str(n)
    ans = ''
    dict = {'01':'M', '02':'', '03':'',
            '11':'C', '12':'D', '13':'M',
            '21':'X', '22':'L', '23':'C',
            '31':'I', '32':'V', '33':'X'}
    while len(n) < 4:
        n = '0' + n
    for i in range(4):
        if n[i] == '0':
            ans += ''
        elif n[i] == '1':
            ans += dict[str(i)+'1']
        elif n[i] == '2':
            ans += 2*dict[str(i)+'1']
        elif n[i] == '3':
            ans += 3*dict[str(i)+'1']
        elif n[i] == '4':
            ans += (dict[str(i)+'1'] + dict[str(i)+'2'])
        elif n[i] == '5':
            ans += dict[str(i)+'2']
        elif n[i] == '6':
            ans += (dict[str(i)+'2'] + dict[str(i)+'1'])
        elif n[i] == '7':
            ans += (dict[str(i)+'2'] + 2*dict[str(i)+'1'])
        elif n[i] == '8':
            ans += (dict[str(i)+'2'] + 3*dict[str(i)+'1'])
        else:
            ans += (dict[str(i)+'1'] + dict[str(i)+'3'])
    return ans