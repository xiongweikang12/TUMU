import copy

import matplotlib.pyplot as plt
import matplotlib
import math
from itertools import chain
import numpy as np
from TUMU.experiment.experment_1.pie_search import draw_pie
from TUMU.experiment.experment_1.exper1 import key_value
from TUMU.experiment.experment_1.exper1 import draw_hitt
from mpl_toolkits.mplot3d import Axes3D
import os
from collections.abc import Iterable
import pandas as pd


#TODO 聚类行为归类

def isequal_lenght(*args:([...])):
    #判断长度是否相同
    """
    :param args: 传入多个可迭代对象,并且类型长度相等[[...]...]
    :return: flag:bool 长度相同True,不同False,当不为Iterable时抛出异常
    """
    is_true_args=args[0]
    is_true=True
    if isinstance(is_true_args,Iterable):
        for i in args:
            if len(i)==len(is_true_args):
                continue
            else:
                is_true=False
                break

        return is_true
    else:
        raise Exception("Type ERROR")

def draw_3D(list1:[float],list2:[float],list3:[float],color='red'):

    #绘制单个图形,[(x...),(y...),(z...)]
    if isequal_lenght(list1, list2, list3):
        a = np.array([list1, list2, list3])
        fig=plt.figure()
        ax1 = Axes3D(fig, auto_add_to_figure=False)
        fig.add_axes(ax1)
        ax1.scatter(list1, list2, list3, c=color)
        ax1.view_init(30, -45)
        plt.show()

    else:
        raise Exception("Input ERROR")


#创建k_mean函数

def k_mean(b,c,d):
    #储存新的簇中的所有点
    list1 = []
    list2 = []
    list3 = []
    #储存新的簇中心点
    gap1 = b
    gap2 = c
    gap3 = d
    #生成空矩阵用于存储各簇的数据
    b = np.zeros(0)
    c = np.zeros(0)
    d = np.zeros(0)
    #计算所有值到新的簇中心点的距离
    for i in range(0,len(a)):
        dis1=np.linalg.norm(a[i:i+1]-gap1)
        dis2=np.linalg.norm(a[i:i+1]-gap2)
        dis3=np.linalg.norm(a[i:i+1]-gap3)
        # 根据每个点与各个簇中心的距离将每个对象重新赋给最近的簇
        if min(dis1, dis2, dis3) == dis1:
            list1.append(i)
            b = np.append(b, a[i:i + 1])
            x = int(len(b) / 4)
            b = np.reshape(b, newshape=(x,4))
        if min(dis1, dis2, dis3) == dis2:
            list2.append(i)
            c = np.append(c, a[i:i + 1])
            x = int(len(c) / 4)
            c = np.reshape(c, newshape=(x,4))
        if min(dis1, dis2, dis3) == dis3:
            list3.append(i)
            d = np.append(d, a[i:i + 1])
            x = int(len(d) / 4)
            d = np.reshape(d, newshape=(x,4))
    #将新生成的簇的所有值转化为多维向量
    line1= pd.DataFrame(b)
    line2=pd.DataFrame(c)
    line3=pd.DataFrame(d)
    #对新生成的簇的所有值求平均值来获得新的簇中心点
    b=np.mean(b,axis=0)
    c=np.mean(c,axis=0)
    d=np.mean(d,axis=0)
    #当簇的中心点不再发生明显的变化时停止递归
    if abs(sum(b - gap1))+abs(sum(c - gap2))+abs(sum(d - gap3))<10**(-64):


        x1 = line1[0]
        y1 = line1[2]
        z1 = line1[3]
        x2 = line2[0]
        y2 = line2[2]
        z2 = line2[3]
        x3 = line3[0]
        y3 = line3[2]
        z3 = line3[3]
        #创建绘制三维图的环境
        fig=plt.figure()
        ax = Axes3D(fig,auto_add_to_figure=False)
        fig.add_axes(ax)
        # 绘制散点图
        ax.scatter(x1, y1, z1,cmap='Blues',label='Setosa')
        ax.scatter(x2, y2, z2,c='g',label='Versicolor',marker='D')
        ax.scatter(x3, y3, z3,c='r',label='Virginica')
        ax.legend(loc='best')
        # 调整观察角度和方位角。这里将俯仰角设为30度，把方位角调整为-45度
        ax.view_init(30, -45)
        plt.show()
    #当簇的中心点发生明显的变化时继续递归k_mean函数
    else:
        gap1=b
        gap2=c
        gap3=d
        return k_mean(b,c,d)





#TODO OD流向图
def draw_OD(label:[str],position:[(int,int)],array:[int]):

    # array = [[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [3, 4, 5, 6, 8]]
    # 一般矩阵要求方阵
    # draw_3D(*array)
    #
    # array = np.array([[0, 4, 3, 4], [2, 0, 3, 6], [1, 4, 0, 8], [2, 4, 5, 6]])
    # a = draw_OD(label=['1', '2', '3', '4'], position=[(1, 4), (6, 6), (8, 4), (2, 7)], array=array)
    # a.show()

    plt.style.use('mpl15')
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    x=[i[0] for i in position]
    y=[i[1] for i in position]
    plt.scatter(x,y,s=np.pi*3**2,alpha=0.6,color='#000000')

    for i in range(len(label)):
        plt.text(*position[i],label[i],size=15)

    sum_array=array.sum()
    for j in range(len(array[0])):
        for i in range(len(array[0])):
            if i>=j:
                break
            else:
                plt.plot([position[j][0],position[i][0]],[position[j][1],
                position[i][1]],c='red',linewidth=40*(array[j][i]/sum_array))

    plt.axis('off')
    plt.title("OD出行量")
    return plt


def exchange_num(num:float)->float:
    """
    :param num: 比较大的整型或者浮点型的数据
    :return: 转换为10以内的float 缩小
    """
    while True:
        if num < 10:
            break
        else:
            num /= 10
            continue
    return num

def exchange_position(position:[float,float])->(float,float):
    """
    :param position: 转换坐标，扽比例缩小
    :return: 缩小后的结果
    """
    if isinstance(position[0],float):
       return (exchange_num(position[0]),exchange_num(position[1]))
    else:
        raise Exception("type diffence")



# TODO 出行行为比例
# TODO 不同时间段的出行目的图形 {"时间段":(频率,"出行行为目的")}
#同一时间段，不同出行目的的频次
#总的



# def bulid_dict1(list1:[str],list2:[float],list3:[str])->[{str:(float,str)}]:

def hitt_road(dict_all: [{str: (float, str)}], labelstr_dict, labelstr_tuple):
    k = fittler_car_road(dict_all, labelstr_tuple)

    # def fittler_car_road(dict1: [{str: (float, str)}], label: [str] = ['1', '2']):
    # def fittler_part(car: str) -> [[int]]:
    # 返回[[int,int..]] 不同车辆车型,不同类型

    container = []
    for i in labelstr_dict:
        container.append(k(i))

    list_cars = list(chain.from_iterable(container))
    list_road = [1, 2] * len(labelstr_dict)
    con_l = [0] * len(labelstr_dict) * 2
    col = [label[i // 2] for i in range(len(con_l))]

    def add_info(labelx:str,labely:str,hue1:str):
        p = draw_hitt(list_cars, list_road, col,labelx,labely,hue1)
        p.show()

    return add_info

    # def draw_hitt(list1: [int], list2: [str], list3: [str], labelx='各车种', labely='不同车道上的频数',hue1='car_road') -> plt:  # 因车道不同的图形



# def draw_pie(*args:list or int,sheet_exchange=[2,1.5,1,1,2.5],label = ["小汽车", "中型车", "大型车", "货车", '公交车'])->plt:

# def return_car(dictt:{str:float or iter}):

# def return_args(dicctt:{str:float},label=['小汽车','中型车','大型车','货车','公交车'])->[[float],[float]]:

# return_args 转换为各个label对应的数据的（长度) -> [len(i) for i in args:[[...]]]->[int]


def get_center(a:[[float]])->[[float]]:

    b = np.zeros(0)
    c = np.zeros(0)
    d = np.zeros(0)

    #随机选择三个中心点，计算所有值到中心点的距离
    for i in range(0,len(a)):
        dis1=np.linalg.norm(a[i:i+1]-a[7:8])
        dis2=np.linalg.norm(a[i:i+1]-a[99:100])
        dis3=np.linalg.norm(a[i:i+1]-a[112:113])
        # 根据每个点与各个簇中心的距离将每个对象重新赋给最近的簇
        if min(dis1,dis2,dis3)==dis1:
            b=np.append(b,a[i:i+1])
            x=int(len(b)/4)
            b=np.reshape(b,newshape=(x,4))
        if min(dis1,dis2,dis3)==dis2:
            c=np.append(c,a[i:i+1])
            x=int(len(c)/4)
            c=np.reshape(c,newshape=(x,4))
        if min(dis1,dis2,dis3)==dis3:
            d=np.append(d,a[i:i+1])
            x=int(len(d)/4)
            d=np.reshape(d,newshape=(x,4))
    #对新生成的簇的所有值求平均值来获得新的簇中心点
    b=np.mean(b,axis=0)
    c=np.mean(c,axis=0)
    d=np.mean(d,axis=0)
    #运行k_mean函数
    return (b,c,d)


def to_args(centroids:[[...]])->[[...]]:
    """
    :param centroids: [[x,y,z],[x,y,z]...]
    :return:  (list1,list2,list3) ->[[x...],[y...],[z...]
    """
    list1=[i[0] for i in centroids]
    list2=[i[1] for i in centroids]
    list3=[i[2] for i in centroids]

    return (list1,list2,list3)

def draw_3D_union(centroids,color = ['blue', 'red', 'yellow', 'Lime', 'Cyan', 'purple', 'Gray', 'Olive']):
    #绘制联合的3D聚类图形
    fig = plt.figure()
    for j,i in enumerate(centroids):
        # 绘制单个图形,[(x...),(y...),(z...)]
        list1,list2,list3=to_args(i)
        if isequal_lenght(list1,list2,list3):
            a = np.array([list1,list2,list3])
            ax1 = Axes3D(fig, auto_add_to_figure=False)
            fig.add_axes(ax1)
            ax1.scatter(list1, list2, list3, c=color[j])
            ax1.view_init(30, -45)
        else:
            raise Exception("Input ERROR")
    plt.show()


