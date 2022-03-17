def large_word(string):
    maximum = 0
    sub_stri_leng = 0
    j = 0

    for i in range(len(string)):
        j = i
        sub_stri_leng = 0

        while string[j] != " " and j < len(string)-1:
            j += 1
            sub_stri_leng += 1
            if sub_stri_leng > maximum:
                maximum = sub_stri_leng

    return maximum


stri = "dbxjh hdbxjhnb jasbxnxb xbzjhbsdjhxgujhdb dbxn"
print(large_word(stri))
