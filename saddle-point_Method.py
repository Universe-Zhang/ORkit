# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 19:17
# @Author  : Zy
# @File    : saddle-point_Method.py
# @Software: PyCharm
import numpy as np
def f(x):
    x = np.array(x)
    y=np.square((x-1)).sum()
    return y
def f_(x):
    x = np.array(x)
    y_=2*(x-1)
    return y_


def M_saddle_point(f,f_,Epsilon=0.1):
    pass

