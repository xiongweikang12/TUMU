import warnings

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")
# font = {'family': 'Time New Roman', 'size': 12}
# sns.set(font_scale=1.2)
# plt.rc('font', family='Time New Roman')
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示。
plt.style.use('ggplot')


# feature=["Sensitivity","Specificity","Accuracy","AUC"]

def draw_radar_graph_groups(data_grouds, label_grouds, classify_mode, title_):
    angles = np.linspace(0, 2 * np.pi, len(label_grouds), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    label_grouds = np.concatenate((label_grouds, [label_grouds[0]]))
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)

    for data in data_grouds:
        data = np.concatenate((data, [data[0]]))
        ax.plot(angles, data, 'o-', linewidth=2)
    for data in data_grouds:
        data = np.concatenate((data, [data[0]]))  # 填充颜色
        ax.fill(angles, data, alpha=0.3)

    ax.set_thetagrids(angles * 180 / np.pi, label_grouds, fontsize=14, style='italic')
    ax.set_ylim(0.2, 1)
    ax.set_theta_zero_location('N')
    ax.set_rlabel_position(270)
    plt.legend(classify_mode)  # classify_mode [" "..]与data_groud长度一致
    plt.title(title_)


    return plt



"""

data_grouds = [[0.46, 0.28, 0.35, 0.6, 0.69, 0.38, 0.71], [0.73, 0.36, 0.2, 0.69, 0.88, 0.5, 0.85]]
label_grouds=["冲突点数目","换乘时间比","换乘距离","绕行系数","换乘安全性","工作人员数","换乘舒适性"]
classify_mode=["现状方案","优化后方案"]
title="各项指标的模糊隶属度值"
a=draw_radar_graph_groups(data_grouds,label_grouds,classify_mode,title_=title)
a.show()


"""