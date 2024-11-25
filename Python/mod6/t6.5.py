def korja_list(lista):
    return [item for item in lista if item % 2 == 0]

if __name__ == '__main__':
    my_list = list(range(1, 9))
    my_list2 = list(range(1, 15))

    cleared_list = korja_list(my_list)
    cleared_list2 = korja_list(my_list2)

    print(f'Alkuperäinen: {my_list}\nCleared list: {cleared_list}')
    print(f'Alkuperäinen: {my_list2}\nCleared list: {cleared_list2}')