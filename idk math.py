code1 = 3897
code2 = 901873
step1 = code1 + code2
step2 = step1 * 2
print("Your final code is", step2)
code3= 40
code4= 5
step3 = code3 + code4
print("Your other code is", step3)
print(9*3)
print(18/6)
print(4+7)
print(20-12)
Hungry=True
Pizza=False
if Hungry==True: 
    if Pizza==True:
        print("Eat the Pizza")
    else:
        print("Make a sandwich")
else:
    print("Play soccer ig")
number=5
if (number):
    print("The number is truthy.")
zero=0
if (not zero):
    print("Zero is considered falsy.")
player_level=23
player_has_weapon=False
player_health=100
has_armor=True
has_magic_ring=True
if player_level >= 10:
    if player_has_weapon or has_armor:
        if player_health >= 50:
                print("\033[31mYou are ready to spill the blood of your enemies in battle.\033[0m")
                Requirements_Not_Met=False
        
            
        else:
            Requirements_Not_Met=True
            if Requirements_Not_Met and has_magic_ring:
                Dont_Print=True
            if not Dont_Print:
                print("You need to heal before battle!")
    else:
        Requirements_Not_Met=True
        if Requirements_Not_Met and has_magic_ring:
            Dont_Print=True
        if not Dont_Print: 
            print("You need a weapon or armor to fight!")
else:
    Requirements_Not_Met=True
    if Requirements_Not_Met and has_magic_ring:
        Dont_Print=True
    if not Dont_Print:
        print("You need a higher player level!")

if Requirements_Not_Met and has_magic_ring:
    Dont_Print=True
    print("The ring allows you to GET FRIED LOL")
def say_hello(name):
    print(f"Hello, {name}!")
say_hello("Random name")
