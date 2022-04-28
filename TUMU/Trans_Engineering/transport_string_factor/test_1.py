import TUMU.Trans_Engineering.trans_survey.transportation_survey_delay_IO as TI_O

tuple1=(80,100,120,90,70,70)
tuple2=(80,90,90,90,90,90)
list1=[303,17,70]
list2=[(68,(40,22),56,(18,32),60),(56,(42,18),58,(20,40),62)]
list3=[18,58,20]
label=[1,2]
list1=[(4,7,8),(18,93,78),(104,326,238),(8,27,11),(1,12,5)]
label=['大','中','小','公','货']
list34=[2,1.5,1,1,2.5]
if __name__=='__main__':

    # p=transportation_survey_delay_IO.Trans_IO([tuple1,tuple2])
    # k=transportation_survey_delay_IO.Tran_floating_car_speed([(2,29,1.5),(2,28.6,1.0)])
    # l=transportation_survey_delay_IO.Trans_cross()

    # k= TUMU.Trans_Engineering.transportation_survey.transportation_survey_delay_IO.Trans_BasicQ(list1, label)
    # ll=k.draw_pie(list34)
    # kk=k.Max_trans_phf("63	71	70	76	93	95	131	128	62	67	102	118",5)
    # kk.show()
    # print(k.__doc__)
    k=TI_O.Trans_IO_K(list2,2,8,0.8)
    print(k.__doc__)




