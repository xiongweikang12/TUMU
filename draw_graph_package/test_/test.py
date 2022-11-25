from TUMU.experiment.experment_1.exper1 import lines_amount
from draw_graph_package.draw_line_graph import *

test_str = ["2:16——2:21",
            "2:21——2:26",
            "2:26——2:31",
            "2:31——2:36",
            "2:36——2:41",
            "2:41——2:46",
            "2:46——2:51",
            "2:51——2:56",
            "2:56——3:01",
            "3:01——3:06",
            "3:06——3:11",
            "3:11——3:16"
            ]

test_data = [[3,
              0,
              3,
              1,
              3,
              1,
              3,
              1,
              1,
              1,
              2,
              1
              ], [3,
                  0,
                  2,
                  2,
                  1,
                  1,
                  3,
                  2,
                  2,
                  2,
                  1,
                  1
                  ]]

Label_str = ["高新路东大路（南到北）", "高新路东大路（北到南）"]

a = lines_amount(listlabelx=test_str, listyamount=test_data, LabelList=Label_str, xlabel="", ylabel="公交车到达量",
                 rotation_x=30
                 , title="一小时公交车到站量")
