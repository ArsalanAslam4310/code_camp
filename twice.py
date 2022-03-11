from codecs import namereplace_errors


def twice(lis):
    new_li=[]

    for i in range(len(lis)):
        new_li.append(lis[i])
        new_li.append(lis[i])
    return new_li

lis=[4,9]
print(twice(lis))