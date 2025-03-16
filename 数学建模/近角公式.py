from numpy import *
from scipy.optimize import fsolve
# 定义常量
d = 25
W = 7.32
H = 2.44
alpha = deg2rad(60)  # 将角度转换为弧度
g = 9.8
v0 = 25
# 定义方程
def f1(theta):
    part1 = (tan(theta) * sqrt(4 * d ** 2 + W ** 2 - 4 * d * W * cos(alpha))) / 2
    part2 = (g * (4 * d ** 2 + W ** 2 - 4 * d * W * cos(alpha)) * (1 + tan(theta) ** 2)) / (8 * v0 ** 2)
    return H - part1 + part2
# 初始猜测值
initial_guess = [0.30924550686490665, 1.4975091091322803]
solution = fsolve(f1, initial_guess)
print("solution:", solution)
print(f"theta(弧度):{solution}, (角度):{rad2deg(solution)}")