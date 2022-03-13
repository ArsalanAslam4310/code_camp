def muteation(lis,target):
    
    for i in range(len(lis)):
        if lis[i]== target:
            return True
        else:
            return False

stri=["hello"]
print(muteation(stri,"hello"))
