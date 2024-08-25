def pizza_laskin(halk, hinta):
    r = (halk / 2) / 100
    pi = 3.14
    s = pi * r**2
    hinnasto = hinta / s
    return hinnasto

pizza1_d = float(input('pizzan1 halk (cm): '))
pizza1_h = float(input('pizzan1 hinta (euro): '))
pizza2_d = float(input('pizzan2 halk (cm): '))
pizza2_h = float(input('pizzan2 hinta (euro): '))

pizza1 = pizza_laskin(pizza1_d, pizza1_h)
pizza2 = pizza_laskin(pizza2_d, pizza2_h)

if pizza1 > pizza2:
    print(f'pizza2 ({pizza2:.2f} e / neliö) halvempi kuin pizza1 {pizza1:.2f} e / neliö')
elif pizza2 > pizza1:
    print(f'pizza1 ({pizza1:.2f} e / neliö) halvempi kuin pizza2 ({pizza2:.2f} e / neliö)')
else:
    print(f'tasan ({pizza1:.2f} e / neliö)')






