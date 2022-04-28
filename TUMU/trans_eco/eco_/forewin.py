import tkinter as tk
import numpy as np
from know_all_exceptEl import foreWindow
import time


def fore_1(other_b, other_a,format_H):#传入模型的弹性系数，模型类型，常数a
    #TODO 下方为一个预测框的类
    win_forecast_price = foreWindow() #窗口对象
    #TODO 下面为两个按钮函数，计算参数根据不同的选择，其也是通过传参重复调用
    def fore_result1():  # 预测需求，要求其价格 #np,pp,pq,el
        input_getq = win_forecast_price.E_forecast.get()#获取entry文本
        if format_H == '线性':  # 预测需求newprice
            new_price = float(input_getq)  # 新价格
            new_need = (other_b * new_price) + other_a
            win_forecast_price.E_tell_result_forecast.insert('end', '预测需求为:{:.2f}\n'.format(new_need))
            win_forecast_price.E_tell_result_forecast.insert('end', '收益为:{:.2f}\n'.format(new_price * new_need))

        if format_H == '对数':  # 预测需求newprice
            new_price = float(input_getq)  # 新价格
            new_need = np.exp(other_b * np.log(new_price) + other_a)
            win_forecast_price.E_tell_result_forecast.insert('end', '预测需求为:{:.2f}\n'.format(new_need))
            win_forecast_price.E_tell_result_forecast.insert('end', '收益为:{:.2f}\n'.format(new_price * new_need))

    def fore_result2():  # 预测价格,要求需求
        input_getp = win_forecast_price.E_forecast.get()
        if format_H == '线性':
            new_need = float(input_getp)
            new_price = (new_need - other_a) / other_b
            win_forecast_price.E_tell_result_forecast.insert('end', '预测需求为:{:.2f}\n'.format(new_price))
            win_forecast_price.E_tell_result_forecast.insert('end', '收益为:{:.2f}\n'.format(new_price * new_need))
        if format_H == '对数':
            new_need = float(input_getp)
            new_price = np.exp((np.log(new_need) - other_a) / other_b)
            win_forecast_price.E_tell_result_forecast.insert('end', '预测需求为:{:.2f}\n'.format(new_price))
            win_forecast_price.E_tell_result_forecast.insert('end', '收益为:{:.2f}\n'.format(new_price * new_need))


    def quit_window():
        win_forecast_price.fore.destroy()

    RB_N = tk.Button(win_forecast_price.fore, text='需求', command=fore_result1)
    RB_N.place(x=70, y=30)
    RB_p = tk.Button(win_forecast_price.fore, text='价格/收入/其他', command=fore_result2)
    RB_p.place(x=120, y=30)
    B_Q = tk.Button(win_forecast_price.fore, text='退出', command=quit_window)
    B_Q.place(x=220, y=75)

    win_forecast_price.start_forecast()
    win_forecast_price.fore.mainloop()



#TODO 通过传入系数b,常数a,与预测的参考数
