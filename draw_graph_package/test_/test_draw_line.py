from draw_graph_package.draw_line_graph import *



#TODO 关于文件中各个函数的测试
# test_draw_line 测试 draw_line_graph

list1=[1,3,6,7]
list2=[2,4,5,8]

a=normoal_draw_line2(list1,list2,add_average=True)
a.xticks(list(range(10)),["坐标"+str(i) for i in range(10)])
a.show()

b=normoal_draw_line1(list1,list2,label_x="x",label_y="c")
b.show()


c=draw_line_roattion_90(list1,list2,add_average=True)
c.show()