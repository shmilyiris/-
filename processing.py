import matplotlib.pyplot as plt
import numpy as np
from Function import *


# 处理数据

def draw_result(creatures, i, n, fig, survive_rate, size):
    """画图"""
    # 图1 散点+函数图
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title('generation number {}'.format(i + 1))
    ax1.set_xlabel('x')
    ax1.set_ylabel('height')
    x0 = np.linspace(-2, 2, 100)
    y0 = f(x0)
    ax1.plot(x0, y0)  # 画出函数图像(山)

    # 图2 平均存活率-n代图
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title('每代平均存活率')

    survive_num = 0  # 幸存生物初始化
    for creature in creatures:
        x, y = creature.where()
        if creature.if_live():
            ax1.scatter(x, y, c='g', marker='o', s=15)
            survive_num += 1
        else:
            ax1.scatter(x, y, c='r', marker='o', s=15)
    survive_rate.append(survive_num / size)

    if i == n - 1:
        ax2.plot([j for j in range(1, n + 1)], survive_rate, color='g')

    plt.pause(0.2)  # 设置停止时间以达到动态效果
