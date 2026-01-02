"""数据拟合"""
import matplotlib.pyplot as plt
import pandas as pd

# 导入数据
data_df = pd.read_csv("数据拟合\金百达银爵DDR43600价格数据集_2022-2025.csv", encoding="utf-8")
print(data_df)

# 绘图
t = data_df["时间量化t"]
price = data_df["价格（元）"]
plt.title("金百达银爵DDR4 3600 8G*2 价格数据_2022-2025")
plt.rcParams['font.sans-serif'] = ['SimHei']  #  在绘图代码前添加字体配置 使用黑体 
plt.scatter(t, price, label="价格变化")
plt.xlabel("时间")
plt.ylabel("价格（元）")
plt.grid(True)
plt.show()

# 数据拟合
# 第一阶段：线性下降(t: 0-39) 
# 选择函数 P(t) = at + b
# 最小二乘法求解参数 a 和 b

def least_squares_linear(t_data, P_data):
    """
    最小二乘法实现线性拟合（解析解，保留所有数据点）
    :return: a, b（最优参数）, SSE, R2
    """
    # 1. 计算基础统计量
    sum_t = sum(t_data)
    sum_P = sum(P_data)
    mean_t = sum_t / len(t_data)
    mean_P = sum_P / len(P_data)
    
    # 2. 计算分子和分母（核心）
    numerator = 0 # 分子 Σ(ti - mean_t) * (Pi - mean_P)
    for i in range(len(t_data)):
        numerator += (t_data[i] - mean_t) * (P_data[i] - mean_P)
    denominator = 0 # 分母 Σ(ti - mean_t)**2
    for i in range(len(t_data)):
        denominator += (t_data[i] - mean_t)**2
    
    # 3. 计算最优参数
    a = numerator / denominator if denominator != 0 else 0.0
    b = mean_P - a * mean_t
    
    # 4. 计算SSE（评估拟合效果）
    SSE = 0
    for i in range(len(t_data)):
        P_predicted = a * t_data[i] + b
        SSE += (P_data[i] - P_predicted)**2

    # 5. 计算R2
    SST = sum((P_data[i] - mean_P)**2 for i in range(len(t_data)))
    R2 = 1 - (SSE / SST) if SST != 0 else 0.0

    return a, b, SSE, R2


# 选择第一阶段数据进行拟合
a, b, SSE, R2 = least_squares_linear(t[:19], price[:19])
print(f"线性拟合结果: P(t) = {a:.2f}t + {b:.2f}, SSE = {SSE:.2f}, R² = {R2:.4f}")
# 绘制拟合结果
plt.plot(t[:19], a * t[:19] + b, label="线性拟合", color='red')
plt.scatter(t, price, label="价格变化")
plt.xlabel("时间")  
plt.ylabel("价格（元）")
plt.grid(True)
plt.show()