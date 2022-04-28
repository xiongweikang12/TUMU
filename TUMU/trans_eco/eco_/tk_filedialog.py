import time
from tkinter import filedialog
from tkinter import scrolledtext
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#TODO 回归分析模块，与前面独立的一部分，由菜单command触发
def start_all():
    window = tk.Tk()
    window.title('选择文件进行回归分析')
    window.geometry('300x200')
    filepath = ''
    L_B = tk.Listbox(window, height=4, width=30)
    for i in ['line', 'line_log', 'log_log']:
        L_B.insert('end', i)
    L_B.pack()
    E_tell = scrolledtext.ScrolledText(window, height=7, width=40)
    E_tell.pack()

    def section_file():
        global filepath
        filepath = filedialog.askopenfilename(filetypes=[('xls', '.xls')])
        filepath = str(filepath)
        print(filepath)

        def input_sheet():
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示正文标签
            plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
            sheet_work = pd.read_excel(str(filepath))
            N_now = sheet_work['转量当年值'].values
            GDP_now = sheet_work['GDP当年值'].values

            # if L_B.curselection()=='line':
            def diff_mol(x, y, mol):
                plt.scatter(x, y)
                slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)
                E_tell.insert('end', '相关系数:{:.2f}\n'.format(rvalue))
                if mol == 'line':
                    E_tell.insert('end', 'Q={:.2f}+{:.2f}xGDP\n'.format(intercept, slope))
                    el_line = slope * (x / y)
                    el_line = el_line[::2]
                    E_tell.insert('end', '弹性:{}'.format([round(i, 4) for i in el_line]))
                if mol == 'line_log':
                    E_tell.insert("end", 'Q={:.2f}+{:.2f}xlnGDP\n'.format(intercept, slope))
                    el_line_log = slope / (y)
                    el_line_log = el_line_log[::2]
                    E_tell.insert('end', '弹性:{}'.format([round(i, 4) for i in el_line_log]))
                if mol == 'log_log':
                    E_tell.insert("end", 'lnQ={:.2f}+{:.2f}xlnGDP\n'.format(intercept, slope))
                    el_log_log = slope
                    E_tell.insert('end', '弹性:{:.3f}'.format(slope))

                def myfunc(x):
                    return slope * x + intercept

                getmodel = list(map(myfunc, x))
                plt.plot(x, getmodel)
                time.sleep(1)
                plt.show()

            if L_B.get(L_B.curselection()) == 'line':
                diff_mol(GDP_now, N_now, 'line')
            if L_B.get(L_B.curselection()) == 'line_log':
                GDP_now_log = [np.log(i) for i in GDP_now]
                diff_mol(GDP_now_log, N_now, 'line_log')
            if L_B.get(L_B.curselection()) == 'log_log':
                GDP_now_log = [np.log(i) for i in GDP_now]
                N_now_log = [np.log(i) for i in N_now]
                diff_mol(GDP_now_log, N_now_log, 'log_log')

        input_sheet()

    B_section = tk.Button(window, text='选择文件', command=section_file)
    B_section.pack()
    window.mainloop()
