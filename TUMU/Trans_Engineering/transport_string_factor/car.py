#TODO 创建一个car的类
import tkinter as tk
import numpy as np

class car:

    def __init__(self,vf,kj,*args):#畅通速度，阻塞密度,车头时距，车头间距 args为tuple

        self.vf=vf
        self.kj=kj

        if args:
            self.ht = args[0]
            self.hd = args[1]
            self.Q = 3600 / self.ht
        else:
            pass

class relationship_Q_K:

    def __init__(self,obj1):
        self.vf=obj1.vf
        self.kj=obj1.kj

    def V_Q(self,v):
        self.q=v*(self.kj-v*(self.kj/self.vf))
        return self.q

    def V_Q_lim(self,lim):
        self.vm=self.vf/2
        self.km=self.kj/2
        self.qm=self.vm*self.km
        self.max=0

        x1=((-(self.kj))+np.sqrt((self.kj**2)+4*(self.kj/self.vf)*(lim*self.qm)))\
           /-2*(self.kj/self.vf)
        x2=((-(self.kj))-np.sqrt((self.kj**2)+4*(self.kj/self.vf)*(lim*self.qm)))\
           /-2*(self.kj/self.vf)


        if (x1>x2):
            self.max=x1
        else:
            self.max=x2

        return self.max



