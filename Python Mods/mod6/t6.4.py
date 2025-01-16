def lista_summa(lista):
    return sum(lista)

if __name__ == '__main__':
    list_of_nums = list(range(1, 9))
    list_of_nums2 = list(range(1, 11))
    summ = lista_summa(list_of_nums)
    summ2 = lista_summa(list_of_nums2)
    print(f'sum of my list: {summ}, length of my list: {len(list_of_nums)}')
    print(f'sum of my list: {summ2}, length of my list: {len(list_of_nums2)}')