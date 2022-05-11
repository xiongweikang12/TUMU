import re
from exper1 import *
from itertools import chain


class TEST:

   str="aabeb ebaaa baeba ebcbc bbeba ddbab aeaab aecba edaea aaaba"
   str1="baaab bbbac aeaaa eaaaa bbeab aabba baeaa eacaa ecaab aaaba"
   str2="bcaaa acaaa caeaa aeeaa bbaaa deabe bacca aabca babab aaaaa"
   str3="aaaca acacb babab abaaa aeaba aacaa bbaaa baaaa deaba bacaa"

   car_l="11212 22221 12212 21121 12211 21222 12121 12121 21122 22212"
   car_l1="21211 11122 21122 21112 21211 12112 12221 22111 22111 11222"
   car_l2="12212 12221 22212 22222 22122 12222 21121 21222 21212 122222"
   car_l3="12122 22122 21222 21222 11222 22222 21121 11111 11111 111111"

   listv_=[27,29,29,23,23,37,20,25,34,39,42,35,32,29,35,34,41,37,43,41,36,51,37,36,38,38,31,36,45,43,37,34,44,42,38,35,28,36,33,40,40,30,41,38,35,42,38,31,49,32]
   listv1=[37,41,36,31,35,36,40,36,42,26,31,32,45,32,34,41,28,23,42,32,32,34,45,56,38,40,44,42,47,44,29,40,28,21,38,36,28,26,34,48,28,28,30,37,35,48,40,30,28,37]
   list_n=listv_+listv1
   listv2=[46,31,45,28,29,50,42,41,24,36,30,35,34,38,42,38,36,38,37,48,54,43,64,33,34,45,29,42,54,27,42,48,40,34,48,40,34,46,40,36,34,35,27,41,39,54,34,42,37,33]
   listv3=[53,50,42,46,23,50,40,42,33,39,43,30,42,39,52,49,46,35,56,52,40,30,28,39,35,29,43,44,34,31,40,25,33,51,27,29,40,32,48,39,31,28,35,40,29,34,45,40,33,48]
   list_s=listv2+listv3

   strn = str.strip() + str1.strip()
   strs = str2.strip() + str3.strip()
   car_ln = car_l.replace(' ','')+car_l1.replace(' ','')
   car_ls = car_l2.replace(' ','')+car_l3.replace(' ','')

   str_p="abaaa abaaa baaae dbeab aaaab eeabd bcbab ebacd aaaaa eaaba"
   str_p_1="baaea aaaab acaba abaaca aabab caeaa eaaea aaaea abaaa abcac"
   str_p_2="caaee aaaab aaaed abaaa aaba abbaa abaea aaaba adaaa cabcac"
   str_p_3="accea aaaea aaaaa abc abeba aabce aabda abaab aaaac eaaaeaa"

   car_l_p="11211 11111 11211 12212 12111 12111 211112 11211 22212 1211".replace(' ','')
   car_l_p1="22222 22222 22222 22222 22222 22211 11111 11111 11111 11111".replace(' ','')
   car_l_p2="11111 11111 11111 11111 1111 11111 11111 11111 11111 111111".replace(' ','')
   car_l_p3="22222 22222 22222 222 22222 22222 22222 22222 22222".replace(' ','')

   lists=[1.78,2.26,2.27,4.03,2.37,2.13,2.37,1.67,3.11,2.54,2.25,1.88,3.10,2.40,2.85,3.26,2.54,2.16,2.95,3.99,1.88,2.2,2.35,1.9,2.9,2.93,2.13,2.36,2.57,4.4,2.19,2.29,3.74,1.94,2.29,2.68,2.77,2.19,3.08,2.58,2.87,2.44,3,2.57,3.2,3.09,2.7,2.26,2.5,2.5,2.5,2.5]
   lists1=[1.7,2.7,3.68,2.94,2.53,2.95,3.33,2.40,2.54,2.71,3.06,2.45,1.72,1.99,2.37,2.0,1.97,1.23,1.46,2.16,2.29,2.65,2.08,1.84,2.87,1.46,3.24,3.24,1.84,2.17,2.62,3.16,3.64,2.23,2.85,3.39,2.24,3.24,4.05,2.45,2.37,2.13,2.35,3.23,3.73,2.79,1.81,1.78,2.78]
   lists2=[2.33,2.19,3.56,2.76,2.65,2.75,2.29,2.26,2.53,2.91,2.56,2.61,3.33,2.85,3.81,2.96,3.11,2.85,2.17,3.6,2.89,2.28,1.92,2.24,1.91,2.24,2.59,3.34,2.16,2.67,3.54,2.62,3.51,2.08,1.78,3.07,2.67,3.21,2.78,3.26,3.46,2.02,2.75,2.97,2.17,3.9,3.29,2.28,2.48]
   lists3=[4.5,2.53,3.15,1.99,1.97,2.65,2.69,2.78,2.58,3.48,1.88,2.11,2.81,3.12,2.5,4.35,4.25,3.24,1.99,3.12,4.32,2.56,2.26,3.21,2.56,2.26,3.21,2.5,1.94,3.46,1.96,2.24,3.87,4.50,3.50,2.53,1.89,3.3,2.24,1.95,1.54,2.63,2.64,1.96,2.25,2.77,1.94,1.65,1.79,3.47,2.28]

   listsv=s_to_v(25,lists)
   listsv1=s_to_v(25,lists1)
   listsv2=s_to_v(25,lists2)
   listsv3=s_to_v(25,lists3)
   listsv_n=listsv+listsv1
   listsv_s=listsv2+listsv3


   str_p_n=str_p+str_p_1
   str_p_s=str_p_2+str_p_3
   car_p_n=car_l_p.replace(' ','')+car_l_p1.replace(' ','')
   car_p_s=car_l_p2.replace(' ','')+car_l3.replace(' ','')



def exchange(string:str)->list[str]:

   #将字母内容替换成相应的文字,并生成列表
   str=re.sub("a","小汽车,",string)
   str=re.sub("b",'中型车,',str)
   str=re.sub("c",'大型车,',str)
   str=re.sub("d",'货车,',str)
   str=re.sub("e",'公交车,',str)
   str=str.split(',')
   str.pop(-1)
   return str

def to_list(string:str)->list[str]:
   #将字符串转换成列表list
   return [i for i in string]

def bulid_dict(list1,list2)->list:
   container=[]
   for i in range(len(list1)):
      dict={}
      dict[list1[i]]=list2[i]
      container.append(dict)
   return container

def bulid_dict1(list1:[str],list2:[float],list3:[str])->[{str:(float,str)}]:
   #创建车型:(速度,车道字符串)
   containter=[]
   for i in range(len(list1)):
      dict={}
      dict[list1[i]]=(list2[i],list3[i])
      containter.append(dict)
   return containter

def fittler_car_road(dict1:[{str:(float,str)}]):
   #通过车型筛选出不同车型的,车道与速度关系
   def fittler_part(car)->list[(float,str)]:
      a=return_car(dict1)
      car_tuple=a(car)# car:表示车种 return->(float,str)
      road_1=len(list(filter(lambda x:x[1]=='1',car_tuple)))
      road_2=len(list(filter(lambda x:x[1]=='2',car_tuple)))
      return road_1,road_2
   return fittler_part






#TODO 计算总车辆分布
car_nums_n=exchange(TEST.strn)
car_nums_np=exchange(TEST.str_p_n)#人工
car_nums_s=exchange(TEST.strs)
car_nums_sp=exchange(TEST.str_p_s)
car_all=car_nums_n+car_nums_s+car_nums_np+car_nums_sp
road_car=TEST.car_ln+TEST.car_ls+TEST.car_p_n+TEST.car_p_s
road_car=to_list(road_car)
road_car.pop(-1)
road_car.pop(-2)
print(road_car)
print(car_all)

print(len(car_all),len(road_car))
list_vn=TEST.list_n
list_vnp=TEST.listsv_n
list_vs=TEST.list_s
list_vsp=TEST.listsv_s
list_vall=list_vn+list_vs+list_vnp+list_vsp
list_vall_j=list_vn+list_vs #机器速度
list_vall_p=list_vnp+list_vsp #人工机器
road_car_j=TEST.car_ln+TEST.car_ls
road_car_p=TEST.car_p_n+TEST.car_p_s
road_car_j=to_list(road_car_j)
road_car_p=to_list(road_car_p)
road_car_j.pop(-1)
road_car_j.pop(-1)
print(list_vall)
print(len(list_vall_j),len(road_car_j))
print(len(list_vall_p),len(road_car_p))
dict_all=bulid_dict1(car_all,list_vall,road_car)
# dict_all_j=bulid_dict1()
print(dict_all)
k=fittler_car_road(dict_all)
container=[]
for i in ["小汽车", "中型车", "大型车", "货车", '公交车']:
   a,b=k(i)
   container.append((a,b))

# car_nums=bulid_dict(car_nums,list_v)
# car=return_car(car_nums)
# min_car=car('小汽车')
# midlle_car=('中型车')
# dig_car=car('大型车')
# trade_car=car('货车')
# bus_car=car('公交车')
# container=[len(min_car),len(midlle_car),len(dig_car),len(trade_car),len(bus_car)]
# a=draw_pie(*container)
# a.show()
list_cars=list(chain.from_iterable(container))
list_road=[1,2]*5
label=["小汽车", "中型车", "大型车", "货车", '公交车']
con_l=[0]*len(label)*2
col=[label[i//2] for i in range(len(label)*2)]
# draw_hitt(list_cars,list_road,col)

print(len(car_nums_n),len(list_vn))
print(len(car_nums_np),len(list_vnp))
print(len(car_nums_s),len(list_vs))
print(len(car_nums_sp),len(list_vsp))
#人工n-1，机器s-1 人工s+1
dict_n=bulid_dict(car_nums_n,list_vn)
dict_s=bulid_dict(car_nums_s,list_vs)
dict_np=bulid_dict(car_nums_np,list_vnp)
dict_sp=bulid_dict(car_nums_sp,list_vsp)

a=staright_draw(return_args(dict_s),return_args(dict_sp),'南向各车型的速度分布')
a.show()

#将速度排序
# dict_all=sorted(dict_all,key=lambda x:list(x.values())[0][0])
list_vall_p.sort()
list_vall_j.sort()
max_1=list_vall_p[-1]
max_2=list_vall_j[-1]
kk=draw_line(*return_w(list_vall_j))
kk.show()

# print(len(car_nums_n),len(list_vn))
# print(len(car_nums_np),len(list_vnp))
# print(len(car_nums_s),len(list_vs))
# print(len(car_nums_sp),len(list_vsp))
# #人工n-1，机器s-1 人工s+1
# dict_n=bulid_dict(car_nums_n,list_vn)
# dict_s=bulid_dict(car_nums_s,list_vs)
# dict_np=bulid_dict(car_nums_np,list_vnp)
# dict_sp=bulid_dict(car_nums_sp,list_vsp)
#
# a=staright_draw(return_args(dict_s),return_args(dict_sp),'北向各车型的速度分布')
# a.show()
#








































# # car_nums_N=bulid_dict(car_nums_n,list_vn)
# #
# # car=return_car(car_nums_N)
# # min_car=car('小汽车')
# # midlle_car=('中型车')
# # dig_car=car('大型车')
# # trade_car=car('货车')
# # bus_car=car('公交车')
# # container=[len(min_car),len(midlle_car),len(dig_car),len(trade_car),len(bus_car)]
# # a=draw_pie(*container)
# # a.show()
#
# car_nums_S=bulid_dict(car_nums_s,list_vs)
# car=return_car(car_nums_S)
# min_car=car('小汽车')
# midlle_car=('中型车')
# dig_car=car('大型车')
# trade_car=car('货车')
# bus_car=car('公交车')
# container=[len(min_car),len(midlle_car),len(dig_car),len(trade_car),len(bus_car)]
# a=draw_pie(*container)
# a.show()
#



