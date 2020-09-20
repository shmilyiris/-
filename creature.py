import Function
import random


class Creature:
    """表示放在山（函数图像）上的生物"""

    def __init__(self, gene):
        self.gene = gene  # 基因编码
        self.gene_length = len(gene)  # 编码长度

    def where(self):
        """通过基因编码进行解码以及函数图像进行定位，返回其xy坐标"""
        s = ''.join(list(map(lambda x: str(x), self.gene)))  # 将基因序列转换为字符串
        x = Function.decoding(s, self.gene_length)
        return x, Function.f(x)

    def if_live(self):
        """返回该生物是否存活"""
        x, y = self.where()
        liv_rate = Function.live_rate(y)
        if random.random() < liv_rate:
            return True
        else:
            return False

    def crossover(self, another_gene):
        """将该生物与另一个进行基因交叉，形成新的物种"""
        index1 = random.randint(0, 9)  # 随机生成交叉片段的第一个索引
        index2 = random.randint(index1, 9)  # 第二个索引
        temp = self.gene[index1:index2]
        self.gene[index1:index2] = another_gene[index1:index2]
        another_gene[index1:index2] = temp

    def mutation(self, probability):
        """生物有一定概率产生变异"""
        if random.random() < probability:
            index = random.randint(0, self.gene_length - 1)  # 变异的基因位置
            if self.gene[index] == 1:
                self.gene[index] = 0
            else:
                self.gene[index] = 1
