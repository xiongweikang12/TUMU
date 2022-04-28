#TODO 验证类中方法互相调用的可行性

class Get_v:

    def __init__(self,v,s):
        self.v=v
        self.s=s
        self.t=self.s/self.v

    def print_content(self,content):
        print(content)

    def show_time(self):
        if float(self.v)>20 and float(self.s)>200:
            Get_v(self.v,self.s).print_content(self.t) #调用自己的方法



a=Get_v(25,400)
a.show_time()