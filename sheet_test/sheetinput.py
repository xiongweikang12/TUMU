import math
import os

import pandas as pd
import numpy as np
import xlrd as xd
import xlwt as xt
from itertools import accumulate
from functools import reduce
from draw_graph_package.draw_hitt_graph import *
from xlutils.copy import copy


#TODO 导入对应的sheet

data=xd.open_workbook('allpath/dir1/testwork.xls') #xlrd对象
new_data=copy(data)#将xlrd 对象转化为xlwt对象
tableli=data.sheets()[0]
nowcol=tableli.nrows+1 #全局变量当前写入行数
print(tableli.nrows)
namdot=[str(tableli.cell_value(1,i)) for i in range(1,tableli.nrows-2)]
titleHeadUpDown=['下行上客数','下行下客数目','车站','上行上客数','上行下客数']
titleHeadsiding=['下行','区间','上行']
titleHeadtime=['时段','客流分布系数','全日最大断面客流量','全日分时开行列车数','行车间隔(min)']
timeBlock=[[str(i)+':00' for i in range(5,24)][j]+'--'+[str(i)+':00' for i in range(5,24)][j+1] for j in range(len([str(i)+':00' for i in range(5,24)])-1)] #时段列表
peopleStringsnum=[0.18,0.45,1,0.73,0.49,0.52,0.57,0.52,0.55,0.59,0.65,0.71,0.92,0.70,0.35,0.25,0.21,0.16]

addlist=[200,224]


#索引8个一组
sheetdiff1=[i for i in range(8)]
sheetdiff2=[i for i in range(8,16)]
sheetdiff3=[i for i in range(16,24)]

def conputeSheet(sheetindex):
    """
    :param sheetindex: xls表的索引
    :return: 对应表获取的数据
    """
    table=data.sheets()[sheetindex]
    nrows=table.nrows #获得行数 去除第一行的作用
    # print(table.row_len(1)) #一行有效为16 去除标题走总计
    # print(data.sheet_names())
    alldata=[]
    for i in range(2,nrows-1):
        datacol=[]
        for j in range(1,nrows-2):
            datacol.append(table.cell_value(i,j))
        alldata.append((datacol))

    return alldata

def DataProcess(dataProcessed,numEveryone)->list:
    """
    :param dataProcessed: 等待处理的1数据
    :return:返回累计后的结果 各站上下车人数,各断面客流量
    """
    dataProcessed=list(map(lambda x:list(map(lambda i:i+numEveryone,x)),dataProcessed))
    for i in range(len(dataProcessed[0])):
        dataProcessed[i][i]=0
    # print(dataProcessed)


    def downUpfunction(): #下行上客
        sumArray=[]
        for i in range(len(dataProcessed[0])):
            if(len(dataProcessed[i][i+1:])==1):
                sumArray.append(dataProcessed[i][-1])
                # print(dataProcessed[i][-1])
            elif(len(dataProcessed[i][i+1:])==2):
                sumArray.append(dataProcessed[i][-2]+dataProcessed[i][-1])
                # print([dataProcessed[i][-2],dataProcessed[i][-1]])
            elif(len(dataProcessed[i][i+1:])==0):
                pass
            else:
                # sum+=reduce(lambda x,y:x+y,dataProcessed[i+1:-1])
                # print(dataProcessed[i][i+1:])
                sumArray.append(reduce(lambda x,y:x+y ,dataProcessed[i][i+1:]))
        sumArray.append(0)
        print(sumArray)
        return sumArray

    def upDown(): #上行下客
        sumArray=[0]
        for i in range(len(dataProcessed[0])):
            if(len(dataProcessed[i][:i])==1):
                sumArray.append(dataProcessed[i][0])
                # print(dataProcessed[i][-1])
            elif(len(dataProcessed[i][:i])==2):
                sumArray.append(dataProcessed[i][0]+dataProcessed[i][1])
                # print([dataProcessed[i][-2],dataProcessed[i][-1]])
            elif(len(dataProcessed[i][:i])==0):
                pass
            else:
                # sum+=reduce(lambda x,y:x+y,dataProcessed[i+1:-1])
                # print(dataProcessed[i][i+1:])
                sumArray.append(reduce(lambda x,y:x+y ,dataProcessed[i][:i]))
        print(sumArray)
        return sumArray


    def downdown():#下行下客
        sumArray = [0]
        for i in range(1,len(dataProcessed[0])):
            rowlist=[dataProcessed[j][i] for j in range(i)]
            if (len(rowlist) == 1):
                sumArray.append(rowlist[0])
                # print(dataProcessed[i][-1])
            elif (len(rowlist) == 2):
                sumArray.append(reduce(lambda x,y:x+y,rowlist))
                # print([dataProcessed[i][-2],dataProcessed[i][-1]])
            elif (len(rowlist) == 0):
                pass
            else:
                # sum+=reduce(lambda x,y:x+y,dataProcessed[i+1:-1])
                # print(dataProcessed[i][i+1:])
                sumArray.append(reduce(lambda x, y: x + y,rowlist))
        print(sumArray)
        return sumArray

    def upup():
        sumArray=[]
        for i in range(0,len(dataProcessed[0])):
            # print(i)
            rowlist = [dataProcessed[j][i] for j in range(i+1,len(dataProcessed[0]))]
            # print(rowlist)
            if (len(rowlist) == 1):
                sumArray.append(rowlist[0])
                # print(dataProcessed[i][-1])
            elif (len(rowlist) == 2):
                sumArray.append(reduce(lambda x, y: x + y, rowlist))
                # print([dataProcessed[i][-2],dataProcessed[i][-1]])
            elif (len(rowlist) == 0):
                pass
            else:
                # sum+=reduce(lambda x,y:x+y,dataProcessed[i+1:-1])
                # print(dataProcessed[i][i+1:])
                sumArray.append(reduce(lambda x, y: x + y, rowlist))
        sumArray.append(0)
        print(sumArray)

        return sumArray

    downUpnum=downUpfunction()
    Updownnum=upup()
    downdownnum=downdown()
    upupnum=upDown()
    downall = [downUpnum[i] - downdownnum[i] for i in range(len(downdownnum)-1)]
    upall = [Updownnum[i] -upupnum[i] for i in range(len(upupnum)-1)]
    print(downall)
    print(upall)
    return [downUpnum,downdownnum,upupnum,Updownnum],[list(accumulate(downall)),list(accumulate(upall))]

def arrayInsert(arrary:list,target):
    """
    :param arrary: 代插入的数组对象
    :param target: 插入的对象
    :return:null 引用类型改变原对象
    """
    InsertIndex=int(len(arrary)/2)
    arrary.insert(InsertIndex,target)


#TODO 将内容填写到xls文件中
# 继续下一步的运算

def show_picture(datalist,sheetIndex,isshow=False,lablex='区间站点',labley='各区间断面客流量',titlenoow='断面客流量'):
    print(data.sheet_names()[sheetIndex])
    str_path=[namdot[i]+'-'+namdot[i+1] for i in range(len(namdot)-1)]
    nowplt=draw_hitt_graph_signal(str_path,datalist,label_x=lablex,label_y=labley,title_=titlenoow+'({})'.format(data.sheet_names()[sheetIndex]),is_average=False)
    nowplt.xticks(rotation=45)
    # nowplt.show()
    return nowplt
    # 存到相应文件夹中




def sheet_writeIn(SheetIndex,DataInto,IntoHead,insertPart,Indexxls):
    #xls 写入
    global nowcol
    global new_data
    """
    :param SheetIndex: workspace sheet的索引
    :param DataInto: 写入数据 [[],[]]
    :param IntoHead: 数据头部标签
    :param insertPart 插入部分
    :return: nll
    """
    co_num=3 #数据间隔
    sheet=new_data.get_sheet(SheetIndex)
    nowcol+=co_num
    #写入标题
    for i in range(len(IntoHead)):
        sheet.write(nowcol,i+1,IntoHead[i])
    nowcol+=1
    #写入数据 行为列,列为行
    if (len(insertPart)==0):
        pass
    else:
        arrayInsert(DataInto,insertPart) #插入

    for i in range(len(DataInto)):
        for j in range(len(DataInto[0])):
            sheet.write(j+nowcol,i+1,DataInto[i][j])
    nowcol+=len(DataInto[0])
    new_data.save('allpath/dir{}/testkeep.xls'.format(Indexxls))




#TODO 文件保存图片&&xls
# 总文件夹对应只一个add数值
# 总文件夹中有子文件夹(每个子文件夹对应一个索引范围,
# 或每个对象都是指定的索引范围,
# 子文件夹里面有相应的xls,
# 每个sheet操作完产生对应的图片保存在其子文件夹路径下递增命名)

def start_(indexls,index,add):
    a = conputeSheet(sheetdiff1[index])
    c, d = DataProcess(a, add)
    # print(c, d)
    # print(len(c), len(d))
    lablex = '区间站点'
    labley = '各区间断面客流量'
    show_picture(d[0], sheetIndex=index).savefig('allpath/dir{}/上行{}.png'.format(indexls,index+1))
    show_picture(d[1], sheetIndex=index).savefig('allpath/dir{}/下行{}.png'.format(indexls,index+1))
    maxpeople=max(d[1])*0.1
    timePeople=list(map(lambda x:x*maxpeople,peopleStringsnum))

    def numadjust(num,index):
        if (math.ceil(num)<6 and 13<=index<=17):
            return 6
        elif(6<math.ceil(num)<10 and 13<=index<=17):
            return 10
        elif(math.ceil(num)<6 and index<=1):
            return 6
        else:
            return math.ceil(num)

    def timeget(num):
        lownum=math.floor(num)
        otherpath=num-lownum
        if (otherpath==0):
            return '{}min'.format(lownum)
        else:
            return '{}min{}s'.format(lownum,math.ceil(otherpath*60))




    carnum=[numadjust(j/(310*6),i) for i,j in enumerate(timePeople)]
    timeinterva=[timeget(60/i) for i in carnum]
    allinto=[timeBlock,peopleStringsnum,timePeople,carnum,timeinterva]
    print(allinto)



    sheet_writeIn(index, c, titleHeadUpDown, namdot,Indexxls=indexls)
    sheet_writeIn(index, d, titleHeadsiding, [namdot[i] + '-' + namdot[i + 1] for i in range(len(namdot) - 1)],Indexxls=indexls)
    sheet_writeIn(index,allinto,titleHeadtime,[],Indexxls=indexls)


for i,j in enumerate(os.listdir(r'D:\python\pythonProject4\sheet_test\allpath')):
    print(i,j)
    if(i==0):
        for k in range(8):
            start_(i+1,k,addlist[i])
            nowcol = tableli.nrows
        continue
    else:
        data = xd.open_workbook('allpath/{}/testwork.xls'.format(j))
        new_data = copy(data)  # 将xlrd 对象转化为xlwt对象
        tableli = data.sheets()[0]
        nowcol = tableli.nrows + 1  # 全局变量当前写入行数
        print(tableli.nrows)
        namdot = [str(tableli.cell_value(1, i)) for i in range(1, tableli.nrows - 2)]
        for k in range(8):
            start_(i+1,k,addlist[i])
            nowcol=tableli.nrows






