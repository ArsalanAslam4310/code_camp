def maximum(lis):
    max = 0
    new = []
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if max < lis[i][j]:
                max = lis[i][j]
        new.append(max)
    return new


li = [[1, 2, 11, 3], [1, 27, 18, 26], [
    32, 35, 37, 39], [100, 1001, 857, 1]]
print(maximum(li))





# Alternative solution

# def maximum(lis):
#     max = 0
#     new = []
#     for i in range(len(lis)):
#         for j in lis[i]:
#             if max < j:
#                 max = j
#         new.append(max)
#     return new


# li = [[111, 2, 11, 3], [133, 27, 18, 26], [
#     323, 35, 37, 39], [10003, 1001, 857, 1]]
# print(maximum(li))



