#TODO 地球曲率对测量的影响
import math
import numpy as np
from functools import reduce

class measure_error:


    def __init__(self, D):
        self.__R = 6371
        self.__D = D
        #私有属性不可以继承

    @property
    def R(self):
        return self.__R

    @R.setter
    def R(self, R):
        self.__R = R

    @property
    def D(self):
        return self.__D

    @D.setter
    def D(self,D):
        self.__D=D

class distance_error(measure_error):
    """
    地球曲率对测量距离的影响,
    用曲面的距离与实际距离的差表示产生的误差
    """
    __slots__ = ('__R','__D')


    def Error(self):
        D_straight=self.D+(math.pow(self.D,3)/(3*math.pow(self.R,2)))
        D_diff=D_straight-self.D
        D_divide=D_diff/self.D
        return D_divide

class Height_error(measure_error):
    """
    地球曲率对测量距离的影响
    用曲面的高度差
    """
    __slots__ = ('__R','__D')


    def Error(self):
        """
        用self.__D替代D_straight
        :return:
        """
        return math.pow(self.D,2)/self.R


# l=distance_error(10000)
# a=l.Error()
# print(a)
#

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

    def __repr__(self):
        print("数据:{}\n改正后高差:{}\n闭合高差:{}\n高程:{}\n"
        .format(self.list1,self.close_h_average,self.close_h,self.get_newH()))
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
        sum_h = reduce(lambda x, y: x + y, [i[0] for i in self.list1])
        return sum_h - (self.He - self.Hs)

    @property
    def name(self)->str:
        return "附和水准线"


class Measure_roadAB_circul(Measure_road):

    @property
    def name(self)->str:
        return "闭合水准路线"
    ...




list1=[(2.145,1.2),(4.271,1.0),(-6.918,1.1),(3.554,0.8),(-2.756,1.5),(6.339,1.4)]
l=Measure_roadAB(list1,30.236,36.936)
print(l)









