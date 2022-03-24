def list_to_string(lis):
    '''convert lis to string
    '''
    new =""
    for i in range(len(lis)):
       new +=", "+lis[i]
    return new


string=['apple', 'bananas', 'tofu', 'cats']
print(list_to_string(string))  
