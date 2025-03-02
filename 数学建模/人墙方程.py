from numpy import tan,cos,sin,pi,sqrt, deg2rad, rad2deg
from scipy.optimize import fsolve
import pandas as pd

#定义方程
# D = 9.15
# h1 = 1.8
# h2 = 0.4
# v0 = 25
# g = 9.8
def equation(theta, D, h1, h2, v0, g):
    return (D*tan(theta)) - (g*D*D*(tan(theta)*tan(theta) + 1) / (2*v0*v0)) - (h1+h2)

# 求解方程，初始值为0
initial_guess = deg2rad(89)

# 其他参数：
D = 9.15
h1 = 1.8
h2 = 0.4
v0 = 25
g = 9.8

solution = fsolve(equation, initial_guess, args=(D, h1, h2, v0, g))
theta_degrees1 = rad2deg(solution[0])
print("solution:", solution)
print("theta值(角度):", theta_degrees1)
print("tan(theta):", tan(solution[0]))
