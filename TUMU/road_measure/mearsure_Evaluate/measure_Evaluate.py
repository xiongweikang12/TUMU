import math
import numpy as np
from functools import reduce


# TODO 非等精度观测值精度评定
class Precision_Evaluate:  # 精度评定
    """
    算术平均值
    平均值  -> 加权平均
    观测中位差 -> 单加中误差
    平均中误差 -> 加权平均值的中误差
    """

    def __init__(self, *args):
        self.args = args

    def average_num(self):
        return sum(self.args) / len(self.args)
        # 算术平均值

    @staticmethod
    def True_Error(numa, list2):
        #默认以毫米为单位
        average = numa
        trueerror = list(map(lambda x: (average - x)*1000, list2))
        return trueerror

    @staticmethod
    def length_1(list1):
        return len(list1) - 1

    @staticmethod
    def length(list1):
        return len(list1)

    # 输入的函数为
    def average_Error(self):
        def Middle_Error():
            T_E = self.True_Error(self.average_num(), self.args)
            l = self.length_1(T_E)
            Error_M = np.sqrt(sum(list(map(lambda x: math.pow(x, 2), T_E))) / l)
            average_E = Error_M / np.sqrt(l)
            return Error_M, average_E
            # 中误差,平均中误差

        return Middle_Error


class Average_Evaluate(Precision_Evaluate):
    ...

class Power_Evaluate(Precision_Evaluate):

    def __init__(self, list_p, H, L):
        self.__list_p = list_p
        self.__H = H
        self.__L = L
        ...

    # 外部获得，修改权重
    @property
    def Get_power(self):
        return self.__list_p

    @Get_power.setter
    def Get_power(self, list1):
        self.__list_p = list1

    def average_num(self, modle):
        if modle == 'L':
            target = self.__L
        if modle == 'H':
            target = self.__H
        P_target = reduce(lambda x, y: x + y, list(map(lambda x, y: x * y, self.Get_power, target)))
        P_all = reduce(lambda x, y: x + y, self.Get_power)
        # 单位误差

        return P_target / P_all

    def average_Error(self, target, modle):
        """
        :param target: 观测值
        :param modle: 权依据
        :return: 加权平均中误差，单中误差
        """

        if target == 'L':
            target = self.__L
        if target == 'H':
            target = self.__H
        aver =self.average_num(modle)
        P = self.Get_power
        True_Error = super().True_Error(aver, target)
        l = super().length_1(True_Error)
        U = np.sqrt(reduce(lambda x, y: x + y, list(map(lambda x, y: x * math.pow(y, 2), P, True_Error))) / l)

        # averager_P_error
        S_P = reduce(lambda x, y: x + y, P)
        Mx = U / (np.sqrt(S_P))

        return Mx, U

