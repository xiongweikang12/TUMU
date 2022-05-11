import numpy as np
import math
from functools import reduce

class Measure_road:
    """
    计算高差，根据闭合高差，得到改正后的高差
    """
    def __init__(self,list1,Hs):
        """
        :param list1:list(L,h)
        :param Hs: 起点高程
        :param He: 终点高程
        :return:
        """
        self.list1=list1
        self.Hs=Hs

    @property
    def close_h(self):
        sum_h = reduce(lambda x, y: x + y, [i[0] for i in self.list1])
        return sum_h

    @property
    def sumL(self):
        sum_L = reduce(lambda x, y: x + y, [i[1] for i in self.list1])
        return sum_L

    @property
    def close_h_average(self):
        chose_H = self.close_h
        sum_L = self.sumL
        average_h = [i[0] + (-(chose_H) * (i[1] / sum_L)) for i in self.list1]
        return average_h
        #改正后高差

    def get_newH(self):
        container=[self.Hs]
        close_h=self.close_h_average
        for i in close_h:
            container.append(container[-1]+i)
        return container

    @property
    def name(self):
        return "name"
    @property
    def maxError_h(self):
        L=self.sumL
        if isinstance(L,int):
            return 12*math.sqrt(L)
        elif isinstance(L,float):
            return 40*math.sqrt(L)
        else:
            raise Exception("Type ERROR")



    def __repr__(self):
        print("数据:{}\n改正后高差:{}\n闭合高差:{}\n高程:{}\n"
        .format(self.list1,self.close_h_average,self.close_h,self.get_newH()))
        print("容许高差:{}".format(self.maxError_h))
        return self.name

class Measure_roadAB(Measure_road):
    """
    附和水准线
    """
    def __init__(self,list1,Hs,He):
        super().__init__(list1,Hs)
        self.He=He

    @property
    def close_h(self):
        sum_h = super().close_h
        return sum_h - (self.He - self.Hs)

    @property
    def name(self)->str:
        return "附和水准线"

class Measure_roadAB_circul(Measure_road):

    @property
    def name(self)->str:
        return "闭合水准路线"
    ...