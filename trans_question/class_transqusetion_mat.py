import numpy as np



class TestData:
    mat_test = np.array([[300, 1100, 300, 1000],
                         [100, 900, 200, 800],
                         [700, 400, 1000, 500]])
    mat_test_orgin = mat_test
    mat_product = [7, 4, 9]
    mat_retail = [3, 6, 5, 6]
    mat_product_j = [True for i in mat_product]
    mat_retail_j = [True for j in mat_retail]
    shape = mat_test_orgin.shape
    Element=np.zeros((shape[0],shape[1]))  #初始基本解矩阵
    vol_mat=np.zeros((shape[0],shape[1]))  #最优解判定矩阵





