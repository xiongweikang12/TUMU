# TODO 获取弹性（价格弹性）
import numpy as np

# np.seterr(divide='ignore',invalid='ignore')


class MoneyElasticity():

    def __init__(self, nowneed, nowmoney, pastneed, pastmoney, H_format):
        #TODO 对计算弹性的类初始化，通过外部传参
        self.nowneed = nowneed
        self.nowmoney = nowmoney
        self.pastmoney = pastmoney
        self.pastneed = pastneed
        self.H_formart = H_format


    # def what_type(self):
    #
    #     if self.H_formart=='线性':
    #         return True
    #     if self.H_formart=='对数':
    #         return False
    #
    def get_price_elasticity(self):

        #TODO 计算各个参数，并通过判断模型返回不同的参数
        self.elasticity = (self.nowneed - self.pastneed) / (self.nowmoney - self.pastmoney)#弹性系数
        self.point_elasticity_lingo = self.elasticity * (self.pastmoney / self.pastneed)
        #点弹性，对于不同模型来说意义是不同的，对于线性是可变的，对于对数就是等值于弹性系数
        self.point_elasticity_log =(np.log(self.nowneed)-np.log(self.pastneed))/(np.log(self.nowmoney)-np.log(self.pastmoney))
        self.other_number_lingo = self.nowneed - (self.elasticity * self.nowmoney)
        #对于，不同模型的常数值
        self.other_number_log = (np.log(self.nowneed) - self.point_elasticity_log * (np.log(self.nowmoney)))
        # self.pro_money=(self.nowmoney-self.pastmoney)/self.pastmoney
        # self.pro_need=(self.nowneed-self.pastneed)/self.pastneed
        if self.H_formart == '线性':
            return self.point_elasticity_lingo, self.other_number_lingo,self.elasticity
        if self.H_formart == '对数':
            return self.point_elasticity_log, self.other_number_log,self.point_elasticity_log


# TODO 获取弹性（收入弹性）
class IncomeElasticity:

    def __init__(self, nowneed, nowincome, pastneed, pastincom, H_formart):
        self.H_formart = H_formart
        self.nowneed = nowneed
        self.nowincome = nowincome
        self.pastneed = pastneed
        self.pastincome = pastincom

    def get_income_elasticity(self):

        self.elasticity = (self.nowneed - self.pastneed) / (self.nowincome - self.pastincome)
        self.point_elasticity_lingo = self.elasticity * (self.pastincome / self.pastneed)
        self.point_elasticity_log = (np.log(self.nowneed)-np.log(self.pastneed))/(np.log(self.nowincome)-np.log(self.pastincome))
        self.other_number_lingo = self.nowneed - (self.elasticity * self.nowincome)
        self.other_number_log = (np.log(self.nowneed) - self.elasticity * (np.log(self.nowincome)))

        if self.H_formart == '线性':
            return self.point_elasticity_lingo, self.other_number_lingo,self.elasticity
        if self.H_formart == '对数':
            return self.point_elasticity_log, self.other_number_log,self.point_elasticity_log


# TODO 获取弹性（交叉弹性）
class CrossPriceElasticity:

    def __init__(self, needone, priceone, needtwo, pricetwo, H_formart):  # 两个需求，两个价格

        self.H_formart = H_formart
        self.needone = needone
        self.needtwo = needtwo
        self.priceone = priceone
        self.pricetwo = pricetwo

    def get_CrossPrice_Elastictiy(self):

        self.elasticity = (self.needone - self.needtwo) / (self.priceone - self.pricetwo)
        self.point_elasticity_lingo = self.elasticity * (self.pricetwo / self.needtwo)
        self.point_elasticity_log = (np.log(self.needone)-np.log(self.needtwo))/(np.log(self.priceone)-np.log(self.pricetwo))
        self.other_number_lingo = self.needone - (self.elasticity * self.priceone)
        self.other_number_log = (np.log(self.needone) - self.point_elasticity_log * (np.log(self.priceone)))

        if self.H_formart == '线性':
            return self.point_elasticity_lingo, self.other_number_lingo,self.elasticity
        if self.H_formart == '对数':
            return self.point_elasticity_log, self.other_number_log,self.point_elasticity_log
