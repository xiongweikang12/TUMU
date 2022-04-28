import tkinter as tk

#TODO 设置主菜单菜单的相关内容，的类
class MainWindow:

    def __init__(self):
        self.mainwindow = tk.Tk()
        self.mainwindow.title('选择不同的模型')
        self.mainwindow.geometry('200x200')
        self.menu = tk.Menu(self.mainwindow)
        self.choicemenu = tk.Menu(self.menu, tearoff=False)
        self.get_functionmenu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='choice mol', menu=self.choicemenu)
        self.forecastmenu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='forecast', menu=self.forecastmenu)
        self.menu.add_cascade(label='log', menu=self.get_functionmenu)

        # self.choicemenu.add_cascade(label='价格',command=open_window_price)
        # self.choicemenu.add_cascade(label='价格',command=open_window_income)
        # self.choicemenu.add_cascade(label='交叉',command=open_window_cross)
