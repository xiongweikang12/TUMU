

#返回二维数组的索引
def con_index(mat1,mat_shape,justity_mat1,justity_mat2):
    """

    :param mat1:矩阵本身
    :param mat_shape: 矩阵大小 三行四列 [3,4]
    :param justity_mat1: 行索引产出
    :param justity_mat2: 列索引销量
    :return:
    寻找最小的元素的索引,最小元素并且要满足相关条件（justity_mat的逻辑与关系）
    """
    min_element=0
    min_index=[]
    flag=False
    for i in range(mat_shape[0]):
        for j in range(mat_shape[1]):
            if all([justity_mat2[j], justity_mat1[i]]):
                min_element=mat1[i][j]
                min_index=[i,j]
                flag=True
                break
            else:
                continue
        if flag:
            break
        else:
            continue

    #确定初始最小值（等待比较）

    for i in range(mat_shape[0]):
        for j in range(mat_shape[1]):
            # print(all([justity_mat2[j], justity_mat1[i]]))
            if all([justity_mat2[j], justity_mat1[i]]) and mat1[i][j]<=min_element:
                min_element=mat1[i][j]
                min_index=[i,j]
            else:
                continue
    return min_index

    #找到最小值，返回其索引



#判断多个数组结果都对
def justity_all(*args):
    temp=[]
    for i in args:
        temp.append(any(i))
    return all(temp)

#目标函数结果
def sum_accomplish(price_mat,num_mat,mat_shape):
    return_sum=0
    for i in range(mat_shape[0]):
        for j in range(mat_shape[1]):
            return_sum+=price_mat[i][j]*num_mat[i][j]
    return return_sum


#判断矩阵遍历完成
def is_over(row_list,col_list)->bool:
    """
    :param row_list: 行判断矩阵（一个维度） list
    :param col_list: 列判断矩阵（一个维度） list
    :return: bool
    row_list 所有元素是逻辑与关系
    col_list 所有元素都是逻辑与关系
    return -> row_list && col_list
    """

    #对行特殊处理
    row_list_check=False
    for i,j in enumerate(row_list):
        if i==0:
            continue
        else:
            if not j:
                row_list_check=False
                break
            else:
                row_list_check=True

    col_list_check=all(col_list)
    return all([row_list_check,col_list_check])



#判断所有元素
def is_big_zero(mat,func):
    """

    :param mat:
    :return:
    判断二维矩阵小于某个条件，且所有元素的逻辑关系为与，
    并返回boolean,不符合相关条件的索引列表[(1,3),(2,0)...]
    """
    is_ok=True
    False_index=[]
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if func(mat[i][j]):
                continue
            else:
                is_ok=False
                False_index.append((i,j))

    return is_ok, False_index
