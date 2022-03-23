def lisreturn(value):
    new = []
    for i in range(len(value)):
        value+=" ,"
        new.append(value[i])
    return new


string="hcbcjh"
print(lisreturn(string))  
