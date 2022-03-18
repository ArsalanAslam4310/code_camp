def maximum(lis):
    max = 0
    new=[]
    for i in range(len(lis)):
        for j in lis[i]:
            if max < j:
                max = j
                new.append(max)
    return new

li=[[111, 2, 11, 3], [133, 27, 18, 26], [323, 35, 37, 39], [10003, 1001, 857, 1]]
print(maximum(li))
