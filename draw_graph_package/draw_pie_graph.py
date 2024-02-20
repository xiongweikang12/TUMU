from TUMU.experiment.experment_1.pie_search import draw_pie
from functools import reduce


#TODO 两个画圆饼图的函数

def draw_pie_graph_list(list_, label, exchange_sheet=None, title_name=None, model_is_summary=None, have_data_exchange=False):
    if have_data_exchange:
        pass
    else:
        exchange_sheet = [1 for _ in list_]

    return draw_pie(args_1=list_, sheet_exchange=exchange_sheet, label=label, titlename=title_name,
                    model_is_summary=model_is_summary)

"""
test_data_pie_1 = [152, 45]
c = draw_pie_graph_list(have_data_exchange=False, list_=test_data_pie_1,
label=["交叉口信号延误", "停车站点上下客延误"],title_name="延误时间比率(上行)")
c.show()
"""


def draw_pie_graph_list_(list_, label, exchange_sheet=None, title_name=None, model_is_summary=None, have_data_exchange=True,
                         list_is_nesting=True):


    if list_is_nesting:
        if all([isinstance(i, list) for i in list_]):
            container_list_new = [0] * len(list_)
            for j in range(len(container_list_new)):
                container_list_new[j] = reduce(lambda x, y: x + y, list_[j])

        else:
            raise Exception("the list is not nesting should_t call this function")
    else:
        raise Exception("please add one argument")


    if have_data_exchange:
        pass
    else:
        exchange_sheet = [1 for _ in list_]

    return draw_pie(args_1=container_list_new, sheet_exchange=exchange_sheet, label=label, titlename=title_name,
                    model_is_summary=model_is_summary)


