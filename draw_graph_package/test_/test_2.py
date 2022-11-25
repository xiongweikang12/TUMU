from draw_pie_graph import *

test_data_pie_1 = [152, 45]
test_data_pie_2 = [145, 70]

c = draw_pie_graph_list(have_data_exchange=False, list_=test_data_pie_1,
                         label=["交叉口信号延误", "停车站点上下客延误"],
                         title_name="延误时间比率(上行)")
c.show()

d = draw_pie_graph_list(have_data_exchange=False, list_=test_data_pie_2,
                         label=["交叉口信号延误", "停车站点上下客延误"],
                         title_name="延误时间比率(下行)")
d.show()

