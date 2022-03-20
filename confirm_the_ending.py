def confirm_the_ending(string,target):
    for i in range(len(string)-1,-1,-1):
        for j in range(len(target)-1,-1,-1):
            if string[i]==target[j]:
                return True
            else:
                return False

string="asadfre hg"
target= "hg"
print(confirm_the_ending(string,target))
