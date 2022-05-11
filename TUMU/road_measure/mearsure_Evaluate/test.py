from measure_Evaluate import *

class Slove:

    def __init__(self):
        self.power_Slove()
        self.aver_Slove()

    def power_Slove(self):
        """
        #加权，非等精度的
        """
        H = [48.421, 48.350, 48.392]
        L = [14.2, 10.9, 12.6]
        list_p = list(map(lambda x: 10 / x, L))

        a = Power_Evaluate(list_p, H, L)
        c, d = a.average_Error('H', 'H')
        print(c, d)

    def aver_Slove(self):
        """
        #等精度距离测量
        """
        L1 = (251.52, 251.46, 251.49, 251.48, 251.50)
        j = Average_Evaluate(*L1)
        f, l = j.average_Error()()
        print(f, l)


l=Slove()