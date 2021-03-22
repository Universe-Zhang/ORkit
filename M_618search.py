# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 15:46
# @Author  : Zy
# @File    : M_618search.py
# @Software: PyCharm

def f(x):
    return 2*x*x-x-1

def M_618(F,LB,UB,L,d='max',path=[]):
    """
        :param F: 目标函数
        :param LB:定义域下界
        :param UB:定义域上界
        :param L:要求精度
        :param d:优化方向最大化或者最小化，可选参数{'max'，'min'}默认'max'
        :param path:搜索过程中的点，只返回x值
        :return:下界x值，下界x对应的函数值，及搜索路径
        """
    if UB-LB<=L:
        return LB,F(LB),path
    else:
        x1 = LB+0.382*(UB-LB)
        x2 = LB+0.618*(UB-LB)
        y1 = F(x1)
        y2 = F(x2)
        if y2>=y1 and d=='max' or y2<=y1 and d=='min':
            path.append(x1)
            return M_618(F, x1, UB, L, d, path)
        else:
            path.append(x2)
            return M_618(F, LB, x2, L, d, path)

if __name__ == '__main__':
    a,b,c = M_618(f,-1,1,0.16,d='min')
    print(a,b)
    print(c)

    import matplotlib.pyplot as plt
    import numpy as np

    px = np.arange(-1,1,0.01)
    py = f(px)
    plt.plot(px,py)
    si=24
    for pi in c:
        plt.scatter(pi,f(pi),s=si,c='black')
        si-=3
    plt.show()


