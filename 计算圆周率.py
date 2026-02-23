from math import *
r = 1 # 圆的半径，单位圆

# 初始条件
a_n = 1 # 初始正六边形的边长AB为1
n = 6 # 初始n边形的边数

while n <= 1e150: # n边形的边数
    # 计算当前n边形的圆周率
    pi = a_n * n / (2 * r)
    print(f"正{n}边形: 圆周率 = {pi:.48f}")

    # 计算下一个2n边形的边长
    OD = sqrt(r ** 2 - (a_n ** 2 / 4))
    CD = r - OD
    a_2n = sqrt((a_n ** 2 / 4) + CD ** 2) # 计算2n边形的边长(递推)
    # 更新
    a_n = a_2n
    n = n * 2