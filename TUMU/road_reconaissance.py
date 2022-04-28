import numpy as np
import math
import matplotlib.pyplot as plt

class Road_con():# TODO  关于道路平面设计，直线，曲线转角

    def __init__(self,tuple1,tuple2):
        """
        :param tuple1: 线段结点坐标1
        :param tuple2: 线段结点坐标2
        """
        self.tupple1=tuple1
        self.tupple2=tuple1

    def Dxdivdy(self): #返回方位角，显示象限角
        self.dx=self.tupple1[0]-self.tupple2[0]
        self.dy=self.tupple1[1]-self.tupple2[0]
        self.s=np.sqrt((self.dx**2)+(self.dy**2)) #交点间距
        self.arctan=(np.arctan(np.abs(self.dy/self.dx))*(180/np.pi))
        print('dx:{},dy:{},s:{},象限角:{}'.format(self.dx, self.dy, self.s, self.arctan))
        if (self.dx<0 and self.dy>0):
            self.arctan=180-arcan
        else:
            pass
        print("方位角{}".format(self.arctan))
        return self.arctan  # 方位角度




class Road_two(): #TODO 平曲线几何要素

    def __init__(self,ls,R,fun_obj2,fun_obj1): #初始化，

        """
        :param ls:  缓和曲线长度
        :param R:   圆曲线半径
        :param fun_obj2:  方位角2
        :param fun_obj1:  方位角1

        转角 a=A2-A1;

        """

        self.ls=ls
        self.R=R
        self.fun_obj2=fun_obj2
        self.fun_obj1 = fun_obj1
        self.T_add_return=self.T_add()
        self.move_into_return=self.move_into()
        self.two_anger_minus_return=self.decide_two_anger()
        self.reanger_return=self.reanger()
        self.length_of_tangent_return=self.length_of_tangent()
        self.strcurve_length_return=self.strcurve_length()
        self.curve_length_return=self.curve_length()

    def decide_two_anger(self):
        # print("A2-A1转角:{}".format(self.fun_obj2-self.fun_obj1))
        if ((self.fun_obj2-self.fun_obj1) < 0):
            print("左转")
        else:
            print("右转")
        return self.fun_obj2-self.fun_obj1

    def draw_di(self,list_tuple):
        plt.style.use('ggplot')
        self.scx=[i[0] for i in list_tuple]
        self.scy=[j[1] for j in list_tuple]
        plt.scatter(self.scx,self.scy,color='b')
        # x=[[list_tuple[e][0],list_tuple[e+1][0]] for e,i in enumerate(list_tuple)]
        # y=[[list_tuple[e][1],list_tuple[e+1][1]] for e,i in enumerate(list_tuple)]
        # plt.annotate('text', xy=(tx0, ty0), xytext=(tx1, ty1), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
        for k in  range(len(self.scx)):
            plt.annotate('({:.2f},{:.2f})'.format(self.scx[k],self.scy[k]),
                         xy=(self.scx[k],self.scy[k]),
                         xytext=(self.scx[k]+5,self.scy[k]+5),
                         arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

        colorlist=['r','y','b','g']
        for e in range(len(list_tuple)-1):
            plt.plot([list_tuple[e][0],list_tuple[e+1][0]],
            [list_tuple[e][1],list_tuple[e+1][1]],colorlist[(e%4)]+'-')


        plt.show()

    def T_add(self): #切线增长值
        return (self.ls/2)-(math.pow(self.ls,3))/(240*(math.pow(self.R,2)))

    def move_into(self): #内移值
        return ((math.pow(self.ls,2))/(24*self.R))-((math.pow(self.ls,4)/(2688*(math.pow(self.R,3)))))

    def reanger(self): #缓和曲线角
        return 28.6479*(self.ls/self.R)

    def length_of_tangent(self):#fun_obj1--move_into #切线长
        target1=self.R+self.move_into_return
        target2=np.tan(np.abs(self.two_anger_minus_return))
        target3=self.T_add_return
        return (target1*target2)+target3

    def strcurve_length(self): #平曲线长
        return ((np.abs(self.two_anger_minus_return)
                 -(2*self.reanger_return))*((np.pi/180)*self.R))\
               +(2*self.ls)

    def curve_length(self): #圆曲线长
        return (self.strcurve_length_return-(2*self.ls))

    def show_data(self):
        print("切线增长值 ：{} \n内移值 :{} \n缓和曲线角 :{}\n切线长 :{} \n平曲线长 :{} \n圆曲线长 :{} \n"
              .format(self.T_add_return,
                      self.move_into_return,
                      self.reanger_return,
                      self.length_of_tangent_return,
                      self.strcurve_length_return,
                      self.curve_length_return))
    #TODO 计算路线桩号
    def get_stack_num(self):
        pass


if __name__=="__main__":
    tuple1 = (55217.39, 60138.25)
    tuple2 = (55234.64, 60394.96)
    tuple3 = (55106.21, 60683.62)
    list1 = [tuple1, tuple2, tuple3]
    road_1 = Road_two(35, 150, 10, 20)
    road_1.show_data()
    road_1.draw_di(list1)

