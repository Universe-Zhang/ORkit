# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 15:46
# @Author  : Zy
# @File    : M_618search.py
# @Software: PyCharm

import math

def f(x):
    return 2*x*x-x-1

def Fibonacci_list_generation(nterms):
    n1 = 1
    n2 = 1
    count = 2
    F_list = [n1]
    if nterms <= 0:
        print("请输入一个正整数。")
    elif nterms == 1:
        return F_list
    else:
        F_list.append(n2)
        while count <= nterms:
            nth = n1 + n2
            F_list.append(nth)
            # 更新值
            n1 = n2
            n2 = nth
            count += 1# 第一和第二项
        return F_list


def M_Fibonacci(F,LB,UB,L,d='max',path=[],sigma=0.001):
    """
    :param F: 目标函数
    :param LB:定义域下界
    :param UB:定义域上界
    :param L:要求精度
    :param d:优化方向最大化或者最小化，可选参数{'max'，'min'}默认'max'
    :param path:搜索过程中的点，只返回x值
    :param sigma:辨别参数
    :return:下界x值，下界x对应的函数值，及搜索路径
    """
    Fn = math.ceil((UB-LB)/L)
    F_list = Fibonacci_list_generation(Fn)
    print(F_list)
    F_list.reverse()
    x1 = LB + F_list[ 2] / F_list[0] * (UB - LB)
    x2 = LB + F_list[ 1] / F_list[0] * (UB - LB)
    path.append(x1)
    path.append(x2)
    y1 = F(x1)
    y2 = F(x2)
    for k in range(1,Fn-2,1):
        if y2>=y1 and d=='max' or y2<=y1 and d=='min':
            UB = x2
            x2 = LB + F_list[k + 2] / F_list[k] * (UB - LB)
            y2 = F(x2)
            path.append(x2)
        else:
            LB=x1
            x1 = LB + F_list[k + 1] / F_list[k] * (UB - LB)
            y1 = F(x1)
            path.append(x1)
    x2 = x1+sigma
    y2 = f(x2)
    if y2 >= y1 and d == 'max' or y2 <= y1 and d == 'min':
        UB=x2
        path.append(x2)
    else:
        LB=x1
        path.append(x1)
    xx=(UB+LB)/2
    path.append(xx)
    return xx,f(xx),path




if __name__ == '__main__':
    a,b,c = M_Fibonacci(f,-1,1,0.16,d='min')
    print(a,b)
    print(c)

    import matplotlib.pyplot as plt
    import numpy as np

    px = np.arange(-1,1,0.01)
    py = f(px)
    plt.plot(px,py)
    si=100
    for pi in c:
        plt.scatter(pi,f(pi),s=si,c='black')
        si-=20
    plt.show()

