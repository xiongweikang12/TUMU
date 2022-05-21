# TODO 行车延误调查
import math
import operator
import os
import re
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from functools import lru_cache
from scipy import integrate


plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示正文标签
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号


# TODO 输入输出法调查延误，读取来往车辆，计算相关参数，延误，绘制图形
class Trans_IO:

    def __init__(self, list1:[tuple,tuple]):
        """
        :param list1: list[tuple1,tuple2]
        tuple1:到达车数
        tuple2:离去车数
        """

        self.come_data = list1[0]
        self.go_data = list1[1]
        self.come_co = 0
        self.go_co = 0
        self.come_sum = []
        self.go_sum = []
        self.time_gap = []
        self.come_sum = self.get_come_data()
        self.go_sum = self.get_go_data()
        self.time_gap = self.count_time_gap()
        self.__able_though = None
        self.__though_time = None
        self.compare_with()
        self.x_start,self.x_end=self.draw_chart()  # 两个函数拟合后的数据
        a,b=self.show_info()

    @property
    def able_though(self):
        return self.__able_though
    @able_though.setter
    def able_though(self,n):
        self.__able_though=n
    @property
    def though_time(self):
        return self.__though_time
    @though_time.setter
    def though_time(self,n):
        self.__though_time=n


    def get_come_data(self):
        for i in self.come_data:
            self.come_co += i
            self.come_sum.append(self.come_co)

        return self.come_sum

    def get_go_data(self):
        for i in self.go_data:
            self.go_co += i
            self.go_sum.append(self.go_co)

        return self.go_sum

    def show_info(self):
        print("到达车数:{}\n离去车数:{}"
              .format(self.come_sum, self.go_sum))
        print(self.come_data_fit, self.go_data_fit)

        return self.come_data_fit,self.go_data_fit
    def count_time_gap(self):
        for i in range(1, len(self.come_sum) + 1):
            self.time_gap.append(i * 15)
        return self.time_gap

    def draw_chart(self):
        # TODO 添加标题文本，x,y轴，箭头标签
        plt.axis([0, 105, 0, 600])

        num_come_polyfit = np.polyfit(self.time_gap, self.come_sum, 2)
        num_go_polyfit = np.polyfit(self.time_gap, self.go_sum, 1)

        funtion_come_p = np.poly1d(num_come_polyfit)
        funtion_go_p = np.poly1d(num_go_polyfit)

        self.come_data_fit, self.go_data_fit = \
            [funtion_come_p[i] for i in range(2, -1, -1)], \
            [funtion_go_p[i] for i in range(1, -1, -1)]

        # 拟合函数的系数
        y_p_funtion = funtion_come_p(np.linspace(15, 90, 100))
        X_time_start, X_time_end, X_time_full, full_num = self.compare_with()
        # 堵塞开始时刻 ,阻塞开始消失,瓶颈通过，瓶颈序号
        full_delay_cars = self.come_sum[full_num] - self.go_sum[full_num]  # 车数
        able_though = (15 / self.go_data[full_num])  # 通行能力
        though_time = full_delay_cars * able_though  # 通行时间
        though_time_siganl=1/able_though #单个通过时间
        self.able_though=able_though
        self.though_time=though_time
        # print(though_time,full_delay_cars,self.come_sum[full_num])

        print("堵塞开始时刻 :{},阻塞开始消失 :{}".format(X_time_start, X_time_end))
        text_pos_start = self.go_data_fit[0] * (X_time_start) + self.go_data_fit[-1]
        text_pos_end = self.go_data_fit[0] * (X_time_end) + self.go_data_fit[-1]

        plt.annotate('(堵塞开始时刻\n{:.2f})'.format(X_time_start),
                     xy=(X_time_start + 1, text_pos_start + 1),
                     xytext=(X_time_start + 10, text_pos_start + 20),
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
        # 文本右移动五个单位，上移五个单位

        plt.annotate('(堵塞逐渐结束时刻\n{:.2f})'.format(X_time_end),
                     xy=(X_time_end + 1, text_pos_end + 1),
                     xytext=(X_time_end + 10, text_pos_end + 20),
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

        plt.text(X_time_start - 10, text_pos_start - 90, 'f(x)')
        plt.text(X_time_end - 10, text_pos_end + 20, 'g(x)')

        # TODO 画出两条竖线，一条横线
        # f_full_y=0
        # j=len(self.come_data_fit)-1
        # for i in range(len(self.come_data_fit)): # 0~3
        #     if (i==j):
        #         f_full_y+=self.come_data_fit[j]
        #     else:
        #         f_full_y+=(math.pow(X_time_full,j-i)*self.come_data_fit[i]
        length_l = len(self.come_data_fit) - 1
        squar_list = [length_l - i for i in range(len(self.come_data_fit))]
        f_full_y = reduce(lambda x, y: x + y,
                          [self.come_data_fit[i] * math.pow(X_time_full, squar_list[i])
                           for i in range(len(self.come_data_fit))])
        g_full_x = (f_full_y - self.go_data_fit[1]) / self.go_data_fit[0]

        plt.plot([X_time_full, X_time_full], [self.go_sum[full_num], f_full_y], 'r--')
        plt.plot([X_time_full, g_full_x], [f_full_y, f_full_y], 'r--')
        # 添加文本
        plt.text(X_time_full - 30, self.go_sum[full_num], "时间，时刻{}时\n的受阻车辆为{}"
                 .format(self.time_gap[full_num], self.come_sum[full_num] - self.go_sum[full_num]))
        plt.text(X_time_full + 15, self.go_sum[full_num], "第{}辆车通过\n瓶颈段的时间为{:.2f}"
                 .format(self.come_sum[full_num], though_time))
        plt.plot(np.linspace(15, 90, 100), y_p_funtion, color='red', linestyle='-')
        plt.plot(self.time_gap, self.come_sum, color='black', linestyle=':')
        plt.plot(self.time_gap, self.go_sum, color='black', linestyle=':')
        plt.grid(True)
        plt.title("到达离去曲线图")
        plt.xlabel("时间")
        plt.ylabel("累计车辆/辆")
        plt.show()
        return X_time_start,X_time_end

    def compare_with(self):
        # TODO 获取信息，得到堵塞形况
        for i in (range(len(self.come_sum))):
            if self.come_sum[i] - self.go_sum[i] > 0:
                break
            # 堵塞开始时刻
        for j in (range(len(self.come_sum))):
            try:
                if (self.come_sum[j] - self.go_sum[j]) < (self.come_sum[j - 1] - self.go_sum[j - 1]):
                    break
                else:
                    continue
            except IndexError:
                continue
            # 阻塞开始消失

        return self.time_gap[i], self.time_gap[j], self.time_gap[i + 1], i + 1
        # 堵塞开始时刻 ,阻塞开始消失,瓶颈通过，瓶颈序号

    # def next_pass(self):
    #
    #     # TODO 积分延误车数
    #     # 平均行驶时间=总延误时数/通行量
    #     # 无阻塞时
    #     # 平均延误
    #     # 平均每辆车延误 #sh #
    #
    #     come_fit=self.come_data_fit #到达车数的函数拟合
    #     go_fit=self.come_data_fit #离去车数的函数拟合
    #     def ding_fun(x):
    #         f_full_y = reduce(lambda x, y: x + y,
    #                           [come_fit[i] * math.pow(x,[j in range(len(come_fit),-1,-1)][i])
    #                            for i in range(len(come_fit))])
    #






# TODO 交叉口调查延误，读取excel，计算相关参数延误
class Trans_cross:

    def __init__(self):
        self.believe_section = 0.9
        self.K_double = 2.7
        self.time_interval = 15
        self.file_name=r'D:\python\pythonProject4\TUMU\Trans_Engineering\transport_string_factor\stu.xls'
        self.sheet_name="stu"
        self.open_chart()
        self.count_all()
        self.show_content()
        # self.sum_stop_car,self.sum_nostop_car,self.all_car\
        #     =self.open_chart()

    def open_chart(self):
        sheet_work = pd.read_excel(io=self.file_name,sheet_name=self.sheet_name)
        ser_stop_car = sheet_work['停止车辆'].values
        ser_nostop_car = sheet_work['不停车辆'].values
        car_all = sheet_work.iloc[:, :-2]
        self.sum_nostop_car = sum(ser_nostop_car)  # 不停数量
        self.sum_all_car = sum(car_all.sum())  # 总数车辆
        self.sum_stop_car= sum(ser_stop_car)  # 停车数量
        self.sum_nostop_car= sum(ser_nostop_car)  # 不停数量
        self. sum_all_car = sum(car_all.sum())  # 总数车辆

    def count_all(self):
        self.all_delay = self.sum_all_car * (self.time_interval)  # 总延误
        self.average_car_stop = self.all_delay / self.sum_stop_car  # 每辆车的平均延误
        self.average_car_cross = self.all_delay / (self.sum_stop_car + self.sum_nostop_car)  # 交叉口每辆车的平均延误
        self.stop_prior = self.sum_stop_car / (self.sum_stop_car + self.sum_nostop_car)  # 停车百分比
        self.stop_diff_prior = np.sqrt(((1 - self.stop_prior) * self.K_double)  # 停车百分比的容许误差
                                       / (self.stop_prior * (self.sum_stop_car + self.sum_nostop_car)))

    def show_content(self):
        print("置信区间:{}\n置信度 :{}\n时间间隔 :{}\n".format(self.believe_section, self.K_double, self.time_interval))
        print("观测到的停驶总车数:{:}辆\n停车数:{:}辆\n不停车数:{:}辆\n总延误:{:}辆.s\n每辆停车的平均延误:{:.2f}s\n"
              "交叉口引道上每辆车的平均延误:{:.2f}s\n停车百分比:{:.2f}%\n停车百分比的容许误差:{:.2f}%"
              .format(self.sum_all_car, self.sum_stop_car, self.sum_nostop_car
                      , self.all_delay, self.average_car_stop, self.average_car_cross
                      , self.stop_prior * 100, self.stop_diff_prior * 100))

    def open_excel(self):
        os.system(self.file_name)


# TODO 浮动车调查速度，读取来往数据，计算速度相关参数,（调查整条道路两个方向）
class double_Tran_floating_car_speed:
    # TODO 双方向的
    def __init__(self, road_distance, list_east_west):
        """
        :param road_distance: 观测路段长度
        :param list_east_west:
        [list_east,list_west]
        [时间，对向车辆来数量，超车-被超车]
        example: [(2.56,48.5,0.67),(2.55,36.2,0.33)]
        """
        self.road_distance = road_distance
        self.east_time = list_east_west[0][0]
        self.east_amount = list_east_west[0][1]
        self.east_amount_subtract = list_east_west[0][2]
        self.west_time = list_east_west[1][0]
        self.west_amount = list_east_west[1][1]
        self.west_amount_subtract = list_east_west[1][2]
        self.calculate_partmeter()
        self.show_content()

    def calculate_partmeter(self):
        self.traffic_q_east = ((self.west_amount + self.east_amount_subtract) / (self.east_time + self.west_time)) * 60
        self.average_time_east = self.east_time - (self.east_amount_subtract / (self.traffic_q_east / 60))
        self.average_speed_east = (self.road_distance / self.average_time_east) * 60
        self.traffic_q_west = ((self.east_amount + self.west_amount_subtract) / (self.west_time + self.east_time)) * 60
        self.average_time_west = self.west_time - (self.west_amount_subtract / (self.traffic_q_west / 60))
        self.average_speed_west = (self.road_distance / self.average_time_west) * 60

    def show_content(self):
        print("\n向东行情况\n交通量:{:.0f}辆/h\n平均行驶时间:{:.2f} min\n平均车速:{:.1f} km/h\n"
              .format(self.traffic_q_east, self.average_time_east, self.average_speed_east))
        print("\n向西行情况\n交通量:{:.0f}辆/h\n平均行驶时间:{:.2f} min\n平均车速:{:.1f} km/h\n"
              .format(self.traffic_q_west, self.average_time_west, self.average_speed_west))


# TODO 调查一个方向
class signal_Tran_floating_car_spend:

    # TODO 单方向的
    def __init__(self, road_distance, list_sigal_dict):
        """
        :param road_distance: 线路长度
        :param list_sigal_dict:
        [face_car,minus_car,float_car_spend]
        face_car:迎面相遇的车辆数
        minus_car:超越观测车减去被超越测试车的数量
        浮动车的自身速度
        """
        self.road_distance = road_distance
        self.face_car = list_sigal_dict[0]
        self.minus_car = list_sigal_dict[1]
        self.float_car_spend = list_sigal_dict[2]

    # TODO 时间通过，浮动车的速度与待测路段的长度的商计算
    def counter_time(self):
        return self.road_distance / self.float_car_spend

    # TODO 交通量计算 q=X+Y/t+t
    def colcul_traffic(self):
        driver_time = self.counter_time()
        traffic_amount = (self.face_car + self.minus_car) / (driver_time * 2)
        return traffic_amount

    # TODO 计算平均时间 t_average=t-(Y/q)
    def colcul_averagetime(self):
        driver_time = self.counter_time()
        traffic_amount = self.colcul_traffic()
        average_time = driver_time - (self.minus_car / traffic_amount)
        return average_time

    # TODO 计算平均速度 v_average=(l/t_average)
    def colcul_averagespeed(self):
        average_time = self.colcul_averagetime()
        average_speed = (self.road_distance / average_time)
        return average_speed


class Sample_speed:

    def __init__(self, Admissable_Error):
        """
        :param Admissable_Error: 容许误差
        :param Confidence_Level: 置信水平
        """
        self.admissable_error = Admissable_Error
        self.confidence_level = 1.96
        self.Variance = 0.5
        self.Sample_num = self.colcultate_Sample_Num()
        self.show_content()

    def colcultate_Sample_Num(self):
        return (math.pow(self.confidence_level, 2) * math.pow(self.Variance, 2)) / math.pow(self.admissable_error, 2)

    def show_content(self):
        print("\n至少应该取:{:.0f}个样本".format(self.Sample_num + 1))


# TODO 出入量法计算路段交通量，时刻密度
class Trans_IO_K:
    """
    1.计算交通交通密度
        E(t)=E(t0)+(Qa(t)-Qb(t))
        E(t0)=q+a-b
        q-从t0到t1时刻通过B处的车辆数
        a-被试验车超越的车辆数
        b-超越试验车的车辆数
        q为时间累计量[(42,18),58,(20,40)]
        q=18+58+20
        E(t2)=E(t1)+Qa-Qb

        K=E(t)/L
    2.绘制路段存车辆与累计交通量的关系
        Qa=Qa+E(to)

    """

    def __init__(self, list1, thougth, by_thougth, road_distance):
        """
        :param list1: 数据列表
        :param thougth: 超越试验车的车辆
        :param by_thougth: 被试验车超越的车辆
        :param road_distance: 路段长度
        list[tuple,tuple]
        其中时段中间的用（q1,q2）
        表示试验车驶入，驶出时段的断面量交通量
        """
        self.listA = list1[0]  # 驶入A断面交通量
        self.listB = list1[1]  # 驶出B断面交通量
        self.thougth = thougth
        self.by_thougth = by_thougth
        self.road_distance = road_distance
        self.prime = self.get_prime()
        self.continer_K, self.continter_E = self.counter_every_E()
        self.show_chart()

    def get_prime(self) -> int:

        """
        :param list1:
        [to~t1的车辆数总数]
        :return: E(t0)
        """
        sum = 0
        for i in range(len(self.listB)):
            if isinstance(self.listB[i], tuple):
                sum += self.listB[i][1]
                break
            else:
                continue
        # 表示第一个开始时间
        for j in self.listB[i + 1:]:
            if isinstance(j, tuple):
                sum += j[0]
                break
            else:
                sum += j

        # sum=reduce(lambda x,y:x+y,list1)
        sum = sum + self.by_thougth - self.thougth
        return sum
        # 返回E(t0)

    def counter_every_E(self):
        continer_E = []
        for i in range(len(self.listB)):
            if (isinstance(self.listB[i], tuple)):
                break
            else:
                continue
        E_start = (self.prime + self.listA[i][1] - self.listB[i][1]) \
                  - (sum(self.listA[i]) - sum(self.listB[i]))
        # 根据驶入时间段，得到记录开始的累计交通量
        continer_E.append(E_start)
        continer_E.append(self.prime + self.listA[i][1] - self.listB[i][1])
        for j in range(i + 1, len(self.listB)):
            if (isinstance(self.listA[j], tuple)):
                continer_E.append(continer_E[-1] + (sum(self.listA[j]) - sum(self.listB[j])))
            else:
                continer_E.append(continer_E[-1] + self.listA[j] - self.listB[j])

        # [k / self.road_distance for k in continer_E]
        continer_E_time = list(map(lambda x: x / self.road_distance, continer_E))
        return continer_E_time, continer_E  # 瞬时密度,时刻车辆数

    def show_chart(self):
        # TODO 画图，时刻于累计车辆数
        plt.style.use('ggplot')
        Q_add_E = []
        E_B = []
        E_A = []
        for i in range(len(self.continter_E)):
            if (isinstance(self.listB[i], tuple)):
                E_A.append(sum(self.listA[i]))
                E_B.append(sum(self.listB[i]))
                Q_add_E.append(self.continter_E[i] - sum(self.listB[i]))
            else:
                E_A.append(self.listA[i])
                E_B.append(self.listB[i])
                Q_add_E.append(self.continter_E[i] - self.listB[i])

        time_l = [j for j in range(len(self.listB))]
        # [j + self.prime for j in E_A]
        E_A = list(map(lambda x: x + self.prime, E_A))
        plt.plot(time_l, E_A, 'r')
        plt.plot(time_l, E_B, 'b--')
        plt.axis([0, len(time_l), 0, 300])
        plt.title("A,B路段的存在车辆数与A，B点累计交通量关系")
        plt.xlabel("时刻T")
        plt.ylabel('累计交通量Q')
        # TODO 设置标题,设置坐标轴信息，text文本
        plt.show()


# TODO 交通量
class Trans_BasicQ:
    """
     文档 ：Trans_BasicQ 基础交通量调查

     1.对不同车型进行车辆换算，
        得到道路不同车辆分布情况
        绘制饼图

     2.得到换算后的交通量

     3.计算小时高峰量系数PHF ,绘制小时交通量图

     """

    def __init__(self, list1, label):
        """
        :param list1:
        list1:[().....]
        tuple:各车型的数据，左转，直行，右转
        :param label: 各车型标签

        """
        # self.dig_car_exchange=2
        # self.mid_car_exchange=1.5
        # self.normal_car_exchange=1
        # self.bus_exchage=1
        # self.track_exchage=2.5
        self.decide_lengt(list1, label)
        self.__list1 = list1
        self.__label = label
        # __表示

    def decide_lengt(self, list1, label):
        if (len(list1) == len(label)):
            ...
        else:
            raise Exception("list can not match label")

    @property
    # @property：属性方法，把方法变成一个静态属性，调用和访问实例属性的方式一样 object.funtion
    def digtial_list1(self) -> list:
        return self.__list1

    @digtial_list1.setter
    def digital_list1(self, list1) -> None:
        self.__list1 = list1

    def draw_pie(self, change_car_list:[float]) -> int:
        """
         :param change_car_list: 车辆换算表
         :return:转换后的交通量总数
         """
        if len(self.__list1) == len(change_car_list):
            porp_all = reduce(lambda x, y: x + y,
                              [sum(self.__list1[i]) * change_car_list[i] for i in range(len(self.__list1))])
            # 获取总的换算后交通量
            porp_part = [sum(self.__list1[j]) * change_car_list[j] / porp_all for j in range(len(self.__list1))]
            # 换算后各百分比
            explode = [0] * len(self.__list1)
            max_index, max_number = max(enumerate(porp_part), key=operator.itemgetter(1))
            explode[max_index] = 0.1

            plt.pie(x=porp_part, explode=explode,
                    labels=self.__label, autopct='%.2f%%',
                    pctdistance=0.8, labeldistance=1.1,
                    startangle=180, radius=1.2, shadow=True,
                    textprops={'fontsize': 10, 'color': 'black'})
            # wedgeprops={'linewidth': 1.5, 'edgecolor': 'blue'})
            plt.title('机动车换算后分布')
            plt.axis('equal')
            plt.show()
            return porp_all
        else:
            raise Exception("list can not match change_list")
            ...

    @staticmethod
    # 装饰器 @staticmethod:静态方法，函数不属于类了，没有类的属性，但是还是通过类对象调用
    def Max_trans_phf(list1, time_interval) -> plt:
        # 开发时的->return返回类型
        """
         :param list1: 各时间段的交通量情况
         :param time_interval: 调查时间间隔
         :return: PHF高峰小时系数
         """
        if (isinstance(list1, str)):
            Intger_Trans = [int(i) for i in re.findall("\d{2,3}", list1)]
            max_index, max_trans = max(enumerate(Intger_Trans), key=operator.itemgetter(1))
            phf = sum(Intger_Trans) / (max_trans * (60 / time_interval))
        else:
            Intger_Trans = list1
            max_trans, max_index = max(enumerate(Intger_Trans), key=operator.itemgetter(1))
            phf = sum(Intger_Trans) / (max_trans * (60 / time_interval))
        # TODO 绘制小时交通量图
        plt.style.use('ggplot')
        time_x = list(range(0, 60, time_interval))
        plt.plot(time_x, Intger_Trans, 'b--')
        plt.plot(time_x[max_index], max_trans, 'r*')
        plt.text(time_x[max_index], max_trans + 4, '时段内统计最高交通量:{}'.format(max_trans))
        plt.title("以{}为间隔的一个小时交通量统计".format(time_interval))
        plt.xlabel("时间")
        plt.ylabel("交通量")
        plt.axis([0, 70, 0, max_trans + 50])
        plt.grid(True)
        print("PHF:{}".format(phf))
        return plt


"""
面向对象方法：
装饰器 @staticmethod:静态方法，函数不属于类了，没有类的属性，但是还是通过类对象调用
@classmethod:类方法，通过类方法调用，而不是实例调用，不能访问实例变量，只能访问类变量
@property：属性方法，把方法变成一个静态属性，调用和访问实例属性的方式一样 object.funtion
装饰器：接受函数作为参数做点事情，返回一个函数，闭包思想
"""

