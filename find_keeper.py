def find_element(lis, func):
    '''

    '''
    for val in lis:
        if func(val):
            return val
    return None


li = [1, 3, 5, 9, 8]
print(find_element(li, lambda x: x % 2 == 0))
