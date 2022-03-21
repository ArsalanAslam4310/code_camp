def confirm_ending(string, target):
    flag = False
    j = len(target)-1
    i = len(string)-1

    while i >= 0 and j >= 0:
        if string[i] == target[j]:
            flag = True
        else:
            flag = False
            break
        i -= 1
        j -= 1

    if flag:
        return True
    return False


string = "asadf re hg"
target = "adf re hg"
print(confirm_ending(string, target))
