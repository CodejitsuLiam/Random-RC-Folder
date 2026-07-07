#yaycode
while True:
    try: 
        pet_type_ip=int(input("Choose the type of pet you want- type 1 for dog, 2 for cat, and 3 for dragon. "))
        if 1<= pet_type_ip <4:
            break
        else:
            print("Please enter 1, 2, or 3 ")
    except ValueError:
        print("Please enter 1, 2, or 3 ")
#values
hunger=80
energy=80
cleanliness=80
happiness=100-(50-(cleanliness/2))-(50-(energy/2))
health=100-(20-(happiness/5))-(40-(hunger/2.5))-(40-(energy/2.5))  
#petmodifiers
if pet_type_ip== 1:
    pet_type= "dog"
    petmoji= "🐕"
    special_bonus= "starts with more hunger"
    hunger=hunger+10
    special_weakness= "starts with less cleanliness"
    cleanliness=cleanliness-10
if pet_type_ip== 2:
    pet_type= "cat"
    petmoji= "🐈"
    special_bonus= "starts with more cleanliness"
    cleanliness=cleanliness+10
    special_weakness= "starts with less energy"
    energy=energy-10
if pet_type_ip== 3:
    pet_type= "dragon"
    petmoji= "🐉"
    special_bonus= "starts with more energy"
    energy=energy+10
    special_weakness= "starts with less hunger"
    hunger=hunger-10
#random code ig 
pet_name=input("Choose the name you want for your pet. ")
print("Your pet is " + pet_name + " the " + pet_type + ".\n" + petmoji)
#eastereggs!
if pet_type_ip == 3 and pet_name == "Midlife Crisis":
    print("You need help.")
elif pet_type_ip == 1 and pet_name == "William":
    print("Yo same!!!")
elif pet_type_ip == 2 and pet_name == "Binka":
    print("RIP")

x_row_health= "x" * int(health/10)
x_row_hunger= "x" * int(hunger/10)
x_row_happiness= "x" * int(happiness/10)
print("Starting happiness: " + x_row_happiness)
print("Starting health: " + x_row_health)
print("Starting hunger: " + x_row_hunger)
while health>0: 
    action=input("A new day begins... what do you want to do? Enter 1 to rest your pet, enter 2 to feed your pet, and enter 3 to clean your pet. You can also press 4 to do nothing. ")
    if action== "1":
        energy=energy+20
    elif action== "2":
        hunger=hunger+20
    elif action== "3":
        cleanliness=cleanliness+20
    elif action== "4":
        pass
    else:
        print("That is not an option!")
    action2=input("The day comes to an end... Choose something to do at the end of the day. The same rules as before apply. ")
    if action2== "1":
        energy=energy+20
    elif action2== "2":
        hunger=hunger+20
    elif action2== "3":
        cleanliness=cleanliness+20
    elif action2== "4":
        pass
    else:
        print("That is not an option!")
    if hunger > 100:
        print("Your pet is at maximum hunger!")
        hunger = 100
    elif hunger < 0:
        print("Your pet is now sick...")
        hunger = 0

    if cleanliness > 100:
        print("Your pet is at maximum cleanliness!")
        cleanliness = 100
    elif cleanliness < 0:
        print("Your pet is very dirty...")
        cleanliness = 0

    if energy > 100:
        print("Your pet is at maximum energy!")
        energy = 100
    elif energy < 0:
        print("Your pet needs some sleep...")
        energy = 0
    happiness=100-(50-(cleanliness/2))-(50-(energy/2))
    health=100-(20-(happiness/5))-(40-(hunger/2.5))-(40-(energy/2.5))
    x_row_health= "x" * int(health/10)
    x_row_hunger= "x" * int(hunger/10)
    x_row_happiness= "x" * int(happiness/10)
    print("Happiness: " + str(x_row_happiness))
    print("Health: " + str(x_row_health))
    print("Hunger: " + str(x_row_hunger))
    energy -=10
    hunger -=10
    cleanliness -=10
    if health <=0:
        print("\033[31mGame Over!\033[0m")

import sys
sys.exit()