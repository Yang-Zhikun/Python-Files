import numpy as np
from scipy.optimize import fsolve
import pandas as pd

# 定义方程
# theta 即 θ
# a 即 α
def equation(theta, y, x, d, a, g, v0):
    return y - (np.tan(theta)*np.sqrt(x*x+d*d+2*np.cos(a)*d)-0.5*g*(x*x+d*d+2*np.cos(a)*d)/(v0*v0*np.cos(theta)**2))

# 初始猜测的 theta 值（以弧度为单位）
initial_guess = np.deg2rad(0)

# 其他参数：
# y 1.83~2.44(m)
# x 1.83~3.66(m)
# d 16.5~32(m)
# a 0~90(度)
# g = 9.8(m/s^2)
# v0 20~30(m/s)
# theta 即 θ
# a 即 α
# 参数范围（示例值，可以根据需要调整）
y_values = [2.44]
x_values = [1.83,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.66]
d_values = [25]
a_values = [60]
v0_values = [25]
g = 9.8

# 用于存储结果的列表
results = []


# 遍历所有可能的参数组合
for y in y_values:
    for x in x_values:
        for d in d_values:
            for a in a_values:
                for v0 in v0_values:
                    # 将角度转换为弧度
                    a_rad = np.deg2rad(a)

                    # 使用 fsolve 求解方程
                    solution = fsolve(equation, initial_guess, args=(y, x, d, a_rad, g, v0))
                    theta_degrees = np.rad2deg(solution[0])

                    # 将结果添加到列表中
                    results.append([y, x, d, a, v0, theta_degrees])

# 将结果转换为 pandas 数据框
df = pd.DataFrame(results, columns=['y', 'x', 'd', 'a(度)', 'v0', 'theta(度)'])

# 将数据框写入 Excel 文件
df.to_excel('数学建模\\近角公式计算结果.xlsx', index=False)

print("结果已保存到'xlsx'文件中。")