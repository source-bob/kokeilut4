leivi = float(input('anna leviskät: '))
naulat = float(input('anna naulat: '))
luodit = float(input('anna luodit: '))

koko_massa = (leivi * 20 * 32 + naulat * 32 + luodit) * 13.3
kg = int(koko_massa // 1000)
gr = koko_massa - kg * 1000

print('Massa nykymittojen mukaan:')
print(f'{kg} kilogramma ja {gr:.2f} grammaa.')