def confirm_the_ending(string, target):
    flag = True
    for j in range(-1, -(len(target))-1, -1):
        if target[j] == string[j]:
            flag = True
        else:
            flag = False
            break
    if flag:
        return flag
    return flag


string = "asadfre hg"
target = "  g"
print(len(target))
print(confirm_the_ending(string, target))
