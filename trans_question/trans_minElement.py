from something_deal import *
import numpy as np


def trans_minElement_getprimemat(TestData1):
    """
    :param TestData1: 类实例
    :return: 基本初始解
    """

    while any([any(TestData1.mat_product_j), any(TestData1.mat_retail_j)]):

        min_index = con_index(TestData1.mat_test, [3, 4], justity_mat1=TestData1.mat_product_j,
                              justity_mat2=TestData1.mat_retail_j)

        # 比较供给大小
        if TestData1.mat_product[min_index[0]] < TestData1.mat_retail[min_index[1]]:
            TestData1.mat_product_j[min_index[0]] = False
            TestData1.mat_retail[min_index[1]] -= TestData1.mat_product[min_index[0]]
            # TestData.mat_product[min_index[0]] -= TestData.mat_product[min_index[0]]
            TestData1.Element[min_index[0], min_index[1]] = TestData1.mat_product[min_index[0]]
        elif TestData1.mat_product[min_index[0]] > TestData1.mat_retail[min_index[1]]:
            TestData1.mat_retail_j[min_index[1]] = False
            # TestData.mat_retail[min_index[1]] -= TestData.mat_retail[min_index[1]]
            TestData1.mat_product[min_index[0]] -= TestData1.mat_retail[min_index[1]]
            TestData1.Element[min_index[0], min_index[1]] = TestData1.mat_retail[min_index[1]]
        else:
            TestData1.mat_product_j[min_index[0]] = False
            TestData1.mat_retail_j[min_index[1]] = False
            # TestData.mat_retail[min_index[1]] = 0
            # TestData.mat_product[min_index[0]] = 0
            TestData1.Element[min_index[0], min_index[1]] = TestData1.mat_retail[min_index[1]]

    return TestData1.Element


def vol_mat_check(init_Element, prime_mat):
    """

    :param init_Element: 初始基解
    :param prime_mat: 初始目标方案
    # :param row_: 0 行位势
    # :param vol_mat:
    :return:
    """
    flag = 0
    col_list = [0] * init_Element.shape[1]  # 列
    row_list = [0] * init_Element.shape[0]  # 行
    col_list_check = [False for _ in col_list]
    row_list_check = [False for _ in row_list]
    row_list_check[0] = True
    while not is_over(row_list_check, col_list_check):
        for i in range(init_Element.shape[0]):
            for j in range(init_Element.shape[1]):
                if init_Element[i][j] == 0:
                    continue
                else:
                    if any([row_list_check[i], col_list_check[j]]) or i == 0:
                        if not row_list_check[i] and i != 0 and flag == 0:
                            row_list[i] = prime_mat[i][j] - col_list[j]
                            row_list_check[i] = True
                        elif not row_list_check[i] or (i == 0 and flag == 0):
                            col_list[j] = prime_mat[i][j]
                            col_list_check[j] = True
                        else:
                            col_list[j] = prime_mat[i][j] - row_list[i]
                            col_list_check[j] = True

                    else:
                        continue
        flag = flag + 1

    # return [col_list,row_list]

    # 计算检验表
    vol_mat_return = np.zeros((init_Element.shape[0], init_Element.shape[1]))
    for i in range(init_Element.shape[0]):
        for j in range(init_Element.shape[1]):
            vol_mat_return[i][j] = row_list[i] + col_list[j]

    return vol_mat_return


def have_need_iter(prime_mat, vol_mat_1):
    return prime_mat - vol_mat_1, is_big_zero(prime_mat - vol_mat_1,func=lambda x:x>=0)


# 初始可行解的修改,闭回路
def change_prime(get_index_list, vol_mat_checkout, prime_mat):
    """
    :param get_index_list: 待调整的索引列表 这里假设只有一个【】
    :param vol_mat_checkout: 检验数表
    :param prime_mat: 初始方案表
    :return:
    """
    row_limit = [0, prime_mat.shape[0] - 1]
    col_limit = [0, prime_mat.shape[1] - 1]
    container_road_path = []
    flag = 1

    def search_road(index):
        if vol_mat_checkout[index[0]][index[1]] == 0:
            pass

        if all([index[0] < row_limit[0], index[0] > row_limit[1], index[1] < col_limit[0], index[1] > col_limit[1]]):
            search_road([index[0] - 1, index[1]])
            search_road([index[0] + 1, index[1]])
            search_road([index[0], index[1] - 1])
            search_road([index[0], index[1] - 1])

    search_road(index=get_index_list[0])

    # 动态规划处理
