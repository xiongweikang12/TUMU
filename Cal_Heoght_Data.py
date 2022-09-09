# test
from cal_heigth import Cal_Height


class Test_data:
    # 以下为未调整的坡度
    i1 = 12 / (990 + 220)
    i2 = 4 / (480 + 10)
    i3 = 12 / (310 + 520)

    i1_e = 0.0092
    i2_e = -0.0082
    i3_e = 0.0145

    point_list = [2220, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600,
                  2650, 2700, 2800, 2850]

    var = [2854, 2870, 2890, 2910, 2926, 2940, 2960, 2980, 2993.313, 3010, 3030, 3050, 3060.26, 3080,
           3100, 3120, 3132.86, 3150, 3200, 3250, 3300]

    var1 = [3320, 3340, 3360, 3380, 3400, 3420, 3440, 3460, 3484.25, 3510, 3530, 3550,
            3568.49, 3590, 3610, 3648.879, 3700, 3750]

    var2 = [3900,3950,4000,4050,4100,4150,4200,4250,4310]


Cal_Height.steer_1 = Test_data.i1_e
Cal_Height.steer_2 = Test_data.i2_e


# def append_point_list(point: int):
# Test_data.point_list.append(point)


def start():
    for i in Test_data.point_list:
        print(Cal_Height(i).self_height())

# point_c = int(input())
# append_point_list(point_c)

#test 试验区
