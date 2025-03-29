from numpy import *
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
# 参数：
W = 7.32
H = 2.44
W0 = 16.5
L0 = 40.32
d = 23
alpha = deg2rad(40)  # 将角度转换为弧度
g = 9.8
v0 = 25
L = 9.15
h1 = 1.8
h2 = 0.4

theta_min = 0.30924550686490665
theta_max = 1.4975091091322803

# 近角公式
def f1(theta):
    part1 = (tan(theta) * sqrt(4 * d ** 2 + W ** 2 - 4 * d * W * cos(alpha))) / 2
    part2 = (g * (4 * d ** 2 + W ** 2 - 4 * d * W * cos(alpha)) * (1 + tan(theta) ** 2)) / (8 * v0 ** 2)
    return H - part1 + part2

# 远角公式
def f2(theta):
    part1 = (tan(theta) * sqrt(4 * d ** 2 + W ** 2 + 4 * d * W * cos(alpha))) / 2
    part2 = (g * (4 * d ** 2 + W ** 2 + 4 * d * W * cos(alpha)) * (1 + tan(theta) ** 2)) / (8 * v0 ** 2)
    return H - part1 + part2


# 求解远角公式
initial_guess_f2 = [theta_min, theta_max]
solution_f2 = fsolve(f2, initial_guess_f2)
print("远角公式 solution:", solution_f2)
print(f"远角公式 theta(弧度):{solution_f2}, (角度):{rad2deg(solution_f2)}")

# 求解近角公式
initial_guess_f1 = [theta_min, theta_max]
solution_f1 = fsolve(f1, initial_guess_f1)
print("近角公式 solution:", solution_f1)
print(f"近角公式 theta(弧度):{solution_f1}, (角度):{rad2deg(solution_f1)}")

# # 探究theta与d的关系
# # 初始化存储结果的列表
# d_values = []
# f2_solutions = []
# f1_solutions = []

# # 改变d值并求解
# start_value = int(10 * W0 / sin(alpha))
# for d in range(start_value, 350):  # 从35，以0.1为步长
#     d = d / 10.0
#     d_values.append(d)
    
#     # 求解远角公式
#     solution_f2 = fsolve(f2, initial_guess_f2)
#     f2_solutions.append(rad2deg(solution_f2[0]))  # 取第一个解
    
#     # 求解近角公式
#     solution_f1 = fsolve(f1, initial_guess_f1)
#     f1_solutions.append(rad2deg(solution_f1[0]))  # 取第一个解

# # 在绘图代码前添加字体配置
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# # 绘制图像
# plt.figure(figsize=(10, 6))
# plt.plot(d_values, f2_solutions, label='远角公式')
# plt.plot(d_values, f1_solutions, label='近角公式')
# plt.xlabel('d值 (米)')
# plt.ylabel('theta值 (度)')
# plt.title(f'theta值与d的关系(alpha={rad2deg(alpha)}度)')
# plt.legend()
# plt.grid(True)
# plt.show()



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
print(f"alpha_min(弧度):{alpha_min}, (角度):{rad2deg(alpha_min)}")

# 改变alpha值并求解
for alpha in range(int(rad2deg(alpha_min)), 91):  # 从0到90，以1为步长
    alpha = deg2rad(alpha)
    alpha_values.append(rad2deg(alpha))  # 将弧度转换为角度
    # 求解远角公式
    solution_f2 = fsolve(f2, initial_guess_f2)
    f2_solutions.append(rad2deg(solution_f2[0]))  # 已经是角度转换，无需修改

    # 求解近角公式
    solution_f1 = fsolve(f1, initial_guess_f1)
    f1_solutions.append(rad2deg(solution_f1[0]))  # 已经是角度转换，无需修改

# 在绘图代码前添加字体配置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 绘制图像
plt.figure(figsize=(10, 6))
plt.plot(alpha_values, f2_solutions, label='远角公式')
plt.plot(alpha_values, f1_solutions, label='近角公式')
plt.xlabel('alpha值 (度)')  # 修改为度
plt.ylabel('theta值 (度)')  # 已经是度，无需修改
plt.title(f'theta值与alpha的关系(d={d})')
plt.legend()
plt.grid(True)
plt.show()
