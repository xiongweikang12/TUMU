import math
import numpy as np
from functools import reduce

class Isfit:
    """
    拟合概率对象，
    choice_isbool判断对象是否为bool类类型
    iterable判断对象是否为可迭代对象
    """

    @staticmethod
    def choice_isbool(obj1)->bool:
        return isinstance(obj1,bool)

    @staticmethod
    def iterable(obj1)->bool:
        return hasattr(obj1,'__iter__')

    # @staticmethod
    # def counter_tuple(tuple1)->int:
    #     return tuple1[0]*tuple1[1]
    #
    # @staticmethod
    # def counter_tuple_N(tuple1)->int:
    #     return tuple1[1]

class BOsong(Isfit):


    """
    泊松分布
    文档：
    在一定时间间隔到达的车辆，
    或在一定距离内分布的车辆数是随机变数，
    所得的数列可以用离散型分布描述
    这是其中一种，泊松分布
    P(k)---在计数间隔t内到达k辆车或个人的概率
    R--单位时间间隔的平均到达率
    t--每个计数间隔持续时间或距离
    P(k)=((Rt)**k)*e**(-Rt)/k! ,k=0,1,2,3...

    若令 m=Rt为计数时间t内平均到达的车辆
    P(k)=(m**k)*(e**-m)/k!
    当m为已经知道的计数时间间隔t内恰好有k辆车到达的概率
    p(<=k)=sum((m**k)*(e**-m)/k!)

    递推公式：
        p(0)=e-m
        p(k+1)=(m/(k+1）)*P(k)



    """

    __slots__ = ('__R', '__t', '__k','__m','__list1')

    def __init__(self,R,t,k,list1):
        """
        :param R: 单位时间间隔的平均到达率
        :param t: 时间间隔，需要保持单位统一
        :param k:
        """
        self.__R=R
        self.__t=t
        self.__k=k
        self.__list1=list1
        self.__M=self.build_m()
        #对于泊松的数据拟合，期望和rT相同作为计算P的参数

        try:
            self.__Square=self.__Square
        except NameError:
            self.__Square=self.__M

    @property
    def set_k(self)->int:
        return self.__k
    @set_k.setter
    def set_k(self,k):
        self.__k=k

    @property
    def M_average(self)->float:
        return self.__M
    @M_average.setter
    def M_average(self,M):
        self.__M=M

    @property
    def Ds_sqarue (self):
        return self.__Square
    @Ds_sqarue.setter
    def Ds_sqarue(self,sqarue):
        self.__Square=sqarue



    def build_m(self)->float:
        """
        :param list1: 时间间隔内车数，间隔时间
        :return:
        """
        if ((super().choice_isbool(self.__R) and super().choice_isbool(self.__t)) and super().iterable(self.__list1)):
            #表示R,T没有，或list1没有
            # 表示R，T没有
            total_N = reduce(lambda x, y: x + y, list(map(lambda x: x[1], self.__list1)))
            m = reduce(lambda x, y: x + y, list(map(lambda x: x[0] * x[1], self.__list1)))
            m = m / total_N
            sqarue=reduce(lambda x,y:x+y,list(map(lambda x: math.pow((x[0]-m),2)*(x[1]) ,self.__list1)))
            sqarue=sqarue/(total_N-1)
            self.Ds_sqarue=sqarue
            # self.M_average = m #将拟合数据，方差，期望修改。
            return m

        else:
            if (super().iterable(self.__list1)):#表示是RT,有，list1也有
                raise Exception("list1 and Rt only given one")
            elif (~super().choice_isbool(self.__R) and ~super().choice_isbool(self.__t)): #表示list1没有
                return self.__R * self.__t
            else: #表示list没有，也部分有
                raise Exception("list1 is iterable or RT_ValueERRoR")

    # def __repr__(self):
    #     print("时间间隔:{}\n单位时间间隔到达率:{}\n期望，方差:{}\n".
    #           format(self.__t,self.__R,self.__t*self.__R))

    #装饰器是在主题函数的基础功能上，可以灵活加入我们想要的功能

    def show_doc(string_):
        def show_deco(func):
            def warapper():
                print("面向对象装饰器")
                print(string_)
                func()
            return warapper
        return show_deco

    @staticmethod
    @show_doc("算法")
    def show1():
        pass

    @staticmethod
    def get_p(m,j) -> float:
        return ((math.pow(m, j) * (math.exp(-m))) / math.factorial(j))

    def counter_proable(self,model)->float:
        """
        :param model: 模式 =,>,<,<=,>=
        :return:
        """
        m = self.build_m()

        if (model=='='):
            proable=self.get_p(m,self.__k)

        elif (model=='>'or model=='<='):
            proable=reduce(lambda x,y:x+y,[self.get_p(m,i) for i in range(self.__k+1)])
            if (model==">"):
                proable=1-proable
            if (model=="<="):...

        elif (model=='<' or model=='>='):
            proable=reduce(lambda x,y:x+y,[self.get_p(m,i) for i in range(self.__k)])
            if (model=='>='):
                proable=1-proable
            if (model == '<'): ...

        else:
            raise Exception('model cant match ')

        return proable

    def show_content(self):
        print("泊松分布")
        print("m:{}\nk:{}\n"
        .format(self.__M,self.__k))

class TwinItem(Isfit):
    """
    二项分布：
        p(K):在计数间隔t内到达k辆车或k个人的概率
        R:单位时间间隔的平均到达率
        t:每个计数间隔持续时间或距离
        n:正整数(分布参数)

    p=Rt/n

    """
    __slots__ = ('__p','__list1','__n','__k')
    def __init__(self,p,list1,n,k):
        """
        :param p:  概率
        :param list1: 拟合数据
        list1=[(k,f)...]
        :param n: 分布参数
        :param k:
        """
        self.__p=p
        self.__list1=list1
        self.__n=n
        self.__k=k
        self._kk=self.get_m()
        #二项分布数据拟合时，返回p计算参数,均值，
        #  方差在self.get_m方法中通过属性方法设置

    @property
    def set_k(self):
        return self.__k

    @set_k.setter
    def set_k(self,k):
        self.__k=k

    @property
    def M_average(self) -> float:
        return self.__M

    @M_average.setter
    def M_average(self, M):
        self.__M=M

    @property
    def Ds_sqarue(self):
        return self.__sqarue

    @Ds_sqarue.setter
    def Ds_sqarue(self, sqarue):
        self.__sqarue=sqarue

    def get_m(self)->float:
        if super().choice_isbool(self.__p) and super().iterable(self.__list1):
            total_ = reduce(lambda x, y: x + y, list(map(lambda x: x[0] * x[1], self.__list1)))
            total_N = reduce(lambda x, y: x + y, list(map(lambda x: x[1], self.__list1)))
            m = total_ / total_N #期望
            total_square = reduce(lambda x, y: x + y, list(map(lambda x: math.pow(x[0] - m, 2) * x[1], self.__list1)))
            self.__sqarue = total_square / (total_N - 1) #方差
            self.__M=m
            p = (m - self.__sqarue) / m
            self.__n = m // p
            return p

        else:
            if super().iterable(self.__list1):
                raise Exception("list1 and p cant together")
            elif ~super().choice_isbool(self.__p):
                return self.__p
            else:
                raise Exception("list1 and p least given one")

    @staticmethod
    def get_p(m,n,k):
        Cnk = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        return (Cnk * math.pow(m, k)) * math.pow(1 - m, n - k)

    def counter_proable(self,model)->float:
        """
        :param model: 模式 =,>,<,<=,>=
        :return:
        """
        m = self.get_m()

        if (model=='='):
            proable=self.get_p(m,self.__n,self.__k)

        elif (model=='>'or model=='<='):
            proable=reduce(lambda x,y:x+y,[self.get_p(m,self.__n,i) for i in range(self.__k+1)])
            if (model==">"):
                proable=1-proable
            if (model=="<="):...

        elif (model=='<' or model=='>='):
            proable=reduce(lambda x,y:x+y,[self.get_p(m,self.__n,i) for i in range(self.__k)])
            if (model=='>='):
                proable=1-proable
            if (model == '<'): ...

        else:
            raise Exception('model cant match ')

        return proable

    def show_content(self):
        print("二项分布")
        print("分布参数:{}\n概率p:{}\nk:{}\n"
        .format(self.__n,self._kk,self.__k))










    # def show_doc(self):
    #     def show_deco(func):
    #         def warapper():
    #             print("面向对象装饰器")
    #             print(self.__doc__)
    #             func()
    #         return warapper
    #     return show_deco

    # def show1():
    #     pass

class Negative_TwinItem(Isfit):

    """
    负二项分布
    文档：
        基本公式：略
        其公式中有两个参数，负二项分布参数p,B.0<p<1 B为正整数
        用于计算在计数间隔t内到达的k辆车或人的几率
        适用条件方差较大，方差/期望明显大于1是
    """
    #先不去计算拟合的参数

    __slots__ = ('__B','__k','__p')

    def __init(self,B,k,p):
        self.__B=B
        self.__k=k
        self.__p=p

    @property
    def set_k(self):
        return self.__k

    @set_k.setter
    def set_k(self,k):
        self.__k=k

    @staticmethod
    def get_m(B,p,k)->float:
        C=(math.factorial(k+B-1))/(math.factorial(B-1)*math.factorial(k))
        return C*(math.pow(p,B)*math.pow(1-p,k))

    def counter_proable(self,model)->float:
        """
        :param model: 模式 =,>,<,<=,>=
        :return:
        """
        # m = self.get_m()

        if (model=='='):
            proable=self.get_m(self.__B,self.__p,self.__k)

        elif (model=='>'or model=='<='):
            proable=reduce(lambda x,y:x+y,[self.get_m(self.__B,self.__p,i) for i in range(self.__k+1)])
            if (model==">"):
                proable=1-proable
            if (model=="<="):...

        elif (model=='<' or model=='>='):
            proable=reduce(lambda x,y:x+y,[self.get_m(self.__B,self.__p,i) for i in range(self.__k)])
            if (model=='>='):
                proable=1-proable
            if (model == '<'): ...

        else:
            raise Exception('model cant match ')

        return proable

    # def __repr__(self):
    #     print("{}\n{}\n{}".format(self.__B,self.__k,self.__p))
    #

#TODO 连续型分布
class Negative_E(Isfit):
    """
    负指数分布
    描述事件之间时间间隔的分布为称为连续分布
    连续型分布常用来描述车头时距或穿越空挡，速度等交通流特性的分布特性
    """
    __slots__ = ('__R','__t','__Q')

    def __init(self,R,t,Q):
        self.__R=R
        self.__t=t
        self.__Q=Q
        if (self.string_or_R()):
            raise   Exception("at least one obj userful")

    def string_or_R(self)->bool:
        if super().choice_isbool(self.__R) and super().choice_isbool(self.__Q):
            #如果都为bool类型
            return True
        elif super().choice_isbool(self.__R):
            #表示Q不为bool,__R为bool
            self.__R=self.__Q/3600
            return False
        else:
            #表示Q为bool
            return False
    @property
    def M_average(self):#期望
        return 1/self.__R

    @property
    def Ds_sqarue(self):#方差
        return 1/math.pow(self.__R,2)

    @staticmethod
    def get_p(R,t):
        return math.exp(-R*t)

    def counter_p(self,model)->float:

        if (model=='>='):
            proable=self.get_p(self.__R,self.__t)
        else:
            proable=1-self.get_p(self.__R,self.__t)

        return proable

class Choice_model:
    #多态对不同模型，的不同

    __slots__ = ('__obj')

    def __init__(self,obj):
        self.__obj=obj

    def __repr__(self)->str:
        #print 方差，期望
        print("期望:{:.3f}\t方差:{:.3f}\t方差比期望:{:.3f}\t"
            .format(
              self.__obj.M_average,
              self.__obj.Ds_sqarue,
              self.__obj.Ds_sqarue/self.__obj.M_average
            )
        )
        self.__obj.show_content()
        return 'allright'


# l=BOsong(369,97/3600,11,None)
# c=Choice_model(l)
# print(c)
#









