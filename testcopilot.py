#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Stanl
# @Time     : 2023/2/24 16:36
# @File     : testcopilot.py
# @Project  : gitskills

# write a function to compute the probability of at least 2 students having the same birthday in a class of k students
# the probability is 1 - (365*364*...*(365-k+1)/365^k)
# write a python function to compute the probability of at least 2 students having the same birthday in a class of k students

# 写一个程序展示numba对python的加速效果

import numpy as np
import time
import numba
from numba import jit

@jit(nopython=True)
def compute_pi(n):
    count = 0
    for i in range(n):
        x = np.random.random()
        y = np.random.random()
        if x**2 + y**2 < 1:
            count += 1
    return 4*count/n

if __name__ == '__main__':
    start = time.time()
    print(compute_pi(10000000))
    end = time.time()
    print(end-start)
