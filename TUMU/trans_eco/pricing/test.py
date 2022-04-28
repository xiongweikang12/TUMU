# import math
#
# def solve(a,b,c):
#     p=math.pow(b,2)-(4*a*c)
#     solve_a=(-b+math.sqrt(p))/(2*a)
#     solve_b=(-b-math.sqrt(p))/(2*a)
#     print(solve_a,solve_b)
#
# a=1
# c=1500*330
# b=(-((2.5/((1+0.05)/(1-0.056))-1)))*1500
# solve(a,b)
import time


def deco(func):
    def wrapper():
        print('{}函数进来拉'.format(func()))
        print("函数")
    return 1

@deco #func=deco(func)
def func():
   print("hello")
   time.sleep(1)
   print("world")

a=func #a==1
print(a)