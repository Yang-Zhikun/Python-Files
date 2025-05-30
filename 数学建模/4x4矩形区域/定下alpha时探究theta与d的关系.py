from numpy import *
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
# 参数：
W = 7.32
H = 2.44
W0 = 16.5
L0 = 40.32
d = 35
alpha = deg2rad(90)  # 将角度转换为弧度
g = 9.8
v0 = 25
L = 9.15
h1 = 1.8
h2 = 0.4

theta_min = 0.30924550686490665
theta_max = 1.4975091091322803

# 近角公式
def near_corner_equation(theta):
    x2_sq = d ** 2 + (3 * W / 8) ** 2 - 2 * d * (3 * W / 8) * cos(alpha)
    x2 = sqrt(x2_sq)
    term1 = x2 * tan(theta)
    term2 = g * x2_sq * (1 + tan(theta) ** 2) / (2 * v0 ** 2)
    return term1 - term2 - 7 * H / 8

# 远角公式
def far_corner_equation(theta):
    x2_sq = d ** 2 + (3 * W / 8) ** 2 + 2 * d * (3 * W / 8) * cos(alpha)
    x2 = sqrt(x2_sq)
    term1 = x2 * tan(theta)
    term2 = g * x2_sq * (1 + tan(theta) ** 2) / (2 * v0 ** 2)
    return term1 - term2 - 7 * H / 8


# 探究theta与d的关系
# 初始化存储结果的列表
d_values = []
f2_solutions = []
f1_solutions = []

# 改变d值并求解
# d不能小于W0 / sin(alpha)且不能小于25.65，还不能大于35
if (W0 / sin(alpha)) < 25.65:
    start_value = 256
else:
    start_value = 10 * W0 / sin(alpha)

for d in range(int(start_value), 350):  # 从35，以0.1为步长
    d = d / 10.0
    d_values.append(d)
    
    # 求解近角公式
    initial_guess_f1 = [theta_min, theta_max]
    solution_f1 = fsolve(near_corner_equation, initial_guess_f1)
    f1_solutions.append(rad2deg(solution_f1[0]))  # 取第一个解
    # 求解远角公式
    initial_guess_f2 = [theta_min, theta_max]
    solution_f2 = fsolve(far_corner_equation, initial_guess_f2)
    f2_solutions.append(rad2deg(solution_f2[0]))  # 取第一个解
    

# 求极值点的横纵坐标
far_max_y, far_max_x = max(f2_solutions), d_values[f2_solutions.index(max(f2_solutions))]
far_min_y, far_min_x = min(f2_solutions), d_values[f2_solutions.index(min(f2_solutions))]
near_max_y, near_max_x = max(f1_solutions), d_values[f1_solutions.index(max(f1_solutions))]
near_min_y, near_min_x = min(f1_solutions), d_values[f1_solutions.index(min(f1_solutions))]

# 绘制theta值与d的关系
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.figure(figsize=(10, 6))
plt.plot(d_values, f2_solutions, label='远角公式')
plt.plot(d_values, f1_solutions, label='近角公式')

# 绘制极值点并标注坐标
plt.scatter(far_max_x, far_max_y, color='red', label='远角公式最大值')
plt.text(far_max_x, far_max_y, f'({far_max_x}, {far_max_y})', ha='right')
plt.scatter(far_min_x, far_min_y, color='green', label='远角公式最小值')
plt.text(far_min_x, far_min_y, f'({far_min_x}, {far_min_y})')
plt.scatter(near_max_x, near_max_y, color='blue', label='近角公式最大值')
plt.text(near_max_x, near_max_y, f'({near_max_x}, {near_max_y})', ha='right')
plt.scatter(near_min_x, near_min_y, color='purple', label='近角公式最小值')
plt.text(near_min_x, near_min_y, f'({near_min_x}, {near_min_y}')

plt.xlabel('d值 (米)')
plt.ylabel('theta值 (度)')
plt.title(f'theta值与d的关系(alpha={rad2deg(alpha)}度)')
plt.legend()
plt.grid(True)
plt.show()