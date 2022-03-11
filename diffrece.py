def difference(lis1,lis2):
    new=[]
    
    for item in lis1:
        if item not in  lis2:
            new.append(item)
    return new

lis1=[4,5,6,7]
lis2=[4,5,9]
print(difference(lis1,lis2))