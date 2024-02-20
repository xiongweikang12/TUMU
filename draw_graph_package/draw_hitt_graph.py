from TUMU.experiment.experment_1.exper1 import draw_hitt
from functools import reduce

#TODO 创建
def draw_hitt_graph_signal(list_str,list_data,label_x,label_y,is_average,title_=''):
    """
    :param title_: 标题
    :param list_str: list 的 x
    :param list_data: list 的 data_y
    :param label_x: x的标签
    :param label_y: y的标签
    :param is_average: 取平均值
    :return:
    """

    global average_
    average_=0

    if is_average:
        average_=reduce(lambda x,y:x+y,list_data)/len(list_data)
    else:
        pass

    return draw_hitt(list1=list_str,list2=list_data,
                     labelx=label_x,labely=label_y,
                     choose_method=False,average=average_,
                     isaverage=is_average,title=title_)

"""

draw_hitt_graph.draw_hitt_graph_signal(test_str,test_num,title_='平均排队延误',label_y='延误时间/s',label_x='路口',is_average=False)
    a.xticks(rotation=90)
    a.show()

"""




def draw_hitt_graph_classify(list_str,list_data,list_class,class_type,label_x,label_y,is_average,title_):

    global average_

    if is_average:
        average_ = reduce(lambda x, y: x + y, list_data) / len(list_data)
    else:
        pass

    return draw_hitt(list1=list_str, list2=list_data,list3=list_class,
                     labelx=label_x, labely=label_y,hue1=class_type,
                     choose_method=True, average=average_,
                     isaverage=is_average, title=title_)

"""

class Examtine3:
    diff_person = ['c', 'x', 'c', 'x']
    diff_propose = [0.6, 0.5, 0.3, 0.5]
    time = ['2点', '2点', '3点', '3点']
    
draw_hitt_graph_classify(Examtine3.diff_person, Examtine3.diff_propose, Examtine3.time, class_type='不同时间段', label_x='不同群体',
                  label_y='出行占比',
                  title_='不同群体的出行时间段构成比例图',is_average=True)

"""