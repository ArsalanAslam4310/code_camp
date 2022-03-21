def where_do_i_belong(lis,num):
    
    for i in range(len(lis)):
        x = sorted(lis)
        if lis[i] >= num:
            lis[i] = num
            return i


lis=[5,3,20,3]
print(where_do_i_belong(lis,7))
