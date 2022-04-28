#TODO 内外加法定价，计算边际成本，运输量
class CO:#父类定义公共属性

    # __slots__ = ('FC','list_AVC','rate','profit')

    def __init__(self,FC,list_AVC,rate,profit):
        """
        :param FC: 固定成本
        :param list_AVC: 可变成本列表，长度为三
        list[0]+TQ/list[1]+list[2]/TQ
        :param rate: 税
        :param TQ: 运输量
        """
        self.__FC=FC
        self.__list_AVC=list_AVC
        self.__rate=rate
        self.__profit=profit
        #父类定义子类中公有部分，避免代码服用

    def __repr__(self):
        return "我是一个CO实例:\n" \
               "固定成本:{}\n" \
               "AVC:{}\n" \
               "税率:{}\n" \
               "期望利润:{}"\
            .format(self.__FC
            ,self.__list_AVC
            ,self.__rate
            ,self.__profit)
    #魔法方法：就是实例对象做出某种行为,自动调用的方法
    #像是__init__创建实例时自动调用


    @property
    def FC(self) -> int:
        return self.__FC
    @FC.setter
    def FC(self,FC):
        self.__FC=FC

    @property
    def list_AVC(self)->list:
        return self.__list_AVC
    @list_AVC.setter
    def list_AVC(self,list_AVC):
        self.__list_AVC=list_AVC

    @property
    def rate(self)->float:
        return self.__rate
    @rate.setter
    def rate(self,rate):
        self.__rate=rate

    @property
    def profit(self)->int:
        return self.__profit
    @profit.setter
    def profit(self,profit):
        self.__profit=profit



class T_Price(CO):
    """
    文档： T_Price

    功能：实现计算定价
    总运量：TQ
    平均可变成本：根据总运量的关系得到 AVC
    平均固定成本：固定成本/总运量 AFC
    平均总成本：平均可变成本+平均固定成本 ATC
    单位运量利润：期望利润/总运量 DJ
    成本利润率：期望利润/平均总成本（ATC)*总运量(TQ) CJ
    收入利润率：期望利润/(期望利润+平局总成本(ATC)*总运量(TQ)) SJ
    外加法：(平均总成本(ATC)*(1+成本利润率CJ)/(1-税率)
    内加法：（ATC/(1-CJ-税率)
    """

    def __init__(self,FC,list_AVC,rate,TQ,profit):

        super().__init__(FC,list_AVC,rate,profit)
        #super().__init__()调用父类初始化的方法
        self.TQ=TQ

    def counter_IE(self):
        #TODO 定价内外加法
        AVC=self.list_AVC[0]+(self.TQ/self.list_AVC[1])+(self.list_AVC[2]/self.TQ)
        AFC=self.FC/self.TQ
        ATC=AVC+AFC
        DJ=self.profit/self.TQ
        CJ=self.profit/(ATC*self.TQ)
        SJ=self.profit/(self.profit+(ATC*self.TQ))
        E_price=(ATC*(1+CJ))/(1-self.rate)
        I_price=(ATC/(1-SJ-self.rate))
        AC=AFC+AVC
        VC=AVC*self.TQ
        TC=ATC*self.TQ

        # "平均可变成本：{}\n平均固定成本：""{}\n"
        # "平均总成本：{}\n单位运量利润率：{}\n"
        # "成本利润例：{}\n收入利率：{}\n"
        # "定价一：{} \n定价二：{} \n".

        # print(AVC,AFC,ATC,DJ,CJ,SJ,E_price,I_price)
        if (self.TQ%100==0):
            print(self.TQ,AVC,VC,AFC,TC,ATC)
        else:
            print(self.TQ,AVC,VC,AFC,TC,' ')

        return [self.TQ,AVC,VC,AFC,TC,ATC]
        #显示数据的动作
    def Get_TQ(self,cost_rate):
        pass


class Limit_cost(CO):
    """
    文档：Limit_cost

    功能：计算范围内的边际成本
    TQ~(star,end ,step:100) 可以修改step
    VC(TQ+1)-VC(TQ)
    VC=AVC*TQ
    MC=AVC(TQ+1)*(TQ+1)-AVC(TQ)*TQ
    边际成本
    """

    def __init__(self, FC, list_AVC, rate,profit,sart,end):
        """
        :param sart: 开始
        :param end: 结束
        """
        super().__init__(FC, list_AVC, rate, profit)
        self.__sart=sart
        self.__end=end
        self.__step=100

    @property
    def step(self):
        return self.__step
    @step.setter
    def step(self,step):
        self.__step=step

    def count_limit(self) ->None:
        #循环遍历,在每个遍历前加上一个数
        container=[]
        container_t=[]
        MC_container=[]
        for i in range(self.__sart,self.__end+self.__step,self.__step):
            container.append(i)
            container.append(i+1)
        for j in container:
            # newObject=T_Price(self.__object.FC,self.__object.list_AVC,self.__object.rate,j,self.__object.profit)
            newObject=T_Price(super().FC,super().list_AVC,super().rate,j,super().profit)
            #super 实际是调用父类的方法
            #在一个类中通过其他的类创造对象
            list1=newObject.counter_IE()
            container_t.append(list1)


        for k in range(0,len(container_t)-1,2):
            MC = (container_t[k + 1][0] * container_t[k + 1][1]) - (container_t[k][0] * container_t[k][1])
            MC_container.append(MC)



        # container_tt=[container_t[l].append(MC_container[l//2]) for l in range(len(container_t))]
        # print(container_tt)
        print(MC_container)

co=CO(180,[1,1500,150],0.056,200)
print(co)
# print(list(CO.__dict__.values())[3])
l=Limit_cost(180,[1,1500,150],0.056,200,300,900)
k=T_Price(180,[1,1500,150],0.056,30,200)
l.count_limit()
print(l.__doc__)
print(k.__doc__)



#__doc__:表示类的描述信息
#__dict__:用来查看类或对象成员
# newObject=T_Price(self.__object.FC,self.__object.list_AVC,self.__object.rate,j,self.__object.profit)
# newObject=T_Price(super().FC,super().list_AVC,super().rate,j,super().profit)
'''
装饰器，闭包解读：

def deco(func):
    def wrapper():
        print('{}函数进来拉'.format(func()))
        print("函数")
    return 1

@deco #func=deco(func) 关键就是这句
def func():
   print("hello")
   time.sleep(1)
   print("world")

a=func #a==1
print(a)

如： 以闭包的方式返回
def deco(func):
    def wrapper():
        print('{}函数进来拉'.format(func()))
        print("函数")
    return wrapper

@deco #func=deco(func) --> func==wraper funtion object
func() --> wrapper() --> print('{}函数进来拉'.format(func())),print("函数")

'''

