def confirm_ending(string,target):

    for i in range(len(string)-1,-1,-1):
        i -= 1
        for j in range(len(target)-1,-1,-1):
            j -= 1
            if string[i]==target[j]:
                return True
            else:
                return False
            
        
string="fbhdvkbfkc jdnck"
target=" jdnck"
print(confirm_ending(string,target))
