import operator
import random
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from operator import itemgetter
from TUMU.experiment.experment_3.exper import draw_3D
from TUMU.experiment.experment_3.exper import to_args
from TUMU.experiment.experment_3.exper import draw_3D_union



# 计算欧拉距离
def calcDis(dataSet:[[float,]], centroids:[[float,]], k:int)->[[float,]]:
    """
    :param dataSet: 原始数据
    :param centroids: 质心数据 如: centroids = random.sample(dataSet, k)
    :param k: 用户选定的归类数量
    :return: 每个data对于k各质心的距离度量
    [[float,..k],...len(dataset)]
    """
    clalist = []
    for data in dataSet:
        diff = np.tile(data, (k,1)) - centroids  # 相减   (np.tile(a,(2,1))就是把a先沿x轴复制1倍，即没有复制，仍然是 [0,1,2]。 再把结果沿y方向复制2倍得到array([[0,1,2],[0,1,2]]))
        squaredDiff = diff ** 2  # 平方
        squaredDist = np.sum(squaredDiff, axis=1)  # 和  (axis=1表示行)
        distance = squaredDist ** 0.5  # 开根号
        clalist.append(distance)

    clalist = np.array(clalist)  # 返回一个每个点到质点的距离len(dateSet)*k的数组
    return clalist


# 计算质心
def classify(dataSet:[[float,]], centroids:[[float,]], k:int):
    """
    :param dataSet:
    :param centroids:
    :param k:
    :return: 质点前后位置变化大小,
    """

    # 计算样本到质心的距离
    clalist = calcDis(dataSet, centroids, k)#->[[float,]...]
    # 分组并计算新的质心
    minDistIndices=[min(enumerate(i),key=operator.itemgetter(1))[0] for i in clalist]
    #根据距离量度(数据点到质心的距离),最小量度的归类

    # minDistIndices = np.argmin(clalist, axis=1)  # axis=1 表示求出每行的最小值的下标,表示原始数据接近的中心点(建立树）

    #表示data 靠近的质心点如[1,0,1]
    # newCentroids = pd.DataFrame(dataSet).groupby(
    #     minDistIndices).mean()  # DataFramte(dataSet)对DataSet分组，groupby(min)按照min进行统计分类，mean()对分类结果求均值

    dict={}
    for i,j in enumerate(minDistIndices):
        if dict.get(j):
            dict[j].append(dataSet[i])
        else:
            dict[j]=[dataSet[i]]

    newCentroids = [np.mean(np.array(i), 0) for i in dict.values()]
    newCentroids=[list(i) for i in newCentroids]
    # #表示对树平均->新的质心

    # 计算变化量
    changed = np.array(newCentroids) - np.array(centroids)
    #表示质心偏移状态
    return changed, newCentroids


# 使用k-means分类
def kmeans(dataSet:[float,], k:int):
    # 随机取质心
    centroids = random.sample(dataSet, k)

    # 更新质心 直到变化量全为0
    changed, newCentroids = classify(dataSet, centroids, k)
    while np.any(changed != 0):
        changed, newCentroids = classify(dataSet, newCentroids, k)

    centroids = sorted(newCentroids)  # tolist()将矩阵转换成列表 sorted()排序

    # 根据质心计算每个集群
    cluster = []
    clalist = calcDis(dataSet, centroids, k)  # 调用欧拉距离
    minDistIndices = np.argmin(clalist, axis=1)
    for i in range(k):
        cluster.append([])
    for i, j in enumerate(minDistIndices):  # enymerate()可同时遍历索引和遍历元素
        cluster[j].append(dataSet[i])

    return centroids, cluster


# 创建数据集
# def createDataSet():
#     return [
#             [1, 1], [1, 2], [2, 1],[3,4]
#             ,[2,3],[3,4],[4,6],[6,4],[8,8]
#             ,[4,6],[7,8],[9,9],[10,4],[8,8]
#             ,[6,0],[8,0],[9,0]
#             ]


def K_mean_start(data=[
            [1,1], [1, 2], [2, 1],[3,4],[1,3],[2,5],[5,6],[4,7],[8,8],[9,4],[6,20]
            # ,[2,3],[3,4],[4,6],[6,4],[8,8]
            # ,[4,6],[7,8],[9,9],[10,4],[8,8]
            # ,[6,0],[8,0],[9,0]
            ],k=2,title='K_MEAN聚类',xlabel='x',ylabel='y',model='2'):


    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    # dataset = createDataSet()
    dataset=data
    centroids, cluster = kmeans(dataset,k)
    print('质心为：%s' % centroids)
    print('集群为：%s' % cluster)
    color = ['blue', 'red', 'yellow', 'Lime', 'Cyan', 'purple', 'Gray', 'Olive']

    def diff_model_2(model):

        if model=='2' and len(data[0])==2:
            pass
        else:
            raise Exception("model diffence")

        for i in range(len(dataset)):
            plt.scatter(dataset[i][0], dataset[i][1], marker='o', color='green', s=40, label='原始点')
            #  记号形状       颜色      点的大小      设置标签
            for j in range(len(centroids)):
                plt.scatter(centroids[j][0], centroids[j][1], marker='x', color='red', s=50, label='质心')

        for i in range(k):
            for j in cluster[i]:
                plt.scatter(*j,marker='o',color=color[i],s=40)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def diff_model_3(model):

        #分开的图形
        if model=='3' and len(data[0])==3:
            pass
        else:
            raise  Exception("model diffence")

        #将(x,y,z)...转化为9(x...)(y...)(y...)
        draw_3D(*to_args(centroids))
        # def to_args(centroids: [[int or float]]):
        for i,j in enumerate(cluster):
            draw_3D(*to_args(j),color=color[i])

        draw_3D_union(cluster)



        # draw_3D()
    if model=='2':
        diff_model_2('2')
    if model=='3':
        diff_model_3('3')





K_mean_start(k=2,model='2')

"""

算法思路:
 开始从初始数据中随机k个样本作为初始质心
 loop:
    计算data与质心之间的距离作为度量
    ->一个data对于k个质心的度量->min
    ->将其归类k
    对归类的data求均值->新的质点
    chang(变化差)=上一个支点信息-新的支点信息(不再有太大变化) or looplimit(迭代次数限制）
    退出
    最后的聚类结果


特点:
    对初始值敏感。初始点选择不同可能会产生不同的聚类结果
    最终会收敛。不管初始点如何选择,最终都会收敛
    由于算法开始时为随机选取测试点作为质心进行计算,而对于随机的初始样本有多种情况
    理论上对于一个样本点有n的k树，其结果Cnk,math.factorl(n-k)/math.factorl(k)
    种情况
    
    
"""