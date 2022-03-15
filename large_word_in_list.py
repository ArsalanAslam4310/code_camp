def large_word(lis):
    maximum = len(lis)

    for word in lis:
        if len(word)>maximum:
            maximum= len(word)
    return maximum

li=["dbxjh","hdbxjhnb","jasbxnxb","xbzjhbsdjhxgujhdb","dbxn"]
print(large_word(li))
