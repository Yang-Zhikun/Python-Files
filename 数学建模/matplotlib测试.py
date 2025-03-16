import matplotlib.pyplot as plt
import numpy as np
# 绘制正弦函数
x = np.arange(- 2*np.pi , 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['sin', 'cos'])
plt.show()
