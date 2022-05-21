#TODO 排队论模型
import math
from functools import reduce

class Quene_distribution:

    @staticmethod
    def distribution_protable_model(n,p):
        """
        :param n:顾客数量
        :param p: 服务强度
        :param model: 选择模式
        :return: 闭包
        """

        def distribution_protable(model)->float:

            if (model=='=='):
                if n==0:
                    return 1-p
                else:
                    return (1-p)*math.pow(p,n)

            if (model=='<='):
                property_sum=list(map(lambda x:(1-p)*math.pow(p,x),list(range(n+1))))
                property_sum_1=reduce(lambda x,y:x+y,property_sum)
                return property_sum_1

            if (model=='>'):
                property_sum = list(map(lambda x: (1 - p) * math.pow(p, x), list(range(n + 1))))
                property_sum_1 = reduce(lambda x, y: x + y, property_sum)
                return 1-property_sum_1

        return distribution_protable


class M_M_1(Quene_distribution):
    """
    单通道服务系统
    """
    def __init__(self,R,U):
        """
        :param R:平均到达率
        :param U: 平均服务水平
        """
        self.__R=R
        self.__U=U
        self.p=self.__R/self.__U

    @property
    def return_U(self):
        return self.__U

    @property
    def return_R(self):
        return self.__R

    def no_cunstom(self):
        return 1-self.p

    def average_n(self): #系统中平均顾客数量
        return self.p/(1-self.p)

    def varicance(self): #系统中顾客数量的方差
        return self.p/math.pow(1-self.p,2)

    def average_quene_lenght(self): #平均排队长度
        return self.average_n()-self.p

    def NoZero_quene_lenght(self): #非零平均排队长度
        return 1/(1-self.p)

    def consum_time(self): #排队系统中的平均消耗时间
        return self.average_n()/self.__R

    def average_WaitTime(self):
        return self.consum_time()-(1/self.__R)

    def get_protable(self,model,n):
        protable=super().distribution_protable_model(n,self.p)
        return protable(model)


class M_M_N(M_M_1):
    """
    对于排队论的单个服务对象
    """
    def __init__(self,R,U,N):
        super().__init__(R,U)
        self.N=N

    def no_cunstom(self):
        func1=reduce(lambda x,y:x+y,[math.pow(self.p,i)/math.factorial(i) for i in range(self.N)])
        func2=math.pow(self.p,self.N)/(math.factorial(self.N)*(1-self.p/self.N))
        return 1/(func1+func2)
        #系统中没有顾客的概率 p(0)

    def average_n(self):
        func1=(math.pow(self.p,self.N+1))/math.factorial(self.N)*self.N
        func2=self.no_cunstom()/(1-self.p/self.N)**2
        return self.p+func1*func2
        #系统中的平均顾客数量

    def average_quene_lenght(self):
        return self.average_n()-self.p
        #平均排队长度

    def consum_time(self):
        return self.average_n()/self.return_R

    def average_WaitTime(self):
        return self.average_quene_lenght()/self.return_R

    @staticmethod
    def distribution_protable_model(k,p,N,p0):

        def signal_p(k:int,p:float,N:int,p0:float)->float:
            #单个用户的概率
            if k<N:
                func1=math.pow(p,k)/math.factorial(k)
                return func1*p0
            elif k>=N:
                func1=math.pow(p,k)/(math.factorial(N)*math.pow(N,k-N))
                return func1*p0
            else:
                raise Exception("cant match")

        def pro_model(k,p,N,p0,model):
            if moedl=='=':
                proable=signal_p(k,p,N,p0)
            elif model=='<=':
                proable=reduce(lambda x,y:x+y,[signal_p(i,p,N,p0) for i in range(k+1)])
            elif model=='>':
                proable=1-reduce(lambda x,y:x+y,[signal_p(i,p,N,p0) for i in range(k+1)])
            else:
                raise Exception("no match model")
            return proable

        pro_model
        #通过闭包返回内部函数:多个概率->单个概率的累加 sum通过列表推导式返回

    def get_protable_1(self,model:str,k:int)->float:
        pro_model=self.distribution_protable_model(k,self.p,self.N,self.no_cunstom())
        return pro_model(model)
        #计算频率,根据给定的model ==，>=,< ->return

newobject=M_M_N(1/60,1/200,4)
print(newobject.no_cunstom())





