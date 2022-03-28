def findElement(lis):
  '''Find even number'''
    for i in range(len(lis)):
        if lis[i]%2==0:
            return lis[i]

li=[1, 3, 5, 9]
print(findElement(li))
