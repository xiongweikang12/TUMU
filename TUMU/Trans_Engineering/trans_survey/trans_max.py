#TODO 以5min为调查交通高峰
import re

def Max_trans_phf(list1):
    max_value=max(list1)
    all_=sum(list1)
    phf=all_/(max_value*12)
    print(phf)

def str_into_list(string):
    str=string.split('\t')
    list2=[int(i) for i in str]
    return list2


if __name__=="__main__":
    # Max_trans_phf(str_into_list("63	71	70	76	93	95	131	128	62	67	102	118"))
    # Max_trans_phf(str_into_list("73	84	73	72	69	72	79	84	71	84	92	93"))
    # Max_trans_phf(str_into_list("85	56	97	123	140	123	119	123	141	148	83	166"))
    # Max_trans_phf(str_into_list("42	43	35	47	46	28	41	52	37	53	32	47"))
    print(re.findall("\d{2,3}","42	43	35	47	46	28	41	52	37	53	32	47"))