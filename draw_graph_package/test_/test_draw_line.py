from draw_graph_package.draw_line_graph import *
from draw_graph_package import draw_line_graph as dd_lg



#TODO 关于文件中各个函数的测试
# test_draw_line 测试 draw_line_graph

list1=[i for i in range(1,15)]
list2=[4,4,5,5,6,5,4,5,4,4,5,5,4,6]

#a=normoal_draw_line2(list1,list2,add_average=True)
#a.title("高峰时间段车辆停靠时间") #上午6点到10
#a.ylabel("停靠时间:s")
#a.xlabel("车趟数:辆")

#a.show()

# b=normoal_draw_line1(list1,list2,label_x="x",label_y="c")
#b.show()


c=dd_lg.draw_line_roattion_90(list1,list2,add_average=True)
c.show()
#车辆停靠时间
#车辆到达分布

"""
list3=["1", "2", "3"]
list6=[[2, 3, 5], [2, 4, 6], [2, 4, 6]]
k=signal_draw_line(list3,list6[0],['2','3','5'])
k.show()

"""


