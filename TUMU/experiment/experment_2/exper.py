import itertools

from TUMU.Trans_Engineering.trans_survey.transportation_survey_delay_IO import Trans_IO
from scipy import integrate
import math
from functools import reduce
from itertools import accumulate

class TEST:
    #实验数据
    come_car=(80,100,120,90,70,70)
    go_car=(80,90,90,90,90,90)
    list1=[come_car,go_car]
    all_car=list(itertools.accumulate(go_car))[-1]

newobject=Trans_IO(TEST.list1)
x_start=newobject.x_start
x_end=newobject.x_end
come_fit=newobject.come_data_fit
go_fit=newobject.go_data_fit
able_though=newobject.able_though
though_time=newobject.though_time*60

def f(x):
    func_1=reduce(lambda x, y: x + y,
                          [come_fit[i] * math.pow(x,len(come_fit)-i)
                           for i in range(len(come_fit))])
    func_2=reduce(lambda x, y: x + y,
                          [go_fit[i] * math.pow(x,len(go_fit)-i)
                           for i in range(len(go_fit))])
    return func_1-func_2

def aver_divertime(delay:int,able_though:float,all_though:int):
    aver_driver=delay/all_though    # 瓶颈车辆所需的平均行驶时间
    time_nofill=60/able_though    #无阻塞时每辆车所需时间
    aver_delay=aver_driver-time_nofill  #平均每辆车的延误
    print("{},{},{}".format(aver_driver,time_nofill,aver_delay))


i=integrate.quad(f,x_start,x_end)
aver_divertime(i[0]/60,though_time,TEST.all_car)

