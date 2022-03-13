def get_index(lis,num):
    
    for i in range(len(lis)):
        if lis[i] >= num :
           return i

li=[5,8,12,20]
print(get_index(li,11))
