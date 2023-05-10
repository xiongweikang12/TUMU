import time

from class_transqusetion_mat import *
from trans_minElement import *


# TODO 供需线性规划(运输问题)

# 数据类型 MXN的矩阵,供需矩阵


"""
print(con_index(TestData.mat_test,[3,4],justity_mat1=TestData.mat_product_j
                ,justity_mat2=TestData.mat_retail_j))
                """
t1=time.time()
# 给定初始方案,最小元素法
print('yes')
print(all(TestData.mat_retail_j))
test_min_E= trans_minElement_getprimemat(TestData)

if __name__=="__main__":
    print(test_min_E)
    print(sum_accomplish(TestData.Element,TestData.mat_test,[3,4]))
    print(TestData.mat_test)
    print(vol_mat_check(TestData.Element,TestData.mat_test))
    print(have_need_iter(TestData.mat_test,vol_mat_check(TestData.Element,TestData.mat_test)))
    adjust_index_list=have_need_iter(TestData.mat_test,vol_mat_check(TestData.Element,TestData.mat_test))[-1][-1]
    adjust_boolean=have_need_iter(TestData.mat_test,vol_mat_check(TestData.Element,TestData.mat_test))[-1][0]
    print(adjust_boolean)
    print(adjust_index_list)
    t2=time.time()
    print(t2-t1)