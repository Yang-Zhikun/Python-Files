from numpy import *
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
# 参数：
W = 7.32
H = 2.44
W0 = 16.5
L0 = 40.32
d = 26
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


# 探究theta与alpha的关系
# 初始化存储结果的列表
alpha_values = []
f2_solutions = []
f1_solutions = []

########################### sin(alpha) >= W0 / d
# 求解alpha的下限
def f3_alpha(alpha):
    return sin(alpha) - W0 / d
initial_guess_alpha = deg2rad(40)  # 初始猜测值，弧度
alpha_min = fsolve(f3_alpha, initial_guess_alpha)[0]
# 限制alpha_min不小于39.29869155°
if alpha_min < deg2rad(39.29869155):
    alpha_min = deg2rad(39.29869155)
print(f"alpha_min(弧度):{alpha_min}, (角度):{rad2deg(alpha_min)}")

# 改变alpha值并求解
for alpha in range(int(rad2deg(alpha_min)), 91):  # 从0到90，以1为步长
    alpha = deg2rad(alpha)
    alpha_values.append(rad2deg(alpha))  # 将弧度转换为角度

    # 求解远角公式
    initial_guess_f2 = [theta_min, theta_max]
    solution_f2 = fsolve(far_corner_equation, initial_guess_f2)
    f2_solutions.append(rad2deg(solution_f2[0]))  # 已经是角度转换，无需修改
    # 求解近角公式
    initial_guess_f1 = [theta_min, theta_max]
    solution_f1 = fsolve(near_corner_equation, initial_guess_f1)
    f1_solutions.append(rad2deg(solution_f1[0]))  # 已经是角度转换，无需修改

# 求出极值点的横纵坐标
far_max_y, far_max_x = max(f2_solutions), alpha_values[f2_solutions.index(max(f2_solutions))]
far_min_y, far_min_x = min(f2_solutions), alpha_values[f2_solutions.index(min(f2_solutions))]
near_max_y, near_max_x = max(f1_solutions), alpha_values[f1_solutions.index(max(f1_solutions))]
near_min_y, near_min_x = min(f1_solutions), alpha_values[f1_solutions.index(min(f1_solutions))]

# 绘制theta值与alpha的关系
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.figure(figsize=(10, 6))
plt.plot(alpha_values, f2_solutions, label='远角公式')
plt.plot(alpha_values, f1_solutions, label='近角公式')
# 标出极值点并标注坐标
plt.scatter(far_max_x, far_max_y, color='red', label='远角公式最大值')
plt.text(far_max_x, far_max_y, f'({far_max_x}, {far_max_y})')
plt.scatter(far_min_x, far_min_y, color='green', label='远角公式最小值')
plt.text(far_min_x, far_min_y, f'({far_min_x}, {far_min_y})', ha='right')
plt.scatter(near_max_x, near_max_y, color='blue', label='近角公式最大值')
plt.text(near_max_x, near_max_y, f'({near_max_x}, {near_max_y})', ha='right')
plt.scatter(near_min_x, near_min_y, color='purple', label='近角公式最小值')
plt.text(near_min_x, near_min_y, f'({near_min_x}, {near_min_y}')
plt.xlabel('alpha值 (度)')
plt.ylabel('theta值 (度)')
plt.title(f'theta值与alpha的关系(d={d})')
plt.legend()
plt.grid(True)
plt.show()
