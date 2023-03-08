arr=[[1,2],[3,5]]

def arrayInsert(arrary:list,target):
    InsertIndex=int(len(arrary)/2)
    arrary.insert(InsertIndex,target)

arrayInsert(arr,[1,5])
print(arr)