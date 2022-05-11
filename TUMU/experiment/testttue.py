dict={'class':(1,2)}
print(list(dict.values())[0])
str='20.3'
print(str[0:2]+'%')
container=[2,4,6,8,10,2]
container_1 = [i for i in container if i == 2]
print(container_1)
dict11={(0,20):"<20",(20,30):"20~30",(30,40):"30~40",(40,50):"40~50",(50,60):"50~60",(60,200):">60"}
#根据范围定制,
list1=[10,20,40]
print([0]+[1,2,3])
def test(*args):
    print(args)

test(1,5,4,6)


