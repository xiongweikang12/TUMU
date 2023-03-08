arr=[[1,2],[3,5]]

def arrayInsert(arrary:list,target):
    InsertIndex=int(len(arrary)/2)
    arrary.insert(InsertIndex,target)

arrayInsert(arr,[1,5])
print(arr)
a='({})'.format(11)






timeBlock=[[str(i)+':00' for i in range(5,24)][j]+'--'+[str(i)+':00' for i in range(5,24)][j+1] for j in range(len([str(i)+':00' for i in range(5,24)])-1)]





print(timeBlock)
print(a)

for i,j in enumerate([1,2,3]):
    print(i,j)
