from numpy import *
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# 共享常量参数
d = 27.5
W = 7.32
H = 2.44
alpha = deg2rad(60)  # 将角度转换为弧度
g = 9.8
v0 = 25
L = 9.15
h1 = 1.8
h2 = 0.4

# 人墙方程
def f(theta):
    return (L*tan(theta)) - (g*L*L*(tan(theta)*tan(theta) + 1) / (2*v0*v0)) - h1-h2

# 远角公式
def f2(theta):
    part1 = (tan(theta) * sqrt(4 * d ** 2 + W ** 2 + 4 * d * W * cos(alpha))) / 2
    part2 = (g * (4 * d ** 2 + W ** 2 + 4 * d * W * cos(alpha)) * (1 + tan(theta) ** 2)) / (8 * v0 ** 2)
    return H - part1 + part2

# 近角公式
def f1(theta):
    part1 = (tan(theta) * sqrt(4 * d ** 2 + W ** 2 - 4 * d * W * cos(alpha))) / 2
    part2 = (g * (4 * d ** 2 + W ** 2 - 4 * d * W * cos(alpha)) * (1 + tan(theta) ** 2)) / (8 * v0 ** 2)
    return H - part1 + part2


# 求解人墙方程
initial_guess_f = [deg2rad(0), deg2rad(89)]
solution_f = fsolve(f, initial_guess_f)
print("人墙方程 solution:", solution_f)
print(f"人墙方程 theta值(弧度):{solution_f}, (角度):{rad2deg(solution_f)}")

# 求解远角公式
initial_guess_f2 = solution_f
solution_f2 = fsolve(f2, initial_guess_f2)
print("远角公式 solution:", solution_f2)
print(f"远角公式 theta(弧度):{solution_f2}, (角度):{rad2deg(solution_f2)}")

# 求解近角公式
initial_guess_f1 = solution_f
solution_f1 = fsolve(f1, initial_guess_f1)
print("近角公式 solution:", solution_f1)
print(f"近角公式 theta(弧度):{solution_f1}, (角度):{rad2deg(solution_f1)}")

# # 探究theta与d的关系
# # 初始化存储结果的列表
# d_values = []
# f2_solutions = []
# f1_solutions = []

# # 改变d值并求解
# for d in range(168, 320):  # 从16.8到32，以0.1为步长
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
# plt.title('theta值与d的关系')
# plt.legend()
# plt.grid(True)
# plt.show()

# 探究theta与alpha的关系
# 初始化存储结果的列表
alpha_values = []
f2_solutions = []
f1_solutions = []

# 改变alpha值并求解
for alpha in range(0, 91):  # 从0到90，以1为步长
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
