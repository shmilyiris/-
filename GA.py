from Function import *
import processing
import matplotlib.pyplot as plt

size = 100  # 种群规模，保持100个
gene_length = 10  # 基因段长度为n，有2^n个表现型
new_scale = 0.1  # 新生种群规模/种群规模
old_scale = 1 - new_scale  # 老一代优秀种群加入新种群规模/种群规模
n = 12  # 共执行n代种群
mutation_percentage = 0.1  # 突变概率

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


fig = plt.figure()

creatures = init_encoding(size, gene_length)  # 初始化得到第一族种群

for i in range(n):
    print("执行第{}次循环\n".format(i + 1))
    fit_array = cal_fit(creatures, gene_length)  # 得到种族的适应度列表
    sele_array = selection_prepare(fit_array)  # 根据适应度列表进行选择子准备
    new_creatures = selection(sele_array, new_scale * size, creatures)  # 轮盘赌进行新种群的筛选
    for j in range(0, int(new_scale * size), 2):
        new_creatures[j].crossover(new_creatures[j + 1].gene)  # 在新种群中进行基因交叉
    for k in range(0, int(new_scale * size)):
        new_creatures[k].mutation(mutation_percentage)  # 每个新品种都有一定概率变异
    add_left_creatures(new_creatures, creatures, fit_array, int(old_scale * size))  # 补充剩余的老种群
    if i == 0:
        plt.ion()
        av_living_rate = []  # 平均幸存率初始化
    if i != 0:
        plt.clf()  # 画布清除
    processing.draw_result(new_creatures, i, n, fig, av_living_rate, size)  # 动态画图
    creatures = new_creatures  # 更新种群

plt.ioff()
plt.show()
