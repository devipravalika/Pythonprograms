color_list1=set(["white","Black","Red"])
color_list2=set(["Red","Green"])
color_list3=[]
for ele in color_list1:
    if ele not in color_list2:
        color_list3.append(ele)
print(color_list3)
