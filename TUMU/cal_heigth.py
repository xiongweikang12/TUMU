
import numpy as np


class Cal_Height:
    change_point = 2990 # 变坡点桩号的数字类型
    point_height = 18  # 变坡点的高程
    L_R = 20000  # 竖曲线半径
    point_distance = 20  # 桩距
    steer_1 = 0.0092 # 斜1
    steer_2 = -0.0082  # 斜2
    steer_w = np.abs(steer_2 - steer_1)
    # shape_road_flag = True  # 路的形状默认为凹

    def __init__(self, point):
        self.point = point  # 表示桩号

    @staticmethod
    def shape_road():
        shape_road_flag=False #默认为凸
        if (Cal_Height.steer_2 - Cal_Height.steer_1) > 0: #下凹
            shape_road_flag = True
        if (Cal_Height.steer_2 - Cal_Height.steer_1) < 0: #上凸
            shape_road_flag = False
        return shape_road_flag

    @staticmethod
    def curve_lin(): #竖曲线要素
        return Cal_Height.L_R * Cal_Height.steer_w

    @staticmethod
    def T_lin(): #竖曲线要素，切线
        return Cal_Height.curve_lin() / 2

    @staticmethod
    def E_distance():
        target1 = (Cal_Height.T_lin()) ** 2
        return target1 / (2 * Cal_Height.L_R)

    @staticmethod
    def start_point(): #起点桩号
        start_point_num = Cal_Height.change_point - Cal_Height.T_lin()
        K = start_point_num // 1000
        K_later = start_point_num - (K * 1000)
        # print("起点桩号:K{},{}".format(K,K_later))
        return start_point_num

    @staticmethod
    def end_point(): #终点桩号
        end_point_num=Cal_Height.change_point+Cal_Height.T_lin()
        return  end_point_num

    @staticmethod
    def start_height():  # 起点高程
        T = Cal_Height.T_lin()
        if Cal_Height.shape_road():
            start_height_num = Cal_Height.point_height + (T * np.abs(Cal_Height.steer_1))
        else:
            start_height_num = Cal_Height.point_height - (T * np.abs(Cal_Height.steer_1))

        return start_height_num

    def level_distance(self):  # 横距x
        distance_x = self.point - Cal_Height.start_point()
        return distance_x

    def height_distance1(self):  # 竖距h1
        level_distance2 = (self.level_distance()) ** 2
        return level_distance2 / (Cal_Height.L_R * 2)

    def height_distance2(self):  # 竖距h2
        level_distance1 = (self.level_distance()) * np.abs(Cal_Height.steer_1)
        return level_distance1 + Cal_Height.start_height()

    def self_height(self):  # 高程
        return self.height_distance2() - self.height_distance1()

    def show_point(self):
        K = self.point // 1000
        K_later = self.point - (K * 1000)
        print("点桩号:K{},{}".format(K, K_later))

    def show_data(self):
        # 桩号,横距,竖距,切线上点高程，设计高程
        self.show_point()
        print("横距为{}\n".format(self.level_distance()))
        print("竖距为{}\n".format(self.height_distance1()))
        print("切线上点高程{}\n".format(self.height_distance2()))
        print("设计高程{}\n".format(self.self_height()))


#  a = Cal_Height(5120)
#  a.show_data()
