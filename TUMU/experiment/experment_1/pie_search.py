# TODO 绘制非机动车与机动车的饼图
import operator

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib


# 非机动车的行车
# list_dig:[int] or int , list_mid:[int] or int , list_min:[int] or int , list_bus:[int] or  int , list_tarde:[int]or int
def draw_pie(*args:list or int,sheet_exchange=[2,1.5,1,1,2.5],label = ["小汽车", "中型车", "大型车", "货车", '公交车'])->plt:
    #判断传入参数是否长度相等,是否能对应
    if len(args)==len(sheet_exchange)==len(label):
        pass
    else:
        raise Exception("lenghtoflist cant macth")

    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    #对应两种model，一种是传入int,一种是传入[int...]
    # sheet_exchange=[2,1.5,1,1,2.5]
    list_args=args #其是一个tuple
    if isinstance(list_args[0],int):
        # porp=[list_dig*2,list_mid*1.5,list_min,list_bus,list_tarde*2.5]
        porp=[sheet_exchange[i]*list_args[i] for i in range(len(sheet_exchange))]
    else:
        porp=[sum(list_args[i])*sheet_exchange[i] for i in range(len(sheet_exchange))]

    # 直行，右转，左转
    porp = np.array(porp)
    porp_ = sum(porp)
    porp_num = porp / porp_
    explode = [0]*len(label)

    def return_index_max(list1:[int or float])->int:
        maxindex,maxnum=max(enumerate(list1),key=operator.itemgetter(1))
        return maxindex

    explode[return_index_max(porp_num)] = 0.1
    # colors = ['3333aa', 'ffff##', '##ffff']
    plt.pie(x=porp_num, explode=explode, labels=label, autopct='%.2f%%', pctdistance=0.8, labeldistance=1.1,
            startangle=180,
            radius=1.2, shadow=True
            , textprops={'fontsize': 10, 'color': 'black'})  # wedgeprops={'linewidth': 1.5, 'edgecolor': 'blue'})
    plt.title('机动车换算后分布')
    plt.axis('equal')
    return plt



# if __name__ == "__main__":
#         a = [0, 3, 0,1,2]
#         b = [1, 97, 62,2,4]
#         c = [4, 103, 210,4,8]
#         d = [0, 1, 15,12,16]
#         e = [0, 0, 5,18,15]
#         j=draw_pie(a,b,c,d,e)
#         j.show()


