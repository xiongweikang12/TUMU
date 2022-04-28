from TUMU.Trans_Engineering.trans_theory.probability_statistics_model.diff_distribution import *


list1=[(0,94),(1,63),(2,21),(3,2),(3,0)]
l=BOsong(True,True,11,list1)


# def show_doc(string_):
#     def show_deco(func):
#         def warapper():
#             print("面向对象装饰器")
#             print(string_)
#             func()
#
#         return warapper
#
#     return show_deco
#
#
# @staticmethod
# @show_doc("算法")
# def show1():
#     pass

#TODO 初级调用
# deco=l.show_doc()#返回一个装饰器   test=deco(test) 装饰器原理，外部装饰器而不用@,初级调用
# 此处的l.show_doc() 对于方法来说，self,l是一个待传入的参数
# l.show1=deco(l.show1)#返回内部函数，wrapper,闭包
# l.show1()

#TODO 中级调用
# l.show1=l.show_doc()(l.show1) #升级调用省去 l.show_doc() 返回装饰器的过程，直接test1传参调用返回内部函数，l.show()调用
# l.show1()

#TODO 装饰器调用
print(l.counter_proable('>'))
#需要将show1()加上静态装饰，第一层，@show_doc("算法") 返回一个装饰器,进行操作，self.show1=deco(show1)
#这时需将方法设置为静态，防止self传入deco中成为deco(self,func),就是要让self失效





l.set_k=2
l.set_k=11
