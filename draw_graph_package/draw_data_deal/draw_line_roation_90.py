# TODO 处理折线图（90度过渡）时候

def del_data(test1, test_2):
    i = 0
    while True:
        try:
            if test1[i] == test1[i + 1]:
                i = i + 1
                continue
            if test_2[i] != test_2[i + 1]:
                temp_1 = test_2[i]
                temp_2 = test1[i + 1]
                test_2.insert(i + 1, temp_1)
                test1.insert(i + 1, temp_2)
                i = i + 1
        except IndexError:
            break

    return test1, test_2

"""
import matplotlib.pyplot as plt

test //
test_1 = [0,1, 2, 4,6]
test_22 = [4,5, 3, 4,3]
plt.plot(test_1, test_22)

a, b = del_data(test_1, test_22)
print([(a[i], b[i]) for i in range(len(a))])
plt.plot(a, b)
plt.show()

"""
