from TUMU.experiment.experment_1.exper1 import lines_amount
from draw_graph_package.draw_line_graph import *
test_str1="""
17:21:00
17:29:00
17:39:00
17:49:00
"""
test_str2="""
16:22:00
16:33:00
16:46:00
16:57:00
17:07:00
17:18:00
17:28:00
17:39:00
17:49:00
18:00:00
"""

test_str3="""
16:51:00
17:17:00
17:41:00
"""

test_str4="""
16:23:00
16:26:00
16:38:00
16:51:00
16:55:00
17:06:00
17:17:00
17:26:00
17:31:00
17:34:00
17:40:00
17:50:00
18:00:00
"""
test_str5="""
16:32:00
16:46:00
17:45:00
17:58:00
"""

test_str6="""
16:31:00
16:49:00
16:58:00
17:00:00
17:11:00
"""

test_str7="""
16:31:00
16:41:00
16:52:00
17:01:00
17:18:00
17:22:00
17:31:00
17:41:00
17:51:00
"""

test_union="""
16:22:00
16:32:00
16:41:00
16:51:00
16:55:00
16:57:00
17:01:00
17:06:00
17:11:00
17:21:00
17:26:00
17:41:00
17:49:00
18:00:00
"""



def string_list(str1:str):
    return str1.split('\n')[1:-1]



#各个线到达的车数 只有 0 1

Label_str = ["高新路东大路（南到北）", "高新路东大路（北到南）"] #以下午的高峰时间，各个线的列车

# a = lines_amount(listlabelx=test_str, listyamount=test_data, LabelList=Label_str, xlabel="", ylabel="公交车到达量",
#                 rotation_x=30
#                 , title="一小时公交车到站量")
# a.show()

var_list=[test_str1,test_str2,test_str3,test_str4,test_str5,test_str6,test_str7]
var_container=[]
for i in var_list:
    i=string_list(i)
    var_container.append(i)

print(var_container)
test_str1,test_str2,test_str3,test_str4,test_str5,test_str6,test_str7=var_container
test_union=string_list(test_union)
def return_get(list1):
    containter=[0]*len(test_union)
    for i,j in enumerate(test_union):
        if(j in list1):
            containter[i]=1


    return containter
test_str1=return_get(test_str1)
test_str2=return_get(test_str2)
test_str3=return_get(test_str3)
test_str4=return_get(test_str4)
test_str5=return_get(test_str5)
test_str6=return_get(test_str6)
test_str7=return_get(test_str7)

Label_str = ["503", "531","602","636","664","668","D4"] #以下午的高峰时间，各个线的列车
test_str=test_union
test_data=[test_str1,test_str2,test_str3,test_str4,test_str5,test_str6,test_str7]
a = lines_amount(listlabelx=test_str, listyamount=test_data, LabelList=Label_str, xlabel="到达时间", ylabel="公交车到达量",
                rotation_x=90
                 , title="高峰期车辆到达分布情况")
a.show()