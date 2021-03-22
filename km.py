# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 10:08
# @Author  : Zy
# @File    : km.py
# @Software: PyCharm

import numpy as np
from sklearn.utils.linear_assignment_ import linear_assignment

from scipy.optimize import linear_sum_assignment
cost_matrix = np.array([[15, 40, 45],
						 [20, 60, 35],
						 [40, 40, 25]])

print(cost_matrix.min(axis=1))
print(cost_matrix.min(axis=1)[:, np.newaxis])
cost_matrix -= cost_matrix.min(axis=1)[:, np.newaxis]
print(np.argmax(cost_matrix[2] == 0))
print(cost_matrix)
