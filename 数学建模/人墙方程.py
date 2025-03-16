from numpy import *
from scipy.optimize import fsolve
# 参数：
L = 9.15
h1 = 1.8
h2 = 0.4
v0 = 25
g = 9.8
# 定义方程
def f(theta):
    return (L*tan(theta)) - (g*L*L*(tan(theta)*tan(theta) + 1) / (2*v0*v0)) - h1-h2
# 求解方程初始猜测值
initial_guess = [deg2rad(0), deg2rad(89)]
# 调用fsolve函数求解方程
solution = fsolve(f, initial_guess)
print("solution:", solution)
print(f"theta值1(弧度):{solution[0]}, (角度):{rad2deg(solution[0])}")
print(f"theta值2(弧度):{solution[1]}, (角度):{rad2deg(solution[1])}")