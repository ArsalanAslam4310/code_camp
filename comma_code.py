def list_to_string(lis):
    '''
    convert list to string
    '''
    new = ""
    for i in range(len(lis)):
        if i == len(lis)-1:
            new += ", and "+lis[i]
        else:
            new += lis[i]+", "

    return new


lis = ['apple', 'bananas', 'tofu', 'cats']
print(list_to_string(lis))
