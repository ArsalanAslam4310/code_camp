def maximum(lis):
    max = 0
    new=[]

    for i in range(len(lis)):
        if max < lis[i][1]:
            max = lis[i][1]
            new.append(max)
    return new

li=[[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]
print(maximum(li))
