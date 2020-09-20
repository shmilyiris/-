import random
from creature import Creature


def f(x):
    """目标函数y=-4x^2+16"""
    return 16 - 4 * x * x


def live_rate(y):
    """存活率公式，存活率即是适应度，存活率越高，适应分越高"""
    # y越大，存活率越高
    return (1 / 256) * y * y


def init_encoding(size, gene_length):
    """种群初始化过程，采取二进制编码的方法，返回所有生物的编码集合"""
    race = []
    for i in range(size):
        temp = []
        for j in range(gene_length):
            temp.append(random.randint(0, 1))
        creature = Creature(temp)  # 新建一个生物
        race.append(creature)  # 将该生物加入种群列表中

    return race


def decoding(gene, gene_length):
    """基因解码过程，返回该个体的表现型（所处海拔高度）"""
    # 当改变函数时，相应的参数都应随之改变
    return -2 + 4 * int(gene, 2) / (2 ** gene_length - 1)


def cal_fit(races, gene_length):
    """计算出一个种群对应的适应值二维列表"""
    fit_value = []
    for i in range(len(races)):
        s = ''.join(list(map(lambda x: str(x), races[i].gene)))  # 将基因序列转换为字符串
        fit_value.append(f(decoding(s, gene_length)))  # 求出对应的适应值
    return fit_value


def selection_prepare(fit_value):
    """较优种群的选择，进行轮盘赌算法的准备"""
    # 先计算选择概率，再计算叠加的选择概率，加入表中
    sele_per = []  # 叠加选择概率表
    total = sum(fit_value)  # 适应值总和
    temp_sum = 0
    for every_fit in fit_value:
        temp = every_fit / total
        temp_sum += temp
        sele_per.append(temp_sum)
    return sele_per  # 得到选择叠加列表


def selection(sele_per, target_num, old_race):
    """进行轮盘赌算法"""
    number = 0  # 新种群数量，逐渐逼近目标数量target_num
    new_race = []
    while number < target_num:  # 当数量还未达到目标数量时
        choice = random.random()  # 选取一个随机数
        for sele in sele_per:  # 对叠加选择概率表中的每一个元素遍历
            if choice <= sele:  # 如果轮盘抽到的随机数不大于该元素
                new_race.append(old_race[sele_per.index(sele) - 1])  # 将该基因段加入新种群中
                break
        number += 1
    return new_race


def add_left_creatures(new_race, old_race, fit_array, old_scale):
    """添加剩下的较优老种群"""
    index_sq = sorted(range(len(fit_array)), key=lambda k: fit_array[k])  # 先得到适应度从低到高排列的索引序列
    for i in range(1, old_scale + 1):
        new_race.append(old_race[index_sq[-i]])  # 再根据序列依次将该老生物种群加入新种群中，完成最后的新种群的更新
