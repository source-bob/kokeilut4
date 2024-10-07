from traceback import print_tb

import lisata
import fuktion2
import fuktion1
import random1
import random
import time
from colorama import Fore, Back, Style, init

import text_fuktion, fuktion3, tunus, testi, fuktion4, fuktion5
from fuktion4 import date_goal
import fuktion5

def run_alkupeli():
    gas1= 10
    gas2= 20
    gas3= 40
    player_fuel= 60
    gas5= 80
    gas6= 100
    less_gasoline= -10
    less_gasoline= -20
    less_gasoline= -50
    level = 1
    leve2 = 2
    leve3 = 3
    player_points = 500
    points2 = 1000

    print("""
            |========================================[-][o][x]|
            |                                                 |                                               
            |               'TERVETULOA PELI!'                |
            |                                                 |                                                                                                |
            |=================================================|    """)
    init()
    print(Fore.RED + 'GAME GUIDE'+ Style.RESET_ALL)

    Text1 ="""AGENT, YOUR MISSION STARTS NOW:
    FIRST, YOU MUST REGISTER.
    THEN, YOU WILL CHOOSE THE CONTINENT 
    WHERE YOU WILL START YOUR MISSION, 
    AND AT THE SAME TIME, THE COUNTRY WILL
    BE ASSIGNED TO YOU. YOU WILL BE TRAVELING 
    THROUGH DIFFERENT AIRPORTS, TRYING TO CAPTURE 
    THE VILLAIN WHO HAS STOLEN SECRET INFORMATION. 
    DURING YOUR TRAVELS, YOU MUST KEEP TRACK OF 
    YOUR FUEL LEVEL AND ROLL THE DICE 
    TO REFUEL WHEN NECESSARY.
    ADDITIONALLY, YOU WILL FACE VARIOUS CHALLENGES 
    ALONG THE WAY, WHICH WILL BE EXPLAINED TO YOU AS 
    YOU PROGRESS. THE VILLAIN ISN'T VERY CLEVER AND WILL 
    LEAVE YOU CLUES AT EACH AIRPORT. 
    ONE OF THE MAIN OBSTACLES WILL BE THE CONSTANT 
    DECREASE IN FUEL, SO YOU MUST BE VERY CAREFUL.

    GOOD LUCK, OFFICER!
    """
    text_fuktion.print_with_delay(Text1)
    #make the text go slowly

    #====

    #change text color
    print(Fore.RED+"REGISTER:"+Style.RESET_ALL)
    #===
    first_name=input("FIRST_NAME: ")
    last_name=input("LAST_NAME: ")
    ident= tunus.agenti_tunus()
    age=int(input("AGE: "))

    #Function 2 records in the database
    fuktion2.date(first_name,last_name,ident, age)
    print()

    #SALAINEN AVAIN ON
    print("YOUR SECRET KEY IS:", Fore.RED+ident+Style.RESET_ALL)
    print()
    Text7="""CHOOSE THE CONTINENT 
            WHERE YOU WANT TO START PLAYING"""
    text_fuktion.print_with_delay(Text7)
    print()
    print("""
            ======================
            CONTINENT :
            Asia            =   AS
            Africa          =   AF
            North America   =   NA
            South America   =   SA
            Antarctica      =   AT
            Europe          =   EU
            Australi        =   AU
            ======================
            """)

    Play_start = input("CONTINENT TO START: ")
    continet={"AS":"Asia", "AF":"Africa", "NA":"North_America", "SA":"South_America", "AT":"Antarctica", "EU":"Europe", "AU":"Australi"}
    konet = {"S":"AIRBUS 319", "M":"AIRBUS 321" ,"L":"BOEING 777" }
    print("""
    =====================
    AIRCRAFT MODELS
            "SMALL"  = S
    "MEDIUM_SIZE"  = M 
            "LARGE"  = L
    =====================
            """)
    plane=input( " CHERISH THE AIRPLANE :")
    #GAS LEVER
    if plane in konet:
        if plane=="S":
            print(f"YOUR GAS LEVEL IS{gas6}")
        elif plane=="M":
            print(f"YOUR GAS LEVEL IS{gas5}")
        elif plane=="L":
            print(f"YOUR GAS LEVEL IS{player_fuel}")

    if Play_start in continet:
        print(f"YOUR MISSION BEGINS!\n YOU WILL START ON THE CONTINENT {Fore.RED + continet[Play_start]+ Style.RESET_ALL}")
        cont=continet[Play_start]
        country = fuktion1.continet(Play_start)
        print(f"  IN THE COUNTRY OF {Fore.RED +country + Style.RESET_ALL} ")



        city2 = fuktion3.airport_name_city(country)
        print(F"AIRPORT NAME IS {Fore.RED+city2[0]+Style.RESET_ALL} IS LOCATE {Fore.RED+city2[1]+Style.RESET_ALL}")
        fuktion4.date_goal(first_name,level,cont,city2[0],ident,player_points,player_fuel)
    print()


    Text2 = """
            IT SEEMS THAT THE THIEF IS NO LONGER 
            HERE, ROLL THE DICE TO JUMP TO THE 
            NEXT AIRPORT """
    text_fuktion.print_with_delay(Text2)
    print()

    #heito noppaa1
    #vaihto lento kenta1
    game_dice = input('ROLL THE DICE "D": ')
    if game_dice== "D":
        if Play_start in continet:
            country = fuktion1.continet(Play_start)
            city2 = fuktion3.airport_name_city(country)
            print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED+country+Style.RESET_ALL}")
            print(f"THE AIRPORT IS{Fore.RED+city2[0]+Style.RESET_ALL} IN THE CITY OF {Fore.RED+city2[1]+Style.RESET_ALL}")

    print()

    Text3 ="""IT SEEMS THE VILLAIN HAS BEEN TO THIS AIRPORT, BUT
    HE’S NOT CLEVER ENOUGH AND HAS LEFT YOU CLUES. 
    YOU HAVE THREE GATES TO CHOOSE FROM, BUT IF YOU PICK 
    THE WRONG ONE, YOU COULD RUN INTO TROUBLE. 
    GOOD LUCK!
    """
    text_fuktion.print_with_delay(Text3)
    print()

    doorA= input('CHOOSE THE DOOR "A" "B" "C":')
    print()
    #palauta  random texti
    if doorA=="A":
        elect_TA = random1.random_T()
        print(elect_TA)
    elif doorA=="B":
        elect_TB = random1.random_T()
        print(elect_TB)

    elif doorA=="C":
        elect_TC = random1.random_T()
        print(elect_TC)

    print()

    #vaihto lentokenta2
    Text4= """
            YOU HAVE TO CONTINUE WITH THE TRIP
            ROLL THE DICE AGAIN TO CHANGE AIRPORTS
            """
    text_fuktion.print_with_delay(Text4)
    print()
    #heito noppaa2
    game_dice = input('ROLL THE DICE "D": ')
    if game_dice== "D":
        if Play_start in continet:
            country = fuktion1.continet(Play_start)
            city2 = fuktion3.airport_name_city(country)
            print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED+country+Style.RESET_ALL}")
            print(f"THE AIRPORT IS{Fore.RED+city2[0]+Style.RESET_ALL} IN THE CITY OF  {Fore.RED+city2[1]+Style.RESET_ALL}")
    print()
    Text5 = """ 
            WHEN YOUR FUEL IS REDUCED, 
            OPEN ONE OF THE DOORS TO REFUEL
            """
    text_fuktion.print_with_delay(Text5)
    print()
    door_B= input('CHOOSE THE DOOR "A" "B" "C":')
    if door_B=="A":
        elect_A = random1.random_A()
        if int(elect_A) >0 and int(elect_A)<= 100  :
            print(f" YOUR FUEL HAS INCREASED BY {elect_A}%" )


    elif door_B=="B":
        elect_B = random1.random_A()
        if int(elect_B) > 0 and int(elect_B) <= 100:
            print(f" YOUR FUEL HAS INCREASED BY {elect_B}%")


    elif door_B=="C":
        elect_C = random1.random_A()
        if int(elect_C) > 0 and int(elect_C) <= 100:
            print(f" YOUR FUEL HAS INCREASED BY {elect_C}%")


    print()
    #vaihto lento kenta2
    Text4= """
            YOU HAVE TO CONTINUE WITH THE TRIP
            ROLL THE DICE AGAIN TO CHANGE AIRPORTS
            """
    text_fuktion.print_with_delay(Text4)
    print()
    game_dice = input('ROLL THE DICE "D": ')
    if game_dice== "D":
        if Play_start in continet:
            country = fuktion1.continet(Play_start)
            city2 = fuktion3.airport_name_city(country)
            print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED+country+Style.RESET_ALL}")
            print(f"THE AIRPORT IS{Fore.RED+city2[0]+Style.RESET_ALL} IN THE CITY OF  {Fore.RED+city2[1]+Style.RESET_ALL}")
    print()

    #ovi arvaus
    Text5 = """ 
            OPEN SOME OF THE DOORS TO INCREAS\n YOUR POINTS
            """
    text_fuktion.print_with_delay(Text5)
    print()
    door_c= input('CHOOSE THE DOOR "A" "B" "C":')
    if door_c=="A":
        elect_A = random1.random_B()
        points_incremet= lisata.incrementar_columna(ident, elect_A)
        if int(elect_A) >= 100 and int(elect_A) <= 500:
            print(f" YOU HAVE OBTAINED {elect_A} MORE POINTS ")
    elif door_c=="B":
        elect_B = random1.random_B()
        points_incremet = lisata.incrementar_columna(ident, elect_B)
        if int(elect_B) >=100 and int(elect_B) <= 500:
            print(f" YOU HAVE OBTAINED {elect_B} MORE POINTS ")
    elif door_c=="C":
        elect_C = random1.random_B()
        points_incremet = lisata.incrementar_columna(ident, elect_C)
        if int(elect_C) >=100 and int(elect_C) <= 500:
            print(f" YOU HAVE OBTAINED {elect_C} MORE POINTS ")


    Text4 = """
            YOU HAVE TO CONTINUE WITH THE TRIP
            ROLL THE DICE AGAIN TO CHANGE AIRPORTS
            """
    text_fuktion.print_with_delay(Text4)
    print()
    game_dice = input('ROLL THE DICE "D": ')
    if game_dice == "D":
        if Play_start in continet:
            country = fuktion1.continet(Play_start)
            city2 = fuktion3.airport_name_city(country)
            print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED + country + Style.RESET_ALL}")
            print(
                f"THE AIRPORT IS{Fore.RED + city2[0] + Style.RESET_ALL} IN THE CITY OF  {Fore.RED + city2[1] + Style.RESET_ALL}")
    print()

    # ovi arvaus
    Text5 = """ 
            YOUR SKILLS LEARNED DURING THE GAME 
            HAVE PAID FRUIT. CHOOSE ONE OF THE 
            DOORS. IT IS POSSIBLE THAT THE THIEF 
            IS IN ONE OF THE DOORS.
            """
    text_fuktion.print_with_delay(Text5)
    print()
    door_c = input('CHOOSE THE DOOR "A" "B" "C":')
    if door_c == "A":
        elect_C = random1.random_C()
        print(elect_C)
        if elect_C == "thief":
            print("YOU HAVE MANAGED TO CATCH THE THIEF, CONGRATULATIONS!")
        if elect_C == "time":
            print('YOUR TIME IS RUNNING OUT YOU HAVE TO GO \n'
                'FASTER THE THIEF IS NEXT TO THE AIRPORT DOOR "B"')
        if elect_C == "mail":
            print("YOU HAVE INTERCEPTED A SECRET MESSAGE FROM THE THIEF\n"
                'MAIL: "THE THIEF IS AT DOOR "A"')
        if elect_C == "code":
            code = ("ENTER YOUR CODE TO GET SECRET INFORMATION:")
            if code == ident:
                print('EL LADRON ESTA EN LA PUERTA "C"')



    elif door_c == "B":
        elect_C = random1.random_C()
        print(elect_C)
        if elect_C == "thief":
            print("YOU HAVE MANAGED TO CATCH THE THIEF, CONGRATULATIONS!")
        if elect_C == "time":
            print('YOUR TIME IS RUNNING OUT YOU HAVE TO GO \n'
                'FASTER EL LADRON ESTA LA SIGUIENTE AEROPUERTO LA PUERTA "B"')
        if elect_C == "mail":
            print("YOU HAVE INTERCEPTED A SECRET MESSAGE FROM THE THIEF\n"
                'MAIL: "THE THIEF IS AT DOOR "A"')
        if elect_C == "code":
            code = ("ENTER YOUR CODE TO GET SECRET INFORMATION:")
            if code == ident:
                print('EL LADRON ESTA EN LA PUERTA "C"')



    elif door_c == "C":
        elect_C = random1.random_C()
        print(elect_C)
        if elect_C == "thief":
            print("YOU HAVE MANAGED TO CATCH THE THIEF, CONGRATULATIONS!")
        if elect_C == "time":
            print('YOUR TIME IS RUNNING OUT YOU HAVE TO GO \n'
                'FASTER EL LADRON ESTA LA SIGUIENTE AEROPUERTO LA PUERTA "B"')
        if elect_C == "mail":
            print("YOU HAVE INTERCEPTED A SECRET MESSAGE FROM THE THIEF\n"
                'MAIL: "THE THIEF IS AT DOOR "A"')
        if elect_C == "code":
            code=("ENTER YOUR CODE TO GET SECRET INFORMATION:")
            if code == ident:
                print('HE THIEF IS AT THE DOOR "C"')

    print()
    game_dice = input('ROLL THE DICE "D": ')
    if game_dice == "D":
        if Play_start in continet:
            country = fuktion1.continet(Play_start)
            city2 = fuktion3.airport_name_city(country)
            print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED + country + Style.RESET_ALL}")
            print(
                f"THE AIRPORT IS{Fore.RED + city2[0] + Style.RESET_ALL} IN THE CITY OF  {Fore.RED + city2[1] + Style.RESET_ALL}")
    print()
    door_E= input('CHOOSE THE DOOR "A" "B" "C":')
    if door_E=="A":
        print(Fore.RED+"YOU HAVE CAUGHT THE THIEF CONGRATULATIONS!"+ Style.RESET_ALL)
        print()
        fuktion5.final_date(ident)

    elif door_B=="B":
        print(Fore.RED + "YOU HAVE CAUGHT THE THIEF CONGRATULATIONS!" + Style.RESET_ALL)
        print()
        fuktion5.final_date(ident)

    elif door_B=="C":
        print(Fore.RED + "YOU HAVE CAUGHT THE THIEF CONGRATULATIONS!" + Style.RESET_ALL)
        print()
        fuktion5.final_date(ident)