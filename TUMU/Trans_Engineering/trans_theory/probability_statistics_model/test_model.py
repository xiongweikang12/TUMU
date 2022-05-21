from diff_distribution import *
from functools import reduce
m=7.469

list1=[(3,3),(4,0),(5,8),(6,10),(7,11),(8,10),(9,11),(10,9),(11,1),(12,1)]
l=BOsong(True,True,4,list1)
l1=TwinItem(True,list1,True,4)
m1=Choice_model(l)
m2=Choice_model(l1)
print(m1)
print(m2)
l1.show_content()
print(l1.counter_proable('<='))

# k=math.factorial(16)/(math.factorial(4)*math.factorial(12))
# k=k*math.pow(0.46,4)*math.pow(0.54,12)
# print(k)
list2=[(0,1),(1,7),(2,10),(3,12),(4,12),(5,15),(6,13),(7,10),(8,10),(9,6),(10,3),(11,1)]
l2=BOsong(True,True,10,list2)
m3=Choice_model(l2)
print(m3)
print(l2.counter_proable('>'))
