def differnce_in_list(list1,list2):
    new=[]
    for i in range(len(list1)):
        if list1[i] not in list2:
            new.append(list1[i]) 
    return new
                
li=[4,5,6,7,8]
lis=[4,5,6]
print(differnce_in_list(li,lis))
