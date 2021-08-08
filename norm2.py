# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 21:47:00 2021

@author: Dr.TAOUFIK
"""

import numpy as np

def norm2(v):
    norm=0
    for i in range(len(v)):
        norm+=v[i]**2
    return np.sqrt(norm)
        
""" Test """
a=[1,2,3,4]
z=norm2(a)
print('a=',a)
print('norm2 of a=',z)

c=np.linalg.norm(a,ord=2)
print('c=',c)