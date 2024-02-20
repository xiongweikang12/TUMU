from TUMU.experiment.experment_1.exper1 import lines_amount
from TUMU.experiment.experment_1.exper1 import draw_line
from draw_graph_package.draw_data_deal.draw_line_roation_90 import *
from functools import reduce
import matplotlib.pyplot as plt
import matplotlib


def normoal_draw_line1(list_str_x,list_y,label_x=" ",label_y=" ",title_=None):
    return draw_line(listx=list_str_x,listy=list_y,
                     labelx=label_x,labely=label_y,
                     title=title_)

"""

list1=[i for i in range(1,15)]
list2=[4,4,5,5,6,5,4,5,4,4,5,5,4,6]

a=normoal_draw_line2(list1,list2,add_average=True)
a.title("高峰时间段车辆停靠时间") #上午6点到10
a.ylabel("停靠时间:s")
a.xlabel("车趟数:辆")
a.show()

"""

def normoal_draw_line2(list_x,list_y,mode="ggplot",add_average=False,title=" ",xlabel="",ylabel=""):
    """
    :param list_x:
    :param list_y:
    :param mode: darkgrid ggplot
    :return:
    """
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    plt.style.use(mode)
    plt.plot(list_x,list_y)
    if add_average :
        plt.axhline(y=reduce(lambda x,y:x+y,list_y)/len(list_y), ls='--', c='blue')
    else:
        pass
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    return plt

    "风格不同"


def mult_draw_line(list_str_x,list_mult_y,mult_label,xlabel=None,ylabel=None,
                   title=None,rotation_x=None,rotation_y=None):

    if(all([isinstance(i,list) for i in list_mult_y])):
        return lines_amount(listlabelx=list_str_x,listyamount=list_mult_y,
                            LabelList=mult_label,xlabel=xlabel,
                            ylabel=ylabel,title=title,rotation_x=rotation_x,
                            rotation_y=rotation_y)
    else:
        raise Exception("list_mult_y is nesting list")

    """
    list3=["1", "2", "3"]
    list6=[[2, 3, 5], [2, 4, 6], [2, 4, 6]]
    k=mult_draw_line(list3,list6,['2','3','5'])
    k.show()
    """


def signal_draw_line(list_str_x,list_signal_y,mult_Label,xlabel=None,ylabel=None,
                   title=None,rotation_x=None,rotation_y=None):

    if isinstance(list_signal_y,list):
        return lines_amount(listlabelx=list_str_x,listyamount=[list_signal_y],
                            LabelList=mult_Label,xlabel=xlabel,
                            ylabel=ylabel,title=title,rotation_x=rotation_x,
                            rotation_y=rotation_y)
    else:
        raise Exception("list_signal_y just is a list")

"""
list3=["1", "2", "3"]
list6=[[2, 3, 5], [2, 4, 6], [2, 4, 6]]
k=signal_draw_line(list3,list6[0],['2','3','5'])
k.show()

"""



def draw_line_roattion_90(list_x,list_y,mode="ggplot",add_average=False,title=" ",xlabel="",ylabel=""):
    list_x,list_y=del_data(list_x,list_y)
    return normoal_draw_line2(list_x,list_y,mode=mode,add_average=add_average,title=title,xlabel=xlabel,ylabel=ylabel)




