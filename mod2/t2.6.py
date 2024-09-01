import random

code = []
code2 = []

eka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
toka = [1, 2, 3, 4, 5, 6]

for i in range(3):
    code.append(random.choice(eka))
    #code.append(random.randint(0, 9))

for i in range(4):
    code2.append(random.choice(toka))
    #code2.append(random.randint(1, 6))

print(code)
print(code2)