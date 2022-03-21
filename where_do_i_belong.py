def get_index_to_ins(lis, num):
    sorted_copy = sorted(lis)
    i = 0
    while num >= sorted_copy[i]:
        i += 1
    return i


print(get_index_to_ins([0, 20, 30, 40, 50], 35))
