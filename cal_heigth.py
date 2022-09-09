
import numpy as np


class Cal_Height:
    change_point = 5030  # 变坡点桩号的数字类型
    point_height = 427.68  # 变坡点的高程
    L_R = 2000  # 竖曲线半径
    point_distance = 20  # 桩距
    steer_1 = 0.05  # 斜1
    steer_2 = -0.04  # 斜2
    steer_w = np.abs(steer_2 - steer_1)
    shape_road_flag = True  # 路的形状默认为凹

    def __init__(self, point):
        self.point = point  # 表示桩号

    @staticmethod
    def shape_road():
        if (Cal_Height.steer_2 - Cal_Height.steer_1) > 0:
            Cal_Height.shape_road_flag = True
        if (Cal_Height.steer_2 - Cal_Height.steer_1) < 0:
            Cal_Height.shape_road_flag = False

    @staticmethod
    def curve_lin():
        return Cal_Height.L_R * Cal_Height.steer_w

    @staticmethod
    def T_lin():
        return Cal_Height.curve_lin() / 2

    @staticmethod
    def E_distance():
        target1 = (Cal_Height.T_lin()) ** 2
        return target1 / (2 * Cal_Height.L_R)

    @staticmethod
    def start_point():
        start_point_num = Cal_Height.change_point - Cal_Height.T_lin()
        K = start_point_num // 1000
        K_later = start_point_num - (K * 1000)
        # print("起点桩号:K{},{}".format(K,K_later))
        return start_point_num

    @staticmethod
    def start_height():  # 起点高程
        T = Cal_Height.T_lin()
        start_height_num = Cal_Height.point_height - (T * Cal_Height.steer_1)
        return start_height_num

    def level_distance(self):  # 横距x
        distance_x = self.point - Cal_Height.start_point()
        return distance_x

    def height_distance1(self):  # 竖距h1
        level_distance2 = (self.level_distance()) ** 2
        return level_distance2 / (Cal_Height.L_R * 2)

    def height_distance2(self):  # 竖距h2
        level_distance1 = (self.level_distance()) * Cal_Height.steer_1
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


a = Cal_Height(5120)
a.show_data()
