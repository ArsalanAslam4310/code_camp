def confirm_the_ending(string,target):
    for j in range(-1,-len(string),-1):
        print(string[j])
        for i in range(-1,-len(target),-1):
            if target[i]==string[j]:
                return True
            else:
                return False
        


string=["asadfre hg"]
target= ["g"]
print(confirm_the_ending(string,target))
