import random

maara = int(input('anna määrä: '))

lista = list(range(1, 7))
count = []
for i in range(maara):
    count.append(random.choice(lista))
print(count)
print(sum(count))