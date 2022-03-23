def confirm_the_ending(string,target):
    j = len(target)-1
    j -= 1
    
    for i in range(len(string)-1,-1,-1):
        if string[i]==target[j]:
            return True
        else:
            return False


string=["asadfre hg"]
target= ["hjg"]
print(confirm_the_ending(string,target))
