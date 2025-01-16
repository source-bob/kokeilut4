
ajat = ('kevät', 'kesä', 'syksy', 'talvi')
osat = ('alku', 'keski', 'loppu')

alkukuu = (3, 6, 9, 12)
keskikuu = (4, 7, 10, 1)
loppukuu = (5, 8, 11, 2)

kaikki_kuut = alkukuu, keskikuu, loppukuu

while True:
    kuu = int(input('anna kuukausi (0 - lopeta): '))
    if kuu == 0:
        print('kiitos käynnistä')
        break
    elif kuu < 0 or kuu > 12:
        raise ValueError('virheellinen syöte')
    else:
        i = 0
        while i < len(kaikki_kuut):
            if kuu in kaikki_kuut[i]:
                print(f'sesonki on {ajat[kaikki_kuut[i].index(kuu)]} {osat[i]}')
            i += 1

