from measure_error import *

print(measure_error.__doc__)

class Solve:
    def __init__(self):
        self.D_slove()
        self.H_slove()

    def D_slove(self):
        l=distance_error(10000)
        a=l.Error()
        print(a)

    def H_slove(self):
        k=Height_error(100)
        j=k.Error()
        print(j)

c=Solve()







