import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文支持
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号问题

# 数据
time = [0, 660, 840, 1680, 2160, 2560]
intensity = [0, 470, 595, 535, 285, 0]

# 使用 numpy.polyfit 进行二次曲线拟合
coefficients = np.polyfit(time, intensity, 2)  # 2表示二次拟合

# 创建二次多项式的拟合函数
polynomial = np.poly1d(coefficients)

# 创建时间点以便绘制平滑的拟合曲线
time_fine = np.linspace(min(time), max(time), 500)

# 计算拟合曲线的光强值
intensity_fine = polynomial(time_fine)

# 绘制原始数据点
plt.scatter(time, intensity, color='black', s=10 , zorder=1)

# 绘制拟合后的二次曲线
help(plt.plot)
plt.plot(time_fine, intensity_fine,linestyle='--', color='black', linewidth=1)

# 设置图形标题和轴标签
plt.title('增益曲线')
plt.xlabel('时间 (μs)')
plt.ylabel('光增益系数 ')

# 显示网格
plt.grid(True)

# 显示图例
plt.legend()

# 显示图形
plt.show()
