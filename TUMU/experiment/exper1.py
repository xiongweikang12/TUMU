import itertools
import copy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pie_search import draw_pie
import seaborn as sns
import pandas as pd



#速度转换
def s_to_v(s:float,listt:[float])->list[float]:#返回速度
    """
    :param s:距离
    :param listt:时间间隔
    :return: 速度列表
    """
    return list(map(lambda x:(s/x)*3.6,listt))


def return_car(dictt:{str:float})->function:
    """
    :param dictt:字典 车型:速度
    :return: 闭包
    """
    def car(model:str)->dict:
        filter_=list(filter(lambda x:x.get(model),dictt))
        return list(map(lambda x:x.get(model),filter_))
    return car
    #返回车辆的频数


def return_args(dicctt:{str:float})->[[float],[float]]:
    a=return_car(dicctt)
    min_car=a("小汽车")
    midlle_car=a('中型车')
    dig_car=a('大型车')
    trade_car=a('货车')
    bus_car=a('公交车')
    return [min_car,midlle_car,dig_car,trade_car,bus_car]



#TODO 箱体图
def staright_draw(list1:[(float)],list2:[(float)],tilte:str)->plt:#一个方向的，传入两个的两个
    """
    :param list1:机器测量速度
    :param list2:人工测量速度
    list:[(),()...] 各种车型的速度
    :return:
    """
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    plt.subplot(1,2,1)
    plt.title(tilte)
    labels=["小汽车", "中型车", "大型车", "货车", '公交车']
    plt.boxplot([i for i in list1],labels=labels,showmeans=True,patch_artist=True,boxprops={'color':'orangered','facecolor':'pink'})
    plt.ylabel("KM/H")
    plt.subplot(1,2,2)
    plt.title(tilte+"(人工测法)")
    plt.boxplot([i for i in list2],labels=labels,showmeans=True,patch_artist=True,boxprops={'color':'orangered','facecolor':'pink'})

    plt.ylabel("KM/H")
    return plt


def return_lenght(list)->int:#返回频数
    return len(list)


def into_all(*args)->list:#将各个的集结成整体
    return list(args)

def key_value(list1:[str],list2:[float])->[dict]:
    containter=[]
    for i in range(len(list1)):
        dict = {}
        dict[list1[i]]=list2[i]
        containter.append(dict)
    return containter


#TODO 画直方图
def draw_hitt(list1:[int],list2:[str],list3:[str])->plt: #因车道不同的图形

    """
    :param list1:各车辆
    :param list2: 对应车道
    :return:
    list->[len....] 车次频率
    """
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    df=pd.DataFrame()
    df['各车种']=list3
    df['不同车道上的频数']=list1
    df['car_road']=list2
    ax=sns.barplot(data=df,x='各车种',y='不同车道上的频数',hue='car_road',palette="Blues_d")
    return plt



def changeto_interager(n:float):
    #将float转换为10单位大小的int类型，如11.5->10
    return int(n/10)*10


def return_label(list1:[float])->list[str]:
    #传入的数据是已经排序完成的
    """
    :param list1: 速度列表,根据速度生成其对应区间[18.256...]
    :return: return_str:速度区间标签列表,label:如速度[20,30,...]
    """

    low_num = changeto_interager(list1[0])
    height_num = changeto_interager(list1[-1])
    label = [i for i in range(low_num, height_num + 10, 10)]

    def return_str():
        label_return=[0]*(len(label)+1)
        label_return[0]='<'+str(low_num)
        label_return[-1]='>'+str(height_num)
        for j in range(1,len(label)):
            label_return[j]=str(label[j-1])+'~'+str(label[j])

        return label_return

    return (return_str,label)


def build_dictt(list1:[str],list2:[int])->{(int,int):str}:
    """
    :param list1:速度字符串列表
    :param list2: 速度 [int,int...]
    :return: 返回一个字典
    """
    label_new=[0]+list2+[list2[-1]+200]
    dict={}
    for i in range(len(list1)):
        dict[(label_new[i],label_new[i+1])]=list1[i]

    return dict




def return_w(list1:[float])->[str] and [float]:

    # dict11={(0,20):"<20",(20,30):"20~30",(30,40):"30~40",(40,50):"40~50",(50,60):"50~60",(60,200):">60"}
    label = return_label(list1)
    label_num=label[1] #[20,30,...]
    label=label[0]() #[<20,20~30...]
    #创建字典
    dictl=build_dictt(label,label_num)
    # dict11={(0,20):"<20",(20,30):"20~30",(30,40):"30~40",(40,50):"40~50",(50,60):"50~60",(60,200):">60"}
    container = copy.copy(list1)
    for k,kk in enumerate(container):
        for i,j in dictl.items(): # tuple,str
            if i[0]<kk<=i[1]:
                container[k]=j
            else:
                continue

    #根据对应速度生成对应区间,containter
    conter=[len(list(filter(lambda x:x==i,container)))/len(container) for i in label]
    #遍历label,fiterr过滤得到，不同label的频率
    conter=list(itertools.accumulate(conter,func=lambda x,y:x+y))
    #累积频率


    dict1={}
    for i in range(len(label)):
        dict1[label[i]]=conter[i]
    container_1=copy.copy(container)
    #创建dict将label(速度分布）与累计频率对应，建立hash字典
    for j in range(len(container)):
        container_1[j]=dict1.get(container[j])
        #返回相应的累计频率

    return container,container_1  #x,y
    #containter[str]["<20","20~30"...]
    #containter_1 :[float,...]


def return_index(list1:[float],num:float):
    """
    :param list1: 速度列表
    :param num: 最值的百分比
    :return:
    """
    max_num=list1[-1]
    # index_,num=list((filter(lambda x:x<=num*max_num,list1)))[0]
    # index_=list1.index(num)
    # return (index_,num)
    return list(enumerate(filter(lambda x:x<=max_num*num,list1)))[0]
    #返回一个tuple


def draw_line(listx:[str],listy:[float])->plt:

    """
    :param listx: 速度对应区间
    :param listy: 速度对应累积百分比
    :return: plt
    """
    sns.set(style='darkgrid')
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    df=pd.DataFrame()
    df['累计频率']=listy
    df['地点车速Km/h']=listx
    sns.lineplot(data=df,x='地点车速Km/h',y='累计频率')
    return plt










# list1=[1,3,4,5,6,7,8,9,10,12,13,14]
# num=0.5
# print(return_index(list1,num))
#

# a=staright_draw(,'各车辆速度')
# a.show()

# l1=["大客车", "中型车", "小汽车", "公交车", '货车']
# l2=[1,2,3,4,5,6]#速度或者，时间间隔
# l3=s_to_v(0.25,l2)
# print(l3)
# p=key_value(l1,l2)
# j=return_car(p)
# a=j('小汽车')
# print(a)#返回频数,集合成一个,传入draw_starigiht 箱体图
# k=into_all(a)
# print(k,*k)
# list_test=[1,2,4,6,8]
# l=draw_pie(*list_test)
# l.show()
#
#


