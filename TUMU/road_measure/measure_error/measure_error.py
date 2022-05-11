#TODO 地球曲率对测量的影响
import math
import numpy as np
from functools import reduce

class measure_error:
    """
    计算误差
    """

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
        return math.pow(self.D,2)/(2*self.R)











