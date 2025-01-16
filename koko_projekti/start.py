import main
import alkupeli
import main2

print('1992 超喜3in1歡玩')
print('快點啟動遊戲吧')
peli_names = ['ADVENTURER: 1', 'CLOUDRUNNER: 2', 'not?availible: 3']
for peli in peli_names:
    print(peli)

choice = int(input('valitse peli: '))

if choice == 1:
    main.main() 
elif choice == 2:
    alkupeli.run_alkupeli()
elif choice == 3:
    main2.start()