import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import scrolledtext  # 滚动文本框

#TODO 定义预测框，与计算弹性框的类
class window_exceptEL:

    def __init__(self):
        self.window_getEL = tk.Tk()
        self.L = tk.Label(self.window_getEL, text='获取弹性')
        self.LB = tk.Listbox(self.window_getEL)
        for item in ['线性', '对数']:
            self.LB.insert("end", item)
        # self.B=tk.Button(self.window_getEL,text='开始',command=command1,height=1,width=10,bg='red')
        # self.B_quit=tk.Button(self.window_getEL,text='退出',command=quit,height=1,width=10,bg='red')
        self.E_nowneed = tk.Entry(self.window_getEL)
        self.E_pastneed = tk.Entry(self.window_getEL)
        self.E_np = tk.Entry(self.window_getEL)
        self.E_pp = tk.Entry(self.window_getEL)
        self.L_nn = tk.Label(self.window_getEL, text='nn:')
        self.L_pn = tk.Label(self.window_getEL, text='pn:')
        self.L_np = tk.Label(self.window_getEL, text='np:')
        self.L_pp = tk.Label(self.window_getEL, text='pp:')
        self.E_tell = scrolledtext.ScrolledText(self.window_getEL, height=30, width=50)

    def start_window(self):
        self.window_getEL.title('输入数据并得到弹性')
        self.window_getEL.geometry('400x400')
        self.L.place(x=175, y=5)
        self.L_nn.place(x=15, y=30)
        self.E_nowneed.place(x=60, y=30)
        self.L_pn.place(x=15, y=50)
        self.E_pastneed.place(x=60, y=50)
        self.L_np.place(x=15, y=70)
        self.E_np.place(x=60, y=70)
        self.L_pp.place(x=15, y=90)
        self.E_pp.place(x=60, y=90)
        # self.B.place(x=90,y=130)
        # self.B_quit.place(x=90,y=160)
        self.E_tell.place(x=0, y=250)
        self.LB.place(x=250, y=10)


class foreWindow():

    def __init__(self):
        self.fore = tk.Tk()
        self.L_sec_forecast = tk.Label(self.fore, text='选择需要预测对象')
        self.L_inputexpress_forecast = tk.Label(self.fore, text='输入预测根据:')
        self.E_forecast = tk.Entry(self.fore)
        self.E_tell_result_forecast = scrolledtext.ScrolledText(self.fore, height=4, width=40)

    def start_forecast(self):
        self.fore.title('预测')
        self.fore.geometry('300x200')
        self.L_sec_forecast.place(x=100, y=5)
        self.L_inputexpress_forecast.place(x=5, y=80)
        self.E_forecast.place(x=90, y=80)
        self.E_tell_result_forecast.place(x=0, y=130)
