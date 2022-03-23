def lisreturn(value):
    new = []
    for i in range(len(value)):
        value+=" ,"+ value[i]
        new.append(value[i])
    return new


string="hcbcjh"
print(lisreturn(string))  
