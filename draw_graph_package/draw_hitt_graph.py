from TUMU.experiment.experment_1.exper1 import draw_hitt
from functools import reduce

#TODO 创建
def draw_hitt_graph_signal(list_str,list_data,label_x,label_y,is_average,title_=None):
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

    if is_average:
        average_=reduce(lambda x,y:x+y,list_data)/len(list_data)
    else:
        pass

    return draw_hitt(list1=list_str,list2=list_data,
                     labelx=label_x,labely=label_y,
                     choose_method=False,average=average_,
                     isaverage=is_average,title=title_)





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
