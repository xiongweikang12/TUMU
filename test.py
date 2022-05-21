import numpy as np
import operator
dataSet=[[1, 1], [1, 2], [2, 1]]
minDistIndices=[1,0,1]

dict ={}
for i ,j in enumerate(minDistIndices):
    if dict.get(j):
        dict[j].append(dataSet[i])
    else:
        dict[j] =[dataSet[i]]


minDistIndisex=[min(enumerate(i),key=operator.itemgetter(1))[0] for i in dataSet]
print(minDistIndisex)

# print(dict)
# newCentrodis = [np.mean(np.array(i),0) for i in dict.values()]
# newCentrodis=[list(i) for i in newCentrodis]
# print(newCentrodis)
