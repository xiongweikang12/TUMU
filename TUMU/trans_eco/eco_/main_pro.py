
import tkinter as tk
from know_all_exceptEl import window_exceptEL
from eco_con import MoneyElasticity
from eco_con import IncomeElasticity
from eco_con import CrossPriceElasticity
from window_choice import MainWindow
import numpy as np
from tk_filedialog import start_all
import time
from forewin import fore_1

#TODO 最初的菜单框
mainwin = MainWindow()

#TODO 单位大小对预测的影响巨大

# TODO 回归分析
def GDP_n_function():
    start_all()


# TODO 预测需求/价格部分，并入的弹性弹性计算中


# TODO 计算弹性部分，为mean调用的菜单函数

def open_window_price():
    global format_H
    global other_a
    global other_b
    #TODO 通过传入的不同模型，用导入的类创建对象（技术弹性window的对象）
    win_price = window_exceptEL()
    win_price.start_window()
    #TODO 技术弹性的按钮函数函数
    def command1():



        now_need = float(win_price.E_nowneed.get())  # 当下需求
        past_need = float(win_price.E_pastneed.get())  # 过去uuid
        now_price = float(win_price.E_np.get())  # 当下价格
        past_price = float(win_price.E_pp.get())  # 过去价格
        format_H = win_price.LB.get(win_price.LB.curselection())  # 模型类别
        ELasticity = MoneyElasticity(now_need, now_price, past_need, past_price, format_H)
        # 系数b
        elasticity, other_a ,other_b= ELasticity.get_price_elasticity()  # 弹性,常数a
        # TODO 进一步提出建议，根据弹性
        win_price.E_tell.insert('end', '弹性:{}\n'.format(elasticity))
        if format_H=='线性':
            win_price.E_tell.insert('end','模型为:Q={:.3f}p+{:.3f}\n'.format(other_b,other_a))
        if format_H=='对数':
            win_price.E_tell.insert('end','模型为:lnQ={:.3f}lnp+{:.3f}\n'.format(other_b,other_a))
        if np.abs(elasticity) > 1:
            win_price.E_tell.insert('end', '富有弹性\n价格下降时，收益将增加')
        if np.abs(elasticity) < 1:
            win_price.E_tell.insert('end', '缺乏弹性\n价格下降时，收益下降')
        if np.abs(elasticity) == 1:
            win_price.E_tell.insert('end', '单位弹性\n价格下降时，收益不变')
        #TODO 触发预测，出现预测按钮（可调用预测函数）
        def forecast():
            fore_1(other_b, other_a,format_H)#预测函数声明，函数调用

        B_forecast = tk.Button(win_price.window_getEL, text='预测', command=forecast, height=1, width=10, bg='red')
        B_forecast.place(x=90, y=190)
        #启动command1的Button后显示预测按钮
    #
    def add_Button():
        B = tk.Button(win_price.window_getEL, text='开始', command=command1, height=1, width=10, bg='red')
        #command 按钮
        B_quit = tk.Button(win_price.window_getEL, text='退出', command=quit, height=1, width=10, bg='red')
        # B_forecast = tk.Button(win_income.window_getEL, text='预测', command=forecast, height=1, width=10, bg='red')
        B.place(x=90, y=130)
        B_quit.place(x=90, y=160)
        # B_forecast.place(x=90, y=190)
    #command的window的Button声明

    # time.sleep(1)
    # mainwin.mainwindow.destroy()
    #TODO 将对象图形布置好，然后mainloop（启动调用）
    add_Button()
    win_price.window_getEL.mainloop()
    # 在菜单open_window_price调用时调用add_Button,启动布局，mainloop呈现


def open_window_income():
    global format_H
    global other_a
    global other_b

    win_income = window_exceptEL()
    win_income.start_window()

    def command1():

        now_need = float(win_income.E_nowneed.get())
        past_need = float(win_income.E_pastneed.get())
        now_price = float(win_income.E_np.get())
        past_price = float(win_income.E_pp.get())
        format_H = win_income.LB.get(win_income.LB.curselection())
        ELasticity = IncomeElasticity(now_need, now_price, past_need, past_price, format_H)
        elasticity ,other_a,other_b= ELasticity.get_income_elasticity()
        # TODO 进一步提出建议，根据弹性

        win_income.E_tell.insert('end', '弹性:{}\n'.format(elasticity))
        if format_H=='线性':
            win_income.E_tell.insert('end','模型为:Q={:.3f}p+{:.3f}\n'.format(other_b,other_a))
        if format_H=='对数':
            win_income.E_tell.insert('end','模型为:lnQ={:.3f}lnp+{:.3f}\n'.format(other_b,other_a))
        if np.abs(elasticity) > 1:
            win_income.E_tell.insert('end', '富有弹性\n收入下降时，收益将增加')
        if np.abs(elasticity) < 1:
            win_income.E_tell.insert('end', '缺乏弹性\n收入下降时，收益下降')
        if np.abs(elasticity) == 1:
            win_income.E_tell.insert('end', '单位弹性\n收入下降时，收益不变')

        def forecast():
            fore_1(other_b, other_a, format_H)

        B_forecast = tk.Button(win_income.window_getEL, text='预测', command=forecast, height=1, width=10, bg='red')
        B_forecast.place(x=90, y=190)

    def add_Button():
        B = tk.Button(win_income.window_getEL, text='开始', command=command1, height=1, width=10, bg='red')
        B_quit = tk.Button(win_income.window_getEL, text='退出', command=quit, height=1, width=10, bg='red')
        # B_forecast = tk.Button(win_income.window_getEL, text='预测', command=forecast, height=1, width=10, bg='red')
        B.place(x=90, y=130)
        B_quit.place(x=90, y=160)
        # B_forecast.place(x=90, y=190)

    # time.sleep(1)
    # mainwin.mainwindow.destroy()
    add_Button()
    win_income.window_getEL.mainloop()


def open_window_cross():
    global format_H
    global other_a
    global other_b

    win_cross = window_exceptEL()
    win_cross.start_window()

    def command1():


        now_need = float(win_cross.E_nowneed.get())
        past_need = float(win_cross.E_pastneed.get())
        now_price = float(win_cross.E_np.get())
        past_price = float(win_cross.E_pp.get())
        format_H = win_cross.LB.get(win_cross.LB.curselection())
        ELasticity = CrossPriceElasticity(now_need, now_price, past_need, past_price, format_H)
        elasticity,other_a,other_b = ELasticity.get_CrossPrice_Elastictiy()
        # TODO 进一步提出建议，根据弹性
        win_cross.E_tell.insert('end', '弹性:{:.3f}\n'.format(elasticity))
        if format_H=='线性':
            win_cross.E_tell.insert('end','模型为:Q={:.3f}p+{:.3f}\n'.format(other_b,other_a))
        if format_H=='对数':
            win_cross.E_tell.insert('end','模型为:lnQ={:.3f}lnp+{:.3f}\n'.format(other_b,other_a))
        if elasticity > 0:
            win_cross.E_tell.insert('end', '1价格与2的需求同方向变动，两种运输见有可替代性\n')
        if elasticity < 0:
            win_cross.E_tell.insert('end', '1价格与2的需求反方向变动，两种运输之间存在互补关系\n')

        def forecast():
            fore_1(other_b, other_a, format_H)

        B_forecast = tk.Button(win_cross.window_getEL, text='预测', command=forecast, height=1, width=10, bg='red')
        B_forecast.place(x=90, y=190)

    def add_Button():

        B = tk.Button(win_cross.window_getEL, text='开始', command=command1, height=1, width=10, bg='red')
        B_quit = tk.Button(win_cross.window_getEL, text='退出', command=quit, height=1, width=10, bg='red')
        # B_forecast = tk.Button(win_cross.window_getEL, text='预测', command=forecast, height=1, width=10, bg='red')
        B.place(x=90, y=130)
        B_quit.place(x=90, y=160)
        # B_forecast.place(x=90, y=190)

    # time.sleep(1)
    # mainwin.mainwindow.destroy()
    add_Button()
    win_cross.window_getEL.mainloop()

#TODO 设置各个菜单栏
def startpro():
    # mainwin = MainWindow()
    mainwin.choicemenu.add_command(label='价格', command=open_window_price)
    mainwin.choicemenu.add_command(label='收入', command=open_window_income)
    mainwin.choicemenu.add_command(label='交叉', command=open_window_cross)
    mainwin.choicemenu.add_separator()
    mainwin.choicemenu.add_command(label='退出', command=quit)
    mainwin.mainwindow.config(menu=mainwin.menu)
    # mainwin.forecastmenu.add_command(label='预测', command=fore)
    # mainwin.mainwindow.config(menu=mainwin.menu)
    mainwin.get_functionmenu.add_command(label='货运量与GDP回归模型', command=GDP_n_function)
    mainwin.mainwindow.config(menu=mainwin.menu)

    mainwin.mainwindow.mainloop()


if __name__ == '__main__':
    startpro()

# self.choicemenu.add_cascade(label='价格',command=open_window_price)
# self.choicemenu.add_cascade(label='价格',command=open_window_income)
# self.choicemenu.add_cascade(label='交叉',command=open_window_cross)

# TODO visual stdio 太难看了
